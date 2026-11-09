"""Build the running mock site from the Look 9 concept pages.

The concept pages in pages/ stay the one source. This script writes site/<real-url-path>/index.html
for every mapped page, so the mock site uses the real encloud9.com URL paths:
- every link to a concept page, or to a live encloud9.com URL we have built, becomes a local link;
- the lookbook bar is removed; asset paths are made relative to the repo root;
- links to pages not built yet stay pointed at the live site (listed in site/NOT-BUILT-YET.txt).
Run: python3 tools/build_site.py   (from the repo root)
"""
import os, re, shutil, posixpath

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, 'pages')
SITE = os.path.join(ROOT, 'site')
LIVE = 'https://www.encloud9.com'

# concept page -> real URL path (from SITE-STRUCTURE.md and each page's breadcrumb schema)
MAP = {
    'nine-home.html': '/',
    'nine-dynamics-365.html': '/power-platform-dynamics-365/',
    'nine-dynamics-365-sales.html': '/dynamics-365-sales/',
    'nine-customer-service.html': '/dynamics-365-customer-service/',
    'nine-marketing.html': '/marketing-services/',
    'nine-copilot.html': '/microsoft-copilot-for-business/',
    'nine-packages.html': '/crm-cloud-automation-solutions/',
    'nine-full-implementation.html': '/microsoft-dynamics-365-implementation/',
    'nine-rescue-repair.html': '/encloud9-dynamics-365-crm-services/dynamics-365-crm-solutions-rescue-repair/',
    'nine-sales-accelerator.html': '/dynamics-365-sales-accelerator/',
    'nine-service-accelerator.html': '/dynamics-365-service-accelerator/',
    'nine-stories.html': '/about-encloud9/microsoft-dynamics-365-success/',
    'nine-about.html': '/about-encloud9/',
    'nine-blog.html': '/blog/',
    'nine-blog-post.html': '/blog/generative-pages-dynamics-365/',
    'nine-blog-2024.html': '/blog/optimizing-sales-strategies-with-dynamics-365-enabling-and-utilizing-sales-usage-reports/',
    'nine-storage.html': '/lp/dataverse-storage-analysis/',
    'nine-move-salesforce.html': '/microsoft-dynamics-365-salesforce-crm-migration/',
    'nine-move-hubspot.html': '/lp/microsoft-dynamics-365-hubspot-crm-migration/',
}
PATHS = set(MAP.values())

def rel(from_path, to_path):
    """Relative link from one site path (a folder) to another site path (a folder) or file."""
    r = posixpath.relpath(to_path.rstrip('/') or '/', from_path.rstrip('/') or '/')
    if to_path.endswith('/'):
        r = (r + '/') if r != '.' else './'
    return r

not_built = {}

def rewrite(html, src, here):
    depth_to_root = rel(here, '/')            # e.g. '../../' (site root)
    repo = depth_to_root + '../'               # site/ sits in the repo root
    html = re.sub(r'<nav id="lbbar".*?</nav>\s*', '', html, flags=re.S)

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith(('mailto:', 'tel:', '#', 'data:', 'javascript:')):
            return m.group(0)
        frag = ''
        if '#' in url:
            url, frag = url.split('#', 1)
            frag = '#' + frag
        if url.startswith(LIVE):
            path = url[len(LIVE):] or '/'
            if not path.endswith('/') and '.' not in path.rsplit('/', 1)[-1]:
                path += '/'
            if path in PATHS:
                return f'{attr}="{rel(here, path)}{frag}"'
            if attr == 'href':
                not_built.setdefault(path, set()).add(src)
            return m.group(0)
        if url.startswith(('http://', 'https://', '//')):
            return m.group(0)
        if url in MAP:
            return f'{attr}="{rel(here, MAP[url])}{frag}"'
        if url == '' and frag:
            return m.group(0)
        if url.startswith('../'):
            return f'{attr}="{repo}{url[3:]}{frag}"'
        if url.endswith('.html') and url.startswith('nine-'):
            not_built.setdefault('(concept) ' + url, set()).add(src)
            return m.group(0)
        # files that live next to the concept pages (nine.css, nine.js, images)
        return f'{attr}="{repo}pages/{url}{frag}"'

    html = re.sub(r'\b(href|src)="([^"]*)"', fix, html)
    # concept page names inside scripts (for example the package picker), as quoted strings
    for k, v in MAP.items():
        html = html.replace(f"'{k}'", f"'{rel(here, v)}'")
    return html

def main():
    if os.path.isdir(SITE):
        shutil.rmtree(SITE)
    for src, path in MAP.items():
        with open(os.path.join(PAGES, src), encoding='utf-8') as f:
            html = f.read()
        out = rewrite(html, src, path)
        d = os.path.join(SITE, path.strip('/'))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(out)
    with open(os.path.join(SITE, 'NOT-BUILT-YET.txt'), 'w', encoding='utf-8') as f:
        f.write('Links on the mock site that still go to the live encloud9.com (page not built yet), with the pages that link to them.\n\n')
        for p in sorted(not_built):
            f.write(f'{p}  <- {", ".join(sorted(not_built[p]))}\n')
    print(f'built {len(MAP)} pages; {len(not_built)} link targets not built yet')

if __name__ == '__main__':
    main()
