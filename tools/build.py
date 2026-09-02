#!/usr/bin/env python3
"""Builds the Kreme Cruiser static site.

Every page shares one header, footer and <head> block so navigation and
metadata stay consistent. Run `python3 tools/build.py` after editing this
file, then commit the generated .html files.
"""

import os
import re

SITE_URL = "https://www.kremecruiser.com"
BRAND = "Kreme Cruiser"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

LOGO = """<a class="logo" href="index.html" aria-label="Kreme Cruiser home">
        <span class="logo-mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="5.5" cy="18" r="3"/><circle cx="18.5" cy="18" r="3"/>
            <path d="M8.5 18h7"/><path d="M6 18 9 8h8l2 10"/><path d="M8 8h10"/>
          </svg>
        </span>
        <span class="logo-type"><b>Kreme Cruiser</b><span>Shaved Ice Cart</span></span>
      </a>"""


def header(slug):
    items = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == slug else ""
        items.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    items.append('<li class="nav-cta"><a href="contact.html">Book the Cart</a></li>')
    links = "\n            ".join(items)
    return f"""  <header class="site-header">
    <div class="wrap header-inner">
      {LOGO}
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        Menu
      </button>
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
          <p style="margin-top:16px;max-width:34ch;">A pedal powered shaved ice cart that rolls up to schools, daycares, birthday parties and community events across the south Houston area.</p>
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
  "alternateName": "Kreme Cruiser Shaved Ice",
  "description": "Kreme Cruiser is a mobile shaved ice cart serving schools, daycares, birthday parties, church events and community gatherings in the south Houston area of Texas.",
  "url": "%(site)s/",
  "image": "%(site)s/assets/img/og-kreme-cruiser.jpg",
  "servesCuisine": "Shaved ice",
  "priceRange": "$$",
  "areaServed": [%(areas)s],
  "knowsAbout": ["Shaved ice catering", "School event catering", "Daycare treat days", "Birthday party catering"],
  "makesOffer": {
    "@type": "Offer",
    "itemOffered": {
      "@type": "Service",
      "name": "Mobile shaved ice cart service",
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
<meta property="og:image:alt" content="The Kreme Cruiser shaved ice cart parked under a teal umbrella beside its flavor menu board">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14b6cf">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
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
<script src="assets/js/site.js"></script>
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
        header=header(slug),
        crumbs=crumb_html,
        body=body,
        footer=FOOTER,
    )
    with open(os.path.join(ROOT, slug), "w", encoding="utf-8") as fh:
        fh.write(html)
    return slug
