/* enCloud9 forms: remember where a visitor came from, then send every site form to /wp-json/n9/v1/form.
   The plugin saves each entry and posts it to ClickDimensions, which creates the lead in Dynamics. */
(function () {
  var cfg = window.n9Forms || {};
  var KEY = 'n9_touch';
  var loaded = Date.now();

  /* ---- where the visitor came from: first visit kept, this visit refreshed when it carries a source */
  function store() { try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; } }
  function save(o) { try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  (function track() {
    var q = new URLSearchParams(location.search), t = store(), now = {};
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid'].forEach(function (k) {
      if (q.get(k)) now[k] = q.get(k).slice(0, 200);
    });
    var ref = document.referrer, host = '';
    try { host = ref ? new URL(ref).hostname : ''; } catch (e) {}
    if (host && host !== location.hostname) now.referrer = ref.slice(0, 250);
    var fresh = Object.keys(now).length > 0;
    if (!t.first_seen) {
      t.first_seen = new Date().toISOString();
      t.first_landing = location.href.slice(0, 250);
      t.first_utm_source = now.utm_source || ''; t.first_utm_medium = now.utm_medium || '';
      t.first_utm_campaign = now.utm_campaign || ''; t.first_referrer = now.referrer || '';
    }
    if (fresh) {
      ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'referrer'].forEach(function (k) { t[k] = now[k] || ''; });
      t.landing = location.href.slice(0, 250);
    }
    save(t);
  })();

  /* ---- which form is this */
  function kindOf(f) {
    if (f.dataset.n9Form) return f.dataset.n9Form;
    if (f.id === 'n9-news') return 'newsletter';
    if (f.id === 'prep') return 'callprep';
    if (f.id === 'book') return 'storage';
    if (f.id === 'get') return 'guide';
    if (f.id === 'consult') return 'consult';
    if (f.id === 'cform') return f.querySelector('[name="asset"]') ? 'check' : 'contact';
    return '';
  }

  function msgEl(f) {
    var m = f.querySelector('.fm-msg') || f.querySelector('#cmsg') || f.querySelector('.msg');
    if (!m) { m = document.createElement('p'); m.className = 'fm-msg'; m.setAttribute('role', 'status'); m.setAttribute('aria-live', 'polite'); f.appendChild(m); }
    return m;
  }
  function say(f, text) { var m = msgEl(f); m.hidden = false; m.textContent = ''; setTimeout(function () { m.textContent = text; }, 40); }

  function labelOf(el) {
    var fs = el.closest('fieldset');
    if (fs && fs.querySelector('legend')) return fs.querySelector('legend').textContent.replace(/Required/g, '').trim();
    if (el.type === 'checkbox') return 'the privacy policy box';
    var l = el.closest('label'), s = l && (l.querySelector('span') || l);
    var t = s ? (s.childNodes[0] && s.childNodes[0].nodeType === 3 ? s.childNodes[0].textContent : s.textContent) : '';
    return (t || el.name || 'a field').replace(/Required/g, '').trim();
  }

  function honeypot(f) {
    if (f.querySelector('[name="n9_hp"]')) return;
    var w = document.createElement('div');
    w.setAttribute('aria-hidden', 'true');
    w.style.cssText = 'position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden';
    w.innerHTML = '<label>Leave this empty<input type="text" name="n9_hp" tabindex="-1" autocomplete="off"></label>';
    f.appendChild(w);
  }

  function collect(f) {
    var out = {};
    Array.prototype.forEach.call(f.elements, function (el) {
      if (!el.name || el.name === 'n9_hp' || el.disabled) return;
      if ((el.type === 'radio') && !el.checked) return;
      if (el.type === 'checkbox') { if (el.checked) out[el.name] = 'yes'; return; }
      out[el.name] = el.value;
    });
    return out;
  }

  function onSubmit(ev) {
    var f = ev.target;
    if (!(f instanceof HTMLFormElement)) return;
    var kind = kindOf(f);
    if (!kind || !cfg.endpoint) return;
    // This handler owns the send; the design's own placeholder handlers must not run.
    ev.preventDefault();
    ev.stopImmediatePropagation();
    if (f.dataset.n9Busy) return;

    f.querySelectorAll('[aria-invalid]').forEach(function (e) { e.removeAttribute('aria-invalid'); });
    var bad = [], seen = {};
    Array.prototype.forEach.call(f.elements, function (e) {
      if (e.willValidate && !e.checkValidity()) {
        e.setAttribute('aria-invalid', 'true');
        var n = labelOf(e);
        if (!seen[n]) { seen[n] = 1; bad.push({ n: n, e: e }); }
      }
    });
    if (bad.length) { bad[0].e.focus(); say(f, 'Fill in: ' + bad.map(function (b) { return b.n; }).join(', ') + '.'); return; }

    var btn = f.querySelector('[type="submit"]');
    f.dataset.n9Busy = '1';
    if (btn) { loader(btn); btn.disabled = true; btn.setAttribute('aria-busy', 'true'); }
    say(f, 'Sending...');

    var hp = f.querySelector('[name="n9_hp"]');
    fetch(cfg.endpoint, {
      method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ kind: kind, fields: collect(f), touch: store(), page: location.href.split('#')[0],
        title: document.title, n9_hp: hp ? hp.value : '', n9_age: Date.now() - loaded })
    }).then(function (r) { return r.json().then(function (j) { return { s: r.status, j: j }; }); })
      .then(function (res) {
        if (res.j && res.j.ok) {
          try { if (window.gtag) gtag('event', 'generate_lead', { form_name: kind }); } catch (e) {}
          if (res.j.thanks) { location.href = res.j.thanks; return; }
          f.reset();
          say(f, 'Thanks. We have your answers and will use them on the call.');
        } else if (res.s === 422) {
          say(f, 'Check: ' + ((res.j && res.j.fields) || []).join(', ') + '.');
        } else if (res.s === 429) {
          say(f, 'Too many tries. Wait a few minutes, or call 1-844-264-0729.');
        } else {
          say(f, 'That did not send. Try again, or call 1-844-264-0729.');
        }
      })
      .catch(function () { say(f, 'That did not send. Try again, or call 1-844-264-0729.'); })
      .then(function () { delete f.dataset.n9Busy; if (btn) { btn.disabled = false; btn.removeAttribute('aria-busy'); } });
  }

  /* Button row (logo-motion a06_row, on-blue): three squares show while a form sends.
     The label stays in the button for screen readers; aria-busy already says it is busy. */
  function loader(btn) {
    if (!document.getElementById('n9-row-css')) {
      var st = document.createElement('style'); st.id = 'n9-row-css';
      st.textContent = 'button[aria-busy="true"]{position:relative;color:transparent!important}' +
        '.n9-row{display:none;position:absolute;inset:0;margin:auto;width:28px;height:8px;gap:2px;pointer-events:none}' +
        'button[aria-busy="true"] .n9-row{display:flex}' +
        '.n9-row i{width:8px;height:8px;background:#fff}' +
        '@media (prefers-reduced-motion:no-preference){.n9-row i{animation:n9r 600ms cubic-bezier(.2,.7,.2,1) infinite both}' +
        '.n9-row i:nth-child(2){animation-delay:-400ms}.n9-row i:nth-child(3){animation-delay:-200ms}}' +
        '@keyframes n9r{0%,8.33%{opacity:1}33.33%,41.67%{opacity:.6}66.67%,75%{opacity:.3}100%{opacity:1}}';
      document.head.appendChild(st);
    }
    if (!btn.querySelector('.n9-row')) {
      var r = document.createElement('span'); r.className = 'n9-row'; r.setAttribute('aria-hidden', 'true');
      r.innerHTML = '<i></i><i></i><i></i>'; btn.appendChild(r);
    }
  }

  function ready() { document.querySelectorAll('form').forEach(function (f) { if (kindOf(f)) honeypot(f); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready); else ready();
  // Capture phase: runs before the design's own submit handlers on the form.
  window.addEventListener('submit', onSubmit, true);
})();
