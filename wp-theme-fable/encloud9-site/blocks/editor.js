/**
 * enCloud9 blocks for the editor. No build step: plain script, WordPress globals.
 *
 * encloud9/section  One section of a page. It stores the design's own markup, unchanged. In the editor the
 *                   section looks as it does on the site; click any text to change it. Links and images are
 *                   changed in the sidebar. The element structure cannot change: an edit that would remove
 *                   or add a styled part is undone on the spot.
 * encloud9/box      An element that only holds other blocks (the page wrap, an article frame). Its children
 *                   cannot be moved, removed or added to, unless the box is the running text of a post.
 */
(function (wp) {
  'use strict';
  var el = wp.element.createElement,
    useRef = wp.element.useRef,
    useEffect = wp.element.useEffect,
    useLayoutEffect = wp.element.useLayoutEffect,
    useMemo = wp.element.useMemo,
    RawHTML = wp.element.RawHTML,
    be = wp.blockEditor,
    co = wp.components,
    cfg = window.n9Editor || {};

  var SKIP = 'script,style,svg,canvas,select,textarea,input,button,iframe,video,audio,form [type=submit]';
  var FORMAT = /^(b|i|strong|em|u)$/;

  function parseRoot(html) {
    var t = document.createElement('template');
    t.innerHTML = (html || '').trim();
    return t.content.firstElementChild;
  }

  function hasDirectText(n) {
    for (var c = n.firstChild; c; c = c.nextSibling) {
      if (c.nodeType === 3 && c.nodeValue.replace(/[\s ]+/g, '') !== '') return true;
    }
    return false;
  }

  /* The editable pieces: the outermost elements that hold text directly. */
  function findLeaves(root) {
    var out = [], all = [root].concat([].slice.call(root.querySelectorAll('*')));
    all.forEach(function (n) {
      if (out.length && out[out.length - 1].contains(n)) return;
      if (n.closest(SKIP) || n.closest('[aria-hidden="true"]')) return;
      if (hasDirectText(n)) out.push(n);
    });
    return out;
  }

  /* Tags and classes of everything inside, ignoring plain bold and italic and line breaks. */
  function skeleton(node) {
    var s = [];
    [].forEach.call(node.querySelectorAll('*'), function (x) {
      var t = x.tagName.toLowerCase();
      if (t === 'br') return;
      if (FORMAT.test(t) && !x.attributes.length && x.textContent !== '') return;
      s.push(t + '.' + (x.getAttribute('class') || ''));
    });
    return s.join('|');
  }

  function label(html) {
    var r = parseRoot(html);
    if (!r) return '';
    var h = r.matches('h1,h2,h3') ? r : r.querySelector('h1,h2,h3,summary,b,strong');
    var t = ((h || r).textContent || '').replace(/\s+/g, ' ').trim();
    return t.length > 60 ? t.slice(0, 57) + '...' : t;
  }

  /* A short name for a link in the sidebar: its main line if it is a card, else its words. */
  function linkName(a) {
    var main = a.querySelector('.nm,.t,h3,b,strong');
    var t = main ? main.textContent : a.innerHTML.replace(/<[^>]+>/g, ' ').replace(/&[a-z#0-9]+;/gi, ' ');
    t = (t || '').replace(/\s+/g, ' ').trim() || a.getAttribute('aria-label') || 'Link';
    return t;
  }

  function notice(msg) {
    wp.data.dispatch('core/notices').createNotice('warning', msg, { type: 'snackbar', id: 'n9-locked' });
  }

  /* ---------------------------------------------------------------- section */
  function SectionEdit(props) {
    var content = props.attributes.content || '';
    var ref = useRef(null);
    var live = useRef({ emitted: null, shown: null, timer: 0, leaves: [] });
    var tpl = useMemo(function () { return parseRoot(content); }, [content]);
    var tag = tpl ? tpl.tagName.toLowerCase() : 'div';
    var bodyClass = wp.data.useSelect(function (select) {
      var ed = select('core/editor');
      return (ed && ed.getEditorSettings && (ed.getEditorSettings() || {}).n9BodyClass) || '';
    }, []);

    function serialize() {
      var node = ref.current, c = node.cloneNode(true), shell = parseRoot(live.current.shown);
      [].forEach.call(c.querySelectorAll('[data-n9]'), function (x) {
        x.removeAttribute('contenteditable'); x.removeAttribute('data-n9'); x.removeAttribute('spellcheck');
      });
      [].forEach.call(c.querySelectorAll('[data-n9-d]'), function (x) { x.removeAttribute('draggable'); x.removeAttribute('data-n9-d'); });
      [].forEach.call(c.querySelectorAll('details[data-n9-o]'), function (x) {
        if (x.getAttribute('data-n9-o') === '1') x.setAttribute('open', ''); else x.removeAttribute('open');
        x.removeAttribute('data-n9-o');
      });
      shell.innerHTML = c.innerHTML;
      return shell.outerHTML;
    }

    function commit() {
      var L = live.current;
      clearTimeout(L.timer); L.timer = 0;
      if (!ref.current || L.shown === null) return;
      var html = serialize();
      if (html === L.emitted) return;
      L.emitted = html; L.shown = html;
      props.setAttributes({ content: html });
    }

    function prepare(node) {
      var L = live.current;
      [].forEach.call(node.querySelectorAll('details'), function (d) { d.setAttribute('data-n9-o', d.hasAttribute('open') ? '1' : '0'); });
      [].forEach.call(node.querySelectorAll('a,img'), function (a) {
        if (!a.hasAttribute('draggable')) { a.setAttribute('draggable', 'false'); a.setAttribute('data-n9-d', '1'); }
      });
      L.leaves = findLeaves(node);
      L.leaves.forEach(function (x) {
        x.setAttribute('contenteditable', 'true'); x.setAttribute('data-n9', '1'); x.setAttribute('spellcheck', 'true');
        x._n9 = { skel: skeleton(x), good: x.innerHTML };
      });
    }

    /* Put the stored markup on the canvas when it changes from outside (first load, undo, redo). */
    useLayoutEffect(function () {
      var node = ref.current, L = live.current;
      if (!node || !tpl) return;
      if (L.shown !== null && content === L.emitted) return;
      [].forEach.call(tpl.attributes, function (a) {
        if (a.name === 'class' || a.name === 'id' || a.name === 'contenteditable' || a.name === 'tabindex' || a.name === 'role') return;
        if (a.name === 'aria-labelledby' || a.name === 'aria-label') return;   // the editor names the block itself
        node.setAttribute(a.name, a.value);
      });
      node.innerHTML = tpl.innerHTML;
      L.shown = content; L.emitted = content;
      prepare(node);
    }, [content]);

    /* The canvas wears the page's body class, as the site does. */
    useEffect(function () {
      var node = ref.current;
      if (!node || !bodyClass) return;
      bodyClass.split(/\s+/).forEach(function (c) { if (c) node.ownerDocument.body.classList.add(c); });
    }, [bodyClass]);

    useEffect(function () {
      var node = ref.current;
      if (!node) return;
      var L = live.current;
      function leafOf(t) { return t && t.closest ? t.closest('[data-n9]') : null; }
      function onInput(e) {
        var leaf = leafOf(e.target);
        if (!leaf || !leaf._n9) return;
        if (skeleton(leaf) !== leaf._n9.skel) {
          leaf.innerHTML = leaf._n9.good;
          var sel = node.ownerDocument.getSelection(), r = node.ownerDocument.createRange();
          r.selectNodeContents(leaf); r.collapse(false); sel.removeAllRanges(); sel.addRange(r);
          notice('That would remove a link or a styled part of this section, so it was undone. Change the words inside it instead.');
          return;
        }
        leaf._n9.good = leaf.innerHTML;
        clearTimeout(L.timer);
        L.timer = setTimeout(commit, 400);
      }
      function onBeforeInput(e) {
        if (!leafOf(e.target)) return;
        var t = e.inputType || '';
        if (t === 'insertParagraph' || t === 'insertOrderedList' || t === 'insertUnorderedList' || t === 'insertHorizontalRule' ||
            t === 'formatIndent' || t === 'formatOutdent' || t.indexOf('formatJustify') === 0 || t === 'formatFontName' ||
            t === 'formatBackColor' || t === 'formatFontColor' || t === 'insertFromDrop' || t === 'formatRemove') {
          e.preventDefault();
        }
      }
      function onPaste(e) {
        if (!leafOf(e.target)) return;
        e.preventDefault(); e.stopPropagation();
        var text = (e.clipboardData || window.clipboardData).getData('text/plain').replace(/\s*\n\s*/g, ' ');
        node.ownerDocument.execCommand('insertText', false, text);
      }
      function onKeyDown(e) {
        if ((e.ctrlKey || e.metaKey) && (e.key === 's' || e.key === 'S')) commit();
        if (!leafOf(e.target)) return;
        if (e.key === 'Enter' && !e.shiftKey) e.preventDefault();
      }
      function onKeyUp(e) {
        // a space typed in an editable <summary> must not open or close its <details>
        if ((e.key === ' ' || e.key === 'Enter') && leafOf(e.target) && e.target.closest('summary')) e.preventDefault();
      }
      function onClick(e) {
        var a = e.target.closest && e.target.closest('a,button,[type=submit]');
        if (a && node.contains(a) && !(a.tagName === 'BUTTON' && a.closest('summary'))) e.preventDefault();
      }
      function onSubmit(e) { e.preventDefault(); }
      function onDrop(e) { if (leafOf(e.target)) e.preventDefault(); }
      node.addEventListener('input', onInput);
      node.addEventListener('beforeinput', onBeforeInput);
      node.addEventListener('paste', onPaste, true);
      node.addEventListener('keydown', onKeyDown);
      node.addEventListener('keyup', onKeyUp);
      node.addEventListener('click', onClick);
      node.addEventListener('submit', onSubmit);
      node.addEventListener('drop', onDrop);
      node.addEventListener('focusout', commit);
      return function () {
        if (L.timer) commit();
        node.removeEventListener('input', onInput);
        node.removeEventListener('beforeinput', onBeforeInput);
        node.removeEventListener('paste', onPaste, true);
        node.removeEventListener('keydown', onKeyDown);
        node.removeEventListener('keyup', onKeyUp);
        node.removeEventListener('click', onClick);
        node.removeEventListener('submit', onSubmit);
        node.removeEventListener('drop', onDrop);
        node.removeEventListener('focusout', commit);
      };
    }, []);

    /* Links and images are changed here, by position, on the live canvas; then stored. */
    function setOn(selector, i, fn) {
      var x = ref.current && ref.current.querySelectorAll(selector)[i];
      if (!x) return;
      fn(x);
      commit();
    }
    var links = tpl ? [].slice.call(tpl.querySelectorAll('a[href]')) : [];
    if (tpl && tpl.matches('a[href]')) links = [];   // a section that is itself one link keeps its target with the block around it
    var images = tpl ? [].slice.call(tpl.querySelectorAll('img')) : [];

    var blockProps = be.useBlockProps({ ref: ref, className: (tpl ? tpl.getAttribute('class') || '' : '') + ' n9-section' });

    return el(wp.element.Fragment, null,
      el(be.InspectorControls, null,
        el(co.PanelBody, { title: 'How to edit this section', initialOpen: true },
          el('p', null, 'Click any text on the page and type. The layout is locked, so nothing can shift or break.'),
          el('p', null, 'Links, buttons and images are changed below.')),
        links.length ? el(co.PanelBody, { title: 'Links and buttons (' + links.length + ')', initialOpen: links.length < 9 },
          links.map(function (a, i) {
            var name = linkName(a);
            return el(co.TextControl, {
              key: i, label: name.length > 60 ? name.slice(0, 57) + '...' : name, value: a.getAttribute('href'),
              help: i === 0 ? 'Where it goes. A page on this site starts with / (for example /contact-us/).' : undefined,
              __nextHasNoMarginBottom: false, __next40pxDefaultSize: true,
              onChange: function (v) { setOn('a[href]', i, function (x) { x.setAttribute('href', v); }); }
            });
          })) : null,
        images.length ? el(co.PanelBody, { title: 'Images (' + images.length + ')', initialOpen: true },
          images.map(function (im, i) {
            return el('div', { key: i, className: 'n9-img-row' },
              el('img', { src: im.getAttribute('src'), alt: '', style: { maxWidth: '100%', maxHeight: 80, background: '#EAF0F9' } }),
              el(be.MediaUploadCheck, null, el(be.MediaUpload, {
                allowedTypes: ['image'],
                onSelect: function (m) {
                  setOn('img', i, function (x) {
                    x.setAttribute('src', m.url); x.removeAttribute('srcset'); x.removeAttribute('sizes');
                    if (m.alt && !x.getAttribute('alt')) x.setAttribute('alt', m.alt);
                  });
                },
                render: function (o) { return el(co.Button, { variant: 'secondary', onClick: o.open, __next40pxDefaultSize: true }, 'Replace image'); }
              })),
              el(co.TextControl, {
                label: 'Description for screen readers (alt text)', value: im.getAttribute('alt') || '',
                __nextHasNoMarginBottom: false, __next40pxDefaultSize: true,
                onChange: function (v) { setOn('img', i, function (x) { x.setAttribute('alt', v); }); }
              }));
          })) : null),
      el(tag, blockProps));
  }

  wp.blocks.registerBlockType('encloud9/section', {
    apiVersion: 3,
    title: 'Section',
    description: 'One section of the page, as designed. Change its words, links and images; the layout is locked.',
    category: 'design',
    icon: 'align-wide',
    attributes: { content: { type: 'string', source: 'raw' } },
    supports: { className: false, customClassName: false, html: false, anchor: false, reusable: true, lock: true },
    __experimentalLabel: function (a) { return label(a.content) || undefined; },
    edit: SectionEdit,
    save: function (props) { return el(RawHTML, null, props.attributes.content); }
  });

  /* ---------------------------------------------------------------- box */
  function propsFrom(attrs) {
    var p = {};
    Object.keys(attrs || {}).forEach(function (k) { p[k === 'class' ? 'className' : k] = attrs[k]; });
    return p;
  }

  function BoxEdit(props) {
    var a = props.attributes, attrs = a.attrs || {}, ref = useRef(null);
    var free = !!a.prose || !!a.unlocked;
    useEffect(function () {
      var node = ref.current;
      if (!node) return;
      Object.keys(attrs).forEach(function (k) {
        if (k === 'class' || k === 'id' || k === 'aria-labelledby' || k === 'aria-label' || k === 'role' || k === 'tabindex') return;
        node.setAttribute(k, attrs[k]);
      });
    });
    var blockProps = be.useBlockProps({ ref: ref, className: (attrs['class'] || '') + ' n9-box' });
    var inner = be.useInnerBlocksProps(blockProps, {
      templateLock: free ? false : 'all',
      renderAppender: free ? be.InnerBlocks.DefaultBlockAppender : false
    });
    return el(wp.element.Fragment, null,
      el(be.InspectorControls, null,
        el(co.PanelBody, { title: 'Layout container', initialOpen: true },
          el('p', null, a.prose
            ? 'The running text. Add, remove and reorder paragraphs, headings, lists and images freely.'
            : 'Holds the sections of this page in their designed order.'),
          !a.prose && cfg.canRestructure ? el(co.ToggleControl, {
            label: 'Unlock the order of sections', checked: !!a.unlocked, __nextHasNoMarginBottom: true,
            help: 'Site admins only. When on, sections here can be moved, removed and added.',
            onChange: function (v) { props.setAttributes({ unlocked: v || undefined }); }
          }) : null)),
      el(a.tag || 'div', inner));
  }

  wp.blocks.registerBlockType('encloud9/box', {
    apiVersion: 3,
    title: 'Layout container',
    description: 'Holds sections in their designed order.',
    category: 'design',
    icon: 'layout',
    attributes: {
      tag: { type: 'string', default: 'div' },
      attrs: { type: 'object', default: {} },
      prose: { type: 'boolean' },
      unlocked: { type: 'boolean' }
    },
    supports: { className: false, customClassName: false, html: false, anchor: false, reusable: false, lock: true },
    __experimentalLabel: function (a) { return a.prose ? 'Running text' : ((a.attrs && a.attrs['class']) === 'wrap' ? 'Page sections' : undefined); },
    edit: BoxEdit,
    save: function (props) {
      var a = props.attributes;
      return el(a.tag || 'div', propsFrom(a.attrs), el(be.InnerBlocks.Content));
    }
  });
})(window.wp);
