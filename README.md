# Kreme Cruiser Website

Static marketing site for Kreme Cruiser, a mobile shaved ice cart serving the south Houston area.
No build tooling required to view it. Open `index.html` in a browser, or run `python3 -m http.server`.

---

## Do this before launch

These five items are the only things blocking a live launch. Everything else is finished.

| # | Item | Where | Why it matters |
|---|------|-------|----------------|
| 1 | Add the Facebook page URL | `assets/js/site.js` | The link stays hidden until a URL is added. Phone, email and Instagram are already set. |
| 3 | Confirm the real domain | search and replace `https://www.kremecruiser.com` | Used in canonicals, Open Graph tags, `robots.txt` and `sitemap.xml`. |
| 4 | Confirm the service area list | `tools/build.py` (`AREAS`), then rebuild | The current list is an assumption based on where the cart has been photographed. Correct it before indexing. |
| 5 | Create a Google Business Profile | Google | Highest impact single action for this business. See the SEO notes below. |

### How to edit contact details

Open `assets/js/site.js` and fill in the `CONTACT` object:

```js
var CONTACT = {
  phone:     "(281) 555-0134",
  email:     "hello@kremecruiser.com",
  facebook:  "https://www.facebook.com/kremecruiser",
  instagram: "https://www.instagram.com/kreme_cruiser/",
  tiktok:    ""
};
```

Any value left as an empty string stays hidden on every page. No placeholder text is ever shown to a visitor.

---

## Editing content

Pages are generated so the header, footer, navigation and metadata stay identical everywhere.

```
tools/build.py    page shell, header, footer, schema, service area list
tools/pages.py    the actual page copy, titles and descriptions
```

To change wording, edit `tools/pages.py`, then:

```bash
cd tools && python3 pages.py
```

That rewrites the `.html` files in the project root. Commit both the source and the generated HTML.

If you would rather stop using the generator, delete `tools/` and edit the `.html` files directly.
They are plain, standalone HTML with no dependencies.

---

## Pages

| File | Purpose | Primary keyword target |
|------|---------|------------------------|
| `index.html` | Home | shaved ice cart Houston / mobile shaved ice |
| `services.html` | Service hub | shaved ice catering |
| `schools-and-daycares.html` | School and daycare bookings | shaved ice for schools, daycare treat day |
| `birthday-parties.html` | Birthday bookings | shaved ice cart rental birthday party |
| `community-and-corporate-events.html` | Church, nonprofit, corporate | shaved ice catering church event |
| `flavors.html` | Flavor menu | shaved ice flavors |
| `service-area.html` | Cities served | shaved ice Pearland / Manvel / Rosharon |
| `gallery.html` | Photos | supporting |
| `about.html` | Trust and process | brand |
| `faq.html` | Booking questions | long tail, FAQ rich result |
| `contact.html` | Booking form | book shaved ice cart |
| `thank-you.html` | Form success page, noindex | conversion tracking |
| `404.html` | Not found, noindex | n/a |

---

## Technical setup already in place

- Semantic HTML, one `h1` per page, logical heading order
- Unique title and meta description on every page, all within display limits
- Canonical URL, Open Graph and Twitter card tags on every page
- `FoodEstablishment` schema with `areaServed` on every page (service area business, no storefront address)
- `BreadcrumbList` schema plus visible breadcrumbs on interior pages
- `FAQPage` schema on `faq.html`, `Menu` schema on `flavors.html`
- `robots.txt` and `sitemap.xml`, with `thank-you.html` and `404.html` set to noindex
- Responsive images with `srcset` and `sizes`, lazy loading below the fold
- Mobile navigation with keyboard support and Escape to close
- Skip link, visible focus states, labeled form fields, alt text on every image
- No JavaScript framework, no render blocking scripts, one stylesheet

---

## Form handling

The booking form on `contact.html` is set up for **Netlify Forms**:

```html
<form name="booking" method="POST" data-netlify="true" netlify-honeypot="company-website" action="thank-you.html">
```

Deploy to Netlify and submissions appear under Forms in the site dashboard. Set up an email
notification there so booking requests do not sit unread.

Using a different host? Replace the form attributes with a Formspree or Basin endpoint:

```html
<form action="https://formspree.io/f/YOUR_ID" method="POST">
```

The honeypot field (`company-website`) is hidden off screen and catches most bot submissions.
Leave it in place regardless of which service you use.

---

## Deploying

**Netlify** (`netlify.toml` is already configured with caching headers, security headers and
short URL redirects such as `/book` and `/menu`):

1. Connect the repository in Netlify
2. Publish directory: `.`
3. Build command: `python3 tools/pages.py` (or leave blank, the HTML is committed)

**Any static host** works too. Upload the repository root. The site has no server side dependencies.

---

## SEO priorities after launch

Ranked by impact for a mobile service business in this market.

**Do first**

1. **Google Business Profile.** For a service area business, set the service area rather than a
   street address. Add categories (Caterer, Shaved Ice Shop, Party Equipment Rental Service),
   upload the real event photos, and post regularly. For a business with no map presence yet, this
   outranks everything else on this list.
2. **Get reviews.** As of this build there is no indexed review content for Kreme Cruiser anywhere
   on the open web. Ask every school coordinator and party host for a Google review the day after
   the event, while they are still happy. Ten real reviews changes local ranking more than any
   amount of on page work.
3. **Google Search Console and Bing Webmaster Tools.** Verify the domain and submit
   `sitemap.xml`.
4. **NAP consistency.** Use the exact same business name, phone and service area on the site,
   Google, Facebook, Instagram and every directory. Inconsistent phone numbers actively hurt local
   ranking.

**Do next**

5. **City landing pages.** Once the service area is confirmed, add a page per priority city
   (Pearland, Manvel, Rosharon, Iowa Colony). Each needs genuinely different content: local venues
   served, neighborhood names, a real event from that city. Do not clone one page and swap the
   city name, that produces thin duplicate pages that rank for nothing.
6. **Citations.** Yelp, Nextdoor, Thumbtack, GigSalad, EventVesta and local Houston party vendor
   directories. Parents booking a cart search these.
7. **Real testimonials.** Once reviews exist, add a testimonial section to the home page and the
   school page with the reviewer's first name and event type. Use only real quotes.
8. **Seasonal content.** A short post each spring on booking field day, and each May on summer camp
   weeks, aligned with when coordinators actually plan.

**Later**

9. Pricing page or starting price. Hosts filter vendors by price. Publishing a starting number cuts
   unqualified inquiries and improves conversion rate on the ones that remain.
10. Add `AggregateRating` schema once real reviews exist. Do not add it before then.
11. Analytics. GA4 plus a conversion event on `thank-you.html`.

---

## Business facts used on the site

Taken from the owner's own materials, not invented:

| Fact | Source |
|------|--------|
| Phone (713) 530-6835, info@kremecruiser.com | business flyer |
| 17 water ice flavors | catering inquiry form |
| Small cup $6, large cup $9 | catering inquiry form |
| 50% non-refundable retainer secures a date | catering inquiry form |
| Event types offered | business flyer |

The inquiry form at `contact.html` mirrors the field set of the business's
Jotform catering inquiry, so submissions arrive with the same information.
The Service style and Event type dropdowns use the business's own options.
Where the flyer and the inquiry form disagreed on flavors, the inquiry form
is authoritative: it is the list the business actually books from, so
Blueberry and Cherry from the flyer are deliberately not on the site.

### Asset caching

Every `assets/` URL in the HTML is written with a `?v=` content hash by
`tools/build.py`. This matters: Netlify serves images with a one year
immutable cache, so a stable filename would pin visitors to whatever copy
their browser downloaded first. That is what happened twice during the
build, once with an old stylesheet and once with an old logo. Do not remove
the stamping, and do not hand-write asset URLs into the HTML.

### Logo and icons

The header logo, favicons, touch icon and social share image are all
generated from `assets/img/logo-source.png`, which is the real logo with its
background removed. To change the artwork, replace that file and run:

    python3 tools/make_logo.py

## Research notes

Public web research done while building this site turned up almost nothing:

- No Google Business Profile, Yelp listing, Tripadvisor listing or any indexed review found
- No existing website found
- An Instagram account exists at `@kreme_cruiser`, referenced in the site config
- One Facebook community group post referencing "Kreme Cruiser offers mobile water-ice treats for
  events" was found in search results but could not be opened

All content on this site was written from the business photos supplied by the owner: the cart, the
flavor menu board, the branded staff shirts and the event settings. **Nothing about pricing, hours,
years in business, licensing or customer reviews was invented.** Anywhere a real detail is missing,
the site either asks the visitor to get in touch or hides the element entirely.

Verify the service area list and the operational claims (setup time, space required, allergy
information) against how the business actually runs before going live.
