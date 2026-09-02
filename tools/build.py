#!/usr/bin/env python3
"""Builds the Kreme Cruiser static site.

Every page shares one header, footer and <head> block so navigation and
metadata stay consistent. Run `python3 tools/build.py` after editing this
file, then commit the generated .html files.
"""

import hashlib
import os
import re

SITE_URL = "https://kreme-cruiser.netlify.app"
BRAND = "Kreme Cruiser"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _asset_version(relpath):
    """Content hash for a cache-busted asset URL.

    assets/* is served with a one year immutable cache, so a stable URL
    would pin visitors to whatever copy they downloaded first. Hashing the
    URL means new content is always a new URL.
    """
    full = os.path.join(ROOT, relpath)
    with open(full, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()[:10]


CSS_V = _asset_version("assets/css/style.css")
JS_V = _asset_version("assets/js/site.js")

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("flavors.html", "Flavors"),
    ("service-area.html", "Service Area"),
    ("gallery.html", "Gallery"),
    ("about.html", "About"),
    ("faq.html", "FAQ"),
]

FOOTER_SERVICES = [
    ("schools-and-daycares.html", "Schools &amp; Daycares"),
    ("birthday-parties.html", "Birthday Parties"),
    ("community-and-corporate-events.html", "Community &amp; Corporate"),
    ("services.html", "All Services"),
]

FOOTER_COMPANY = [
    ("about.html", "About Us"),
    ("flavors.html", "Flavor Menu"),
    ("service-area.html", "Service Area"),
    ("faq.html", "Questions"),
    ("contact.html", "Book the Cart"),
]

AREAS = [
    "Pearland", "Manvel", "Rosharon", "Iowa Colony", "Alvin", "Friendswood",
    "Fresno", "Missouri City", "Sienna", "Arcola", "League City", "South Houston",
]

LOGO = """<a class="logo" href="index.html">
        <img src="assets/img/kreme-cruiser-logo.png"
             srcset="assets/img/kreme-cruiser-logo.png 1x, assets/img/kreme-cruiser-logo@2x.png 2x, assets/img/kreme-cruiser-logo@3x.png 3x"
             width="77" height="84" alt="Kreme Cruiser" decoding="async">
      </a>"""


def header(slug):
    items = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == slug else ""
        items.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    items.append('<li class="nav-phone" data-contact-item hidden>'
                 '<a data-contact="phone" href="#">'
                 '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                 '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.4-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>'
                 '</svg><span data-contact-text>Phone</span></a></li>')
    items.append('<li class="nav-cta"><a href="contact.html">Book the Cart</a></li>')
    links = "\n            ".join(items)
    return f"""  <header class="site-header">
    <div class="wrap header-inner">
      {LOGO}
      <div class="header-actions">
        <a class="header-call" data-contact="phone" href="#" data-contact-item hidden aria-label="Call Kreme Cruiser">
          <svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.4-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/></svg>
          <span class="visually-hidden">Call</span>
        </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        Menu
      </button>
      </div>
      <nav class="site-nav" id="site-nav" aria-label="Main">
        <ul>
            {links}
        </ul>
      </nav>
    </div>
  </header>"""


FOOTER = """  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          {logo}
          <p style="margin-top:16px;max-width:34ch;">A pedal powered water ice cart that rolls up to schools, daycares, birthday parties and community events across the south Houston area.</p>
          <ul style="margin-top:18px;">
            <li data-contact-item hidden><a data-contact="phone" href="#">Phone</a></li>
            <li data-contact-item hidden><a data-contact="email" href="#">Email</a></li>
            <li data-contact-item hidden><a data-contact="facebook" href="#" rel="noopener">Facebook</a></li>
            <li data-contact-item hidden><a data-contact="instagram" href="#" rel="noopener">Instagram</a></li>
            <li data-contact-item hidden><a data-contact="tiktok" href="#" rel="noopener">TikTok</a></li>
          </ul>
        </div>
        <div>
          <h3>Services</h3>
          <ul>{services}</ul>
        </div>
        <div>
          <h3>Company</h3>
          <ul>{company}</ul>
        </div>
        <div>
          <h3>Service Area</h3>
          <p style="margin-bottom:10px;">Pearland, Manvel, Rosharon, Iowa Colony, Alvin, Fresno, Missouri City and the surrounding south Houston communities.</p>
          <a class="btn btn-primary" href="contact.html" style="margin-top:6px;">Check Your Date</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="mb-0">&copy; <span data-year>2026</span> Kreme Cruiser. All rights reserved.</p>
        <p class="mb-0"><a href="contact.html">Book the cart</a> &nbsp;&middot;&nbsp; <a href="service-area.html">Where we travel</a></p>
      </div>
    </div>
  </footer>""".format(
    logo=LOGO.replace('href="index.html"', 'href="index.html"'),
    services="".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOTER_SERVICES),
    company="".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOTER_COMPANY),
)


ORG_SCHEMA = """{
  "@context": "https://schema.org",
  "@type": "FoodEstablishment",
  "@id": "%(site)s/#business",
  "name": "Kreme Cruiser",
  "alternateName": "Kreme Cruiser Water Ice",
  "description": "Kreme Cruiser is a mobile water ice cart serving schools, daycares, birthday parties, church events and community gatherings in the south Houston area of Texas.",
  "url": "%(site)s/",
  "telephone": "+1-713-530-6835",
  "email": "info@kremecruiser.com",
  "sameAs": ["https://www.instagram.com/kreme_cruiser/", "https://www.facebook.com/p/Kreme-Cruiser-61588605541964/"],
  "image": "%(site)s/assets/img/og-kreme-cruiser.jpg",
  "servesCuisine": "Shaved ice",
  "priceRange": "$$",
  "areaServed": [%(areas)s],
  "knowsAbout": ["Shaved ice catering", "School event catering", "Daycare treat days", "Birthday party catering"],
  "makesOffer": {
    "@type": "Offer",
    "itemOffered": {
      "@type": "Service",
      "name": "Mobile water ice cart service",
      "serviceType": "Event catering"
    }
  }
}""" % {
    "site": SITE_URL,
    "areas": ", ".join('{"@type":"City","name":"%s, TX"}' % a for a in AREAS),
}


def breadcrumbs(trail):
    """trail: list of (href, label). Returns (html, json-ld)."""
    if not trail:
        return "", ""
    items = []
    ld = []
    for i, (href, label) in enumerate(trail, start=1):
        if i == len(trail):
            items.append(f'<li aria-current="page">{label}</li>')
        else:
            items.append(f'<li><a href="{href}">{label}</a></li>')
        ld.append(
            '{"@type":"ListItem","position":%d,"name":"%s","item":"%s/%s"}'
            % (i, re.sub("<[^>]+>", "", label).replace("&amp;", "and"), SITE_URL,
               "" if href == "index.html" else href)
        )
    html = ('  <div class="wrap crumbs"><nav aria-label="Breadcrumb"><ol>'
            + "".join(items) + "</ol></nav></div>")
    jsonld = ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
              + ",".join(ld) + "]}")
    return html, jsonld


SMALL_WORDS = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "nor",
    "of", "on", "onto", "or", "per", "so", "the", "to", "up", "via",
    "with", "yet",
}

_TOKEN = re.compile(r"[A-Za-z][A-Za-z'’]*")


def _title_case_headings(html):
    """Title case the text inside h1, h2 and h3 tags, leaving tags,
    entities and existing acronyms untouched."""

    def fix_heading(match):
        open_tag, inner, close_tag = match.group(1), match.group(2), match.group(3)
        # split into pieces: html tags, entities, and plain text
        pieces = re.split(r"(<[^>]+>|&[A-Za-z#0-9]+;)", inner)
        words = []
        for i, piece in enumerate(pieces):
            if i % 2 == 1:
                continue
            words.extend((i, m) for m in _TOKEN.finditer(piece))
        total = len(words)
        edits = {}
        for n, (piece_i, m) in enumerate(words):
            word = m.group(0)
            if word.isupper() and len(word) > 1:
                continue  # acronym such as PTO or FAQ
            lower = word.lower()
            first_or_last = (n == 0 or n == total - 1)
            new = word.capitalize() if (first_or_last or lower not in SMALL_WORDS) else lower
            if new != word:
                edits.setdefault(piece_i, []).append((m.start(), m.end(), new))
        for piece_i, changes in edits.items():
            text = pieces[piece_i]
            for start, end, new in reversed(changes):
                text = text[:start] + new + text[end:]
            pieces[piece_i] = text
        return open_tag + "".join(pieces) + close_tag

    return re.sub(r"(<(h[123])\b[^>]*>)(.*?)(</\2>)",
                  lambda m: fix_heading(re.match(r"(<h[123]\b[^>]*>)(.*)(</h[123]>)",
                                                 m.group(0), re.S)),
                  html, flags=re.S)


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{site}/{canonical}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kreme Cruiser">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{site}/{canonical}">
<meta property="og:image" content="{site}/assets/img/og-kreme-cruiser.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The Kreme Cruiser water ice cart parked under a teal umbrella beside its flavor menu board">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14b6cf">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap" media="print" onload="this.media='all';this.onload=null">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap"></noscript>
<link rel="stylesheet" href="assets/css/style.css?v={css_v}">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/img/favicon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<script type="application/ld+json">{org}</script>
{extra_schema}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{header}
<main id="main">
{crumbs}
{body}
</main>
{footer}
<script src="assets/js/site.js?v={js_v}"></script>
</body>
</html>
"""


def build(slug, title, description, body, trail=None, extra_schema=(), robots="index, follow"):
    crumb_html, crumb_ld = breadcrumbs(trail or [])
    schemas = list(extra_schema)
    if crumb_ld:
        schemas.append(crumb_ld)
    extra = "".join(
        '<script type="application/ld+json">%s</script>\n' % s for s in schemas
    )
    html = PAGE.format(
        title=title,
        description=description,
        site=SITE_URL,
        canonical="" if slug == "index.html" else slug,
        robots=robots,
        org=ORG_SCHEMA,
        extra_schema=extra,
        css_v=CSS_V,
        js_v=JS_V,
        header=header(slug),
        crumbs=crumb_html,
        body=body,
        footer=FOOTER,
    )
    html = _title_case_headings(html)
    with open(os.path.join(ROOT, slug), "w", encoding="utf-8") as fh:
        fh.write(html)
    return slug
