#!/usr/bin/env python3
"""Page content for the Kreme Cruiser site. Run this file to build the site."""

from build import build, AREAS, SITE_URL  # noqa: E402

CTA = """  <section class="section">
    <div class="wrap">
      <div class="callout">
        <h2>{heading}</h2>
        <p>{copy}</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="contact.html">Check Your Date</a>
          <a class="btn btn-ghost" href="flavors.html">See the Flavors</a>
        </div>
      </div>
    </div>
  </section>"""


def cta(heading, copy):
    return CTA.format(heading=heading, copy=copy)


def picture(name, alt, widths=(600, 1000, 1179), sizes="(max-width: 860px) 90vw, 520px",
            cls="", loading="lazy"):
    srcset = ", ".join(f"assets/img/{name}-{w}.jpg {w}w" for w in widths)
    cl = f' class="{cls}"' if cls else ""
    return (f'<img{cl} src="assets/img/{name}-{widths[-1]}.jpg" srcset="{srcset}" '
            f'sizes="{sizes}" alt="{alt}" loading="{loading}" decoding="async">')


FLAVORS = [
    ("Pineapple", "#f5c518", "Sweet and tangy"),
    ("Strawberry", "#e63950", "The classic red"),
    ("Mango", "#f79021", "Sweet tropical mango"),
    ("Strawberry Lemonade", "#f2547d", "Strawberry with a squeeze of lemon"),
    ("Peach", "#f8a06a", "Soft and summery"),
    ("Fruit Punch", "#d6294e", "Mixed fruit, always a kid favorite"),
    ("Blue Razz", "#1a7ee0", "Sweet, tart and it turns your tongue blue"),
    ("Rainbow", "linear-gradient(135deg,#e2273f 0%,#ffc629 35%,#3cba54 65%,#1a7ee0 100%)",
     "Layered colors in one cup, the most requested flavor"),
    ("Watermelon", "linear-gradient(135deg,#ef5b6b 60%,#5cb832 60%)", "Cool and refreshing"),
    ("Passion Fruit", "#f2a93b", "Bright and tangy"),
    ("Lemon", "#f5e04a", "Sharp and clean"),
    ("Orange Creamsicle", "#f79a3c", "Creamy orange, no dairy"),
    ("Sour Apple", "#5cb832", "Green apple with a pucker at the end"),
    ("Cotton Candy", "linear-gradient(135deg,#f49ac8 50%,#7cc9ec 50%)", "Tastes like the fair"),
    ("Pi&ntilde;a Colada", "#f6e7c4", "Pineapple and coconut, no alcohol"),
    ("Black Cherry", "#8b1533", "Deeper and richer than regular cherry"),
    ("Pistachio", "#a8c86a", "Nutty and different, for the grown ups"),
]

FLAVOR_NAMES = [n.replace("&ntilde;", "n") for n, _, _ in FLAVORS]


def flavor_list(items):
    out = []
    for name, color, note in items:
        style = f"background:{color};" if color.startswith("#") else f"background:{color};"
        out.append(
            f'<li><span class="dot" style="{style}" aria-hidden="true"></span>'
            f'<span>{name}<small>{note}</small></span></li>'
        )
    return '<ul class="flavor-list">' + "".join(out) + "</ul>"


# ----------------------------------------------------------------- HOME
home_body = f"""  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <span class="eyebrow">Mobile water ice &middot; South Houston area</span>
        <h1>The water ice cart that <span class="accent">comes to you</span></h1>
        <p class="hero-lede">Kreme Cruiser is a pedal powered water ice cart. We roll up to schools, daycares, birthday parties, church events and neighborhood block parties, set up in a few minutes and start handing out cups.</p>
        <ul class="hero-points">
          <li>Seventeen water ice flavors, every one of them dairy free</li>
          <li>Fits indoors or outdoors, no generator noise and no fumes</li>
          <li>Friendly servers in uniform who keep the line moving</li>
          <li>We bring the cart, cups, spoons, napkins and cleanup</li>
        </ul>
        <div class="btn-row">
          <a class="btn btn-primary" href="contact.html">Check Your Date</a>
          <a class="btn btn-ghost" href="flavors.html">See the Flavor Menu</a>
        </div>
      </div>
      <div class="hero-photo">
        {picture("cart-menu-board", "The Kreme Cruiser water ice cart set up on a school lawn under a teal umbrella next to its flavor menu board", sizes="(max-width: 860px) 90vw, 500px", loading="eager")}
      </div>
    </div>
  </section>


  <section class="trust-bar">
    <div class="wrap">
      <ul>
        <li><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 4 6v6c0 5 3.4 9.4 8 10 4.6-.6 8-5 8-10V6Z"/><path d="m9 12 2 2 4-4"/></svg>
          <div><b>Seventeen flavors</b><span>Every one dairy free, no alcohol</span></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 1v22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          <div><b>$6 small, $9 large</b><span>Cup pricing published up front</span></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="5.5" cy="18" r="3"/><circle cx="18.5" cy="18" r="3"/><path d="M8.5 18h7"/><path d="M6 18 9 8h8l2 10"/><path d="M8 8h10"/></svg>
          <div><b>Indoors or outdoors</b><span>Pedal powered, no generator</span></div></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          <div><b>Staffed service</b><span>Uniformed servers run the line</span></div></li>
      </ul>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="section-head center">
        <span class="eyebrow">What we do</span>
        <h2>Pick the kind of event you are planning</h2>
        <p class="lede">Same cart, same flavors. What changes is the serving plan, the timing and how we handle the line.</p>
      </div>
      <div class="grid grid-3">
        <a class="card card-link" href="schools-and-daycares.html">
          <span class="icon-badge" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/></svg></span>
          <h3>Schools &amp; Daycares</h3>
          <p>Field days, reward days, graduations, summer camp weeks and teacher appreciation. We serve classroom by classroom so nobody stands around waiting.</p>
          <span class="more">See how school days work</span>
        </a>
        <a class="card card-link" href="birthday-parties.html">
          <span class="icon-badge" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 16h16v5H4z"/><path d="M4 16c0-3 2-4 4-4s4 1 4 4c0-3 2-4 4-4s4 1 4 4"/><path d="M12 8v4M12 3v2"/></svg></span>
          <h3>Birthday Parties</h3>
          <p>Backyards, driveways, parks and clubhouses. The cart is the photo backdrop and the dessert table in one, and there is no melted mess on the floor.</p>
          <span class="more">Plan a birthday</span>
        </a>
        <a class="card card-link" href="community-and-corporate-events.html">
          <span class="icon-badge" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
          <h3>Community &amp; Corporate</h3>
          <p>Church events, nonprofit fundraisers, HOA gatherings, grand openings and staff appreciation days. We can serve a set count or run open service for a window of time.</p>
          <span class="more">See event options</span>
        </a>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="split">
        <div>
          <span class="eyebrow">The flavors</span>
          <h2>Seventeen flavors, all dairy free</h2>
          <p>Handcrafted water ice, shaved fine so the flavor holds all the way through the cup instead of running out the bottom like a syrup soaked cone. Rainbow is the one most kids point at first.</p>
          <p>Pi&ntilde;a Colada and Orange Creamsicle taste creamy, but there is no dairy and no alcohol anywhere on the cart. Cups are $6 small and $9 large.</p>
          <div class="btn-row mt-32">
            <a class="btn btn-secondary" href="flavors.html">See the full menu</a>
          </div>
        </div>
        <div>{picture("rainbow-shaved-ice", "A cup of rainbow water ice with red, yellow, green and blue layers on the Kreme Cruiser cart", sizes="(max-width: 860px) 90vw, 500px")}</div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head center">
        <span class="eyebrow">How it works</span>
        <h2>Four steps from first message to last cup</h2>
      </div>
      <div class="grid grid-4">
        <div class="card step"><div class="step-num">1</div><h3>Tell us the date</h3><p>Send the date, the address, roughly how many people and what time you want service to start.</p></div>
        <div class="card step"><div class="step-num">2</div><h3>Get your quote</h3><p>We confirm availability and send pricing for your headcount and service window. No guessing games.</p></div>
        <div class="card step"><div class="step-num">3</div><h3>We set up</h3><p>The cart, the umbrella and the menu board go up in about fifteen minutes. We only need a flat spot to park.</p></div>
        <div class="card step"><div class="step-num">4</div><h3>Everybody eats</h3><p>Servers keep the line moving, then we pack out and leave the space the way we found it.</p></div>
      </div>
    </div>
  </section>

  <section class="section section-teal">
    <div class="wrap">
      <div class="section-head center">
        <span class="eyebrow">Out on the route</span>
        <h2>Where the cart has been parked</h2>
        <p class="lede">Summer camps, school lawns, indoor party halls and community fundraisers. Indoors or outdoors, the setup is the same.</p>
      </div>
      <div class="photo-strip">
        <figure>{picture("daycare-shaved-ice-party", "Children seated around a table at a daycare eating cups of water ice", widths=(600, 1000), sizes="(max-width: 860px) 45vw, 260px")}<figcaption>Summer camp treat day</figcaption></figure>
        <figure>{picture("kreme-cruiser-team-event", "Two Kreme Cruiser servers in matching shirts holding cups of water ice in front of the cart at an indoor event", widths=(600, 1000), sizes="(max-width: 860px) 45vw, 260px")}<figcaption>Indoor community event</figcaption></figure>
        <figure>{picture("kids-school-event", "Two boys holding cups of water ice in front of the Kreme Cruiser cart at a school event", widths=(600, 725), sizes="(max-width: 860px) 45vw, 260px")}<figcaption>School celebration</figcaption></figure>
        <figure>{picture("cart-neighborhood-ride", "The Kreme Cruiser cart being pedaled down a residential street", widths=(546,), sizes="(max-width: 860px) 45vw, 260px")}<figcaption>Rolling into the neighborhood</figcaption></figure>
      </div>
      <div class="btn-row mt-32" style="justify-content:center;">
        <a class="btn btn-secondary" href="gallery.html">See more photos</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>{picture("kreme-cruiser-team-event", "Kreme Cruiser servers in branded shirts serving water ice at an indoor event", sizes="(max-width: 860px) 90vw, 500px")}</div>
        <div>
          <span class="eyebrow">Why the cart works</span>
          <h2>Built for places a food truck cannot go</h2>
          <p>A trailer needs a driveway, a turning radius and somewhere to idle. The Kreme Cruiser is a trike. It fits through a gate, rolls onto a gym floor, parks on a lawn and sits under a shade umbrella without blocking anything.</p>
          <p>That matters most at schools and daycares, where the serving spot is usually a courtyard, a cafeteria or a patch of grass behind a fence. It also means no engine running next to a group of kids.</p>
          <div class="btn-row mt-32">
            <a class="btn btn-primary" href="contact.html">Ask about your space</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="section-head center">
        <span class="eyebrow">Who books the cart</span>
        <h2>The places we show up</h2>
        <p class="lede">Every one of these is a booking we actually work, not a list of things we could imagine doing.</p>
      </div>
      <ul class="venues">
        <li>Elementary schools</li><li>Daycares</li><li>Summer camps</li>
        <li>Birthday parties</li><li>Churches</li><li>Nonprofit events</li>
        <li>HOA and neighborhood nights</li><li>Corporate appreciation days</li>
        <li>Community festivals</li><li>Grand openings</li>
      </ul>
      <div class="center" style="margin-top:34px;">
        <h3>Follow the cart</h3>
        <p class="lede" style="max-width:44em;margin:0 auto;">See where the Kreme Cruiser is parked this week, and what the cups look like before you book.</p>
        <div class="social-row">
          <a class="social-btn" data-contact="instagram" href="#" rel="noopener" data-contact-item hidden>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>
            Instagram
          </a>
          <a class="social-btn" data-contact="facebook" href="#" rel="noopener" data-contact-item hidden>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3Z"/></svg>
            Facebook
          </a>
        </div>
      </div>
    </div>
  </section>

{cta("Ready to get the cart on your calendar?", "Send your date, location and headcount. We will confirm whether the cart is open and send you a quote.")}
"""

# ----------------------------------------------------------------- SERVICES
services_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Services</span>
      <h1>Mobile water ice catering for events of any size</h1>
      <p class="lede">One cart, one flavor menu, three ways to run it. Pick the setup that matches your crowd and we will handle the rest.</p>
      <div class="btn-row mt-32"><a class="btn btn-primary" href="contact.html">Check Your Date</a></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="grid grid-3">
        <a class="card card-link" href="schools-and-daycares.html">
          <h3>Schools &amp; Daycares</h3>
          <p>Field day, reward day, graduation, teacher appreciation, summer camp weeks and PTO events. We serve in class rotations so recess and nap schedules stay intact.</p>
          <span class="more">School and daycare details</span>
        </a>
        <a class="card card-link" href="birthday-parties.html">
          <h3>Birthday Parties</h3>
          <p>Backyard, park pavilion, clubhouse or driveway. Usually one to two hours of service, and the cart doubles as the dessert table.</p>
          <span class="more">Birthday party details</span>
        </a>
        <a class="card card-link" href="community-and-corporate-events.html">
          <h3>Community &amp; Corporate</h3>
          <p>Church events, nonprofit fundraisers, HOA nights, grand openings, staff appreciation and vendor markets. Open service or a fixed cup count.</p>
          <span class="more">Community event details</span>
        </a>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">What comes with the cart</span>
        <h2>Everything on this list is included</h2>
      </div>
      <div class="grid grid-2">
        <div class="card">
          <h3>We bring</h3>
          <ul>
            <li>The water ice cart, shade umbrella and A frame flavor menu</li>
            <li>Ice and your selected flavors from the full menu of seventeen</li>
            <li>Cups, spoons and napkins</li>
            <li>Uniformed servers to run the line</li>
            <li>Hand sanitizer and a trash plan for our own service area</li>
            <li>Full cleanup of the serving spot</li>
          </ul>
        </div>
        <div class="card">
          <h3>You provide</h3>
          <ul>
            <li>A flat spot roughly 10 feet by 10 feet to park and serve</li>
            <li>Access wide enough to roll a trike through, about 3 feet</li>
            <li>Somewhere shaded or indoors if the forecast is rough</li>
            <li>A rough headcount ahead of time so we bring enough</li>
            <li>A contact person who will be on site when we arrive</li>
          </ul>
        </div>
      </div>
      <div class="note mt-32">
        <p class="mb-0"><strong>No power needed at most events.</strong> The cart does not run on a generator, so there is no cord across a walkway and no engine noise next to a group of kids. Tell us your setup when you book and we will confirm what your spot needs.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Service styles</span>
        <h2>Three ways to serve the same cart</h2>
      </div>
      <div class="table-wrap">
        <table>
          <caption class="visually-hidden">Comparison of Kreme Cruiser service styles</caption>
          <thead><tr><th scope="col">Style</th><th scope="col">Best for</th><th scope="col">How it runs</th></tr></thead>
          <tbody>
            <tr><td><strong>Set cup count</strong></td><td>Schools, daycares, private parties</td><td>You tell us the headcount. We serve until every guest has had one cup, then close out.</td></tr>
            <tr><td><strong>Timed service</strong></td><td>Festivals, church events, grand openings</td><td>We serve continuously for an agreed window, usually one to three hours.</td></tr>
            <tr><td><strong>Rotation service</strong></td><td>Large schools and camps</td><td>Groups come to the cart in waves so no class is standing in line for long.</td></tr>
          </tbody>
        </table>
      </div>
      <p class="mt-32">Not sure which one fits? Tell us the headcount and the time you have available and we will tell you which style keeps the line shortest.</p>
    </div>
  </section>

{cta("Tell us about your event", "Send the date, the address, the headcount and the time you want service to start. We will come back with availability and a quote.")}
"""

# ----------------------------------------------------------------- SCHOOLS
schools_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Schools &amp; Daycares</span>
      <h1>Water ice for schools, daycares and summer camps</h1>
      <p class="lede">Field day, reward day, graduation, teacher appreciation and camp weeks. We serve fast, we serve clean and we work around your schedule instead of running over it.</p>
      <div class="btn-row mt-32"><a class="btn btn-primary" href="contact.html?event=School%20or%20daycare">Check Your Date</a></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Built for a bell schedule</h2>
          <p>Most school events fail on timing, not on food. A class gets pulled out, the line backs up and the next group loses half its window. We plan around that.</p>
          <p>Before your event we agree on how many groups are coming, how long each group has and where they line up. Then we run rotations. Servers pre-portion cups during the gaps so the next class walks up to a cart that is already ready.</p>
          <p>Cups are handed out one at a time with a spoon and a napkin. Nothing needs to be plugged in, nothing needs to be carried through a hallway, and nothing gets left behind on the floor.</p>
        </div>
        <div>{picture("kids-lined-up-at-cart", "Children lined up at the Kreme Cruiser cart at a school while a server hands out a cup", widths=(541,), sizes="(max-width: 860px) 90vw, 500px")}</div>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="section-head"><h2>Events we handle most</h2></div>
      <div class="grid grid-3">
        <div class="card"><h3>Field day</h3><p>A cold cup at the end of a hot morning. We park at the finish line and serve as groups rotate off the field.</p></div>
        <div class="card"><h3>Reward and incentive days</h3><p>Attendance goals, reading goals, behavior charts. We serve only the qualifying list if you want it that way.</p></div>
        <div class="card"><h3>Graduation and promotion</h3><p>Pre K, kindergarten and fifth grade ceremonies. Serve after the walk while families are still on site.</p></div>
        <div class="card"><h3>Summer camp weeks</h3><p>Weekly themed days at daycares and camps. Book a recurring slot for the season.</p></div>
        <div class="card"><h3>Teacher appreciation</h3><p>Staff lounge or courtyard service during planning periods and lunch.</p></div>
        <div class="card"><h3>PTO and family nights</h3><p>Open house, fall festival, spring carnival. Timed service while families walk the campus.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow">
      <h2>What administrators usually want to know</h2>
      <div class="faq mt-32">
        <details><summary>Can you serve indoors?</summary><div><p>Yes. The cart is a trike, not a trailer. It fits through a standard double door and rolls onto a gym floor, a cafeteria or a multipurpose room. We have served indoor events with the cart parked inside the room.</p></div></details>
        <details><summary>How long does it take to serve a full campus?</summary><div><p>It depends on headcount and how many groups you send at once. Tell us your total number and the window you have, and we will tell you honestly whether one cart can cover it or whether you need a longer window.</p></div></details>
        <details><summary>Are the flavors allergy friendly?</summary><div><p>All flavors are dairy free and the cart does not carry nuts. Pi&ntilde;a Colada and Orange Creamsicle taste creamy but contain no dairy and no alcohol. If you have a student with a specific allergy, send us the details before the event and we will tell you exactly what is in the flavor.</p></div></details>
        <details><summary>Do you need power or water?</summary><div><p>Not at most events. We do not run a generator. Tell us your serving spot when you book and we will confirm what, if anything, we need from you.</p></div></details>
        <details><summary>Can we get an invoice or a W-9?</summary><div><p>Yes. Send your district or center billing requirements with your booking request and we will get you what your business office needs.</p></div></details>
      </div>
    </div>
  </section>

{cta("Put the cart on your school calendar", "Send your event date, campus address, approximate headcount and the time window you have. We will confirm availability and send pricing.")}
"""

# ----------------------------------------------------------------- BIRTHDAYS
birthday_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Birthday Parties</span>
      <h1>Water ice cart rental for birthday parties</h1>
      <p class="lede">The cart rolls into the backyard, the driveway, the park pavilion or the clubhouse. Kids line up, pick a flavor, and you are not the one scooping.</p>
      <div class="btn-row mt-32"><a class="btn btn-primary" href="contact.html?event=Birthday%20party">Check Your Date</a></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>{picture("guests-ordering-at-cart", "Guests standing at the Kreme Cruiser cart under its umbrella at an outdoor party", widths=(547,), sizes="(max-width: 860px) 90vw, 500px")}</div>
        <div>
          <h2>It is the dessert and the decor</h2>
          <p>The cart is bright teal with the umbrella up and the flavor board out front. Parents take photos of it before the first cup is served. You do not need a separate dessert table, a cooler of popsicles or a backup plan for melted ice cream.</p>
          <p>Service usually runs one to two hours. We arrive early, set up, serve your guest list, then pack out and take our trash with us.</p>
          <ul class="hero-points mt-32">
            <li>Kids pick their own flavor, which is half the fun</li>
            <li>Nothing drips onto furniture the way ice cream does</li>
            <li>Adults order too, and they usually do</li>
            <li>No power cord running across the yard</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="section-head center"><h2>Party spots that work</h2><p class="lede">If a bicycle can get there, the cart can get there.</p></div>
      <div class="grid grid-4">
        <div class="card"><h3>Backyards</h3><p>Through a standard gate, onto grass or a patio. Shade umbrella included.</p></div>
        <div class="card"><h3>Driveways</h3><p>Great for block parties and for keeping the mess outside the house.</p></div>
        <div class="card"><h3>Park pavilions</h3><p>We park under the roof or beside it. Check your park permit rules first.</p></div>
        <div class="card"><h3>Clubhouses</h3><p>Indoor service on tile or wood floors, same as any indoor event.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow">
      <h2>Booking a birthday</h2>
      <ol>
        <li><strong>Send the date early.</strong> Spring and summer Saturdays fill up first. If your date is flexible, tell us and we will offer what is open.</li>
        <li><strong>Give us a headcount.</strong> Count adults too. Grown ups order more often than people expect.</li>
        <li><strong>Tell us the serving spot.</strong> Backyard, driveway, park or indoors, and whether there are steps or a narrow gate.</li>
        <li><strong>Pick a start time.</strong> Most hosts start service about thirty minutes after guests arrive, so the line does not form during hellos.</li>
      </ol>
      <p class="mt-32">We will confirm availability and send a quote based on your headcount and service window.</p>
    </div>
  </section>

{cta("Book the cart for the party", "Send the date, the address, the headcount and your start time. We will tell you right away whether the cart is open.")}
"""

# ----------------------------------------------------------------- COMMUNITY
community_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Community &amp; Corporate</span>
      <h1>Water ice for community events, churches and company days</h1>
      <p class="lede">Fundraisers, church events, HOA nights, grand openings, vendor markets and staff appreciation. We can serve a set cup count or run open service for a fixed window.</p>
      <div class="btn-row mt-32"><a class="btn btn-primary" href="contact.html?event=Community%20or%20corporate">Check Your Date</a></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Two ways to run a public event</h2>
          <p><strong>Sponsored service.</strong> The host pays for a set number of cups and guests get them at no charge. This is the usual setup for church events, nonprofit gatherings, HOA nights and employee appreciation. You know your cost before the event starts.</p>
          <p><strong>Timed open service.</strong> We serve continuously for an agreed window. Good for festivals and grand openings where you cannot predict the count but you can predict the hours.</p>
          <p>Either way we bring the cart, the umbrella, the menu board and the servers. You get a bright, photographable setup that draws people toward whatever you are actually promoting.</p>
        </div>
        <div>{picture("serving-community-event", "A Kreme Cruiser server scooping water ice for families at an outdoor community event", widths=(600,722), sizes="(max-width: 860px) 90vw, 500px")}</div>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="section-head"><h2>Events we work</h2></div>
      <div class="grid grid-3">
        <div class="card"><h3>Church and ministry events</h3><p>Vacation Bible school, family nights, outreach days and youth events, indoors or on the lawn.</p></div>
        <div class="card"><h3>Nonprofit fundraisers</h3><p>Awareness walks, donor days and community drives. We have served alongside kids nonprofits at their own events.</p></div>
        <div class="card"><h3>HOA and neighborhood</h3><p>Pool openings, national night out, movie nights and block parties inside the subdivision.</p></div>
        <div class="card"><h3>Grand openings</h3><p>A free cup outside your door is a better draw than a sign. We serve for your window and pack out.</p></div>
        <div class="card"><h3>Staff appreciation</h3><p>Warehouse breakrooms, office parking lots and shift changes. We can serve across two shifts.</p></div>
        <div class="card"><h3>Vendor markets</h3><p>Farmers markets and pop up markets where a compact footprint matters more than a big trailer.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow">
      <h2>What to send when you request a quote</h2>
      <ul>
        <li>Date and rain date if you have one</li>
        <li>Address and where exactly the cart will park</li>
        <li>Expected attendance, and whether all of them will want a cup</li>
        <li>Service window, including whether you want a break in the middle</li>
        <li>Whether you want sponsored cups or timed open service</li>
        <li>Any insurance, permit or vendor paperwork your venue requires</li>
      </ul>
      <p class="mt-32">The more of this you send up front, the faster we can get you a real number instead of a range.</p>
    </div>
  </section>

{cta("Get a quote for your event", "Send your date, location, attendance and service window and we will come back with availability and pricing.")}
"""

# ----------------------------------------------------------------- FLAVORS
flavor_schema = """{
  "@context": "https://schema.org",
  "@type": "Menu",
  "name": "Kreme Cruiser Flavor Menu",
  "url": "%s/flavors.html",
  "hasMenuSection": [
    {"@type":"MenuSection","name":"Water Ice Flavors","hasMenuItem":[%s]}
  ]
}""" % (
    SITE_URL,
    ",".join('{"@type":"MenuItem","name":"%s"}' % n for n in FLAVOR_NAMES),
)

flavors_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Flavor Menu</span>
      <h1>Kreme Cruiser flavors</h1>
      <p class="lede">Seventeen flavors of handcrafted water ice, all shaved fresh at the cart. Everything on the menu is dairy free.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="flavor-cols">
        <div>{flavor_list(FLAVORS[:9])}</div>
        <div>{flavor_list(FLAVORS[9:])}</div>
      </div>
      <div class="note mt-32">
        <p class="mb-0"><strong>How many flavors come with your event?</strong> That depends on the package you book. Extra flavors beyond your package can be added for a small charge. Tell us which ones your guests want when you send your inquiry.</p>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="split">
        <div>{picture("sour-apple-orange-shaved-ice", "A cup of orange and green water ice on the Kreme Cruiser cart", sizes="(max-width: 860px) 90vw, 500px")}</div>
        <div>
          <h2>Water ice, not a snow cone</h2>
          <p>A snow cone is crushed ice with syrup poured on top, which is why it runs out the bottom of the cone in about four minutes. Ours is shaved fine and the flavor goes all the way through, so it still tastes like the flavor your guest picked when they get back to their table.</p>
          <h3 class="mt-32">Common questions about the flavors</h3>
          <ul>
            <li><strong>Dairy:</strong> none in any flavor, including Pi&ntilde;a Colada and Orange Creamsicle.</li>
            <li><strong>Alcohol:</strong> none. Pi&ntilde;a Colada is the flavor, not the drink.</li>
            <li><strong>Cup sizes:</strong> small cups are $6 and large cups are $9.</li>
            <li><strong>Mixing:</strong> ask your server to combine two flavors in one cup.</li>
          </ul>
          <p>If you have a specific allergy question, send it with your inquiry and we will give you a straight answer before you commit.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow center">
      <h2>The menu board that travels with the cart</h2>
      <p class="lede">Guests read this at the event, so nobody has to ask what is available.</p>
      <img src="assets/img/flavor-menu-sign-440.jpg" alt="The Kreme Cruiser A frame menu board listing the water ice flavors" loading="lazy" decoding="async" style="border-radius:16px;box-shadow:var(--shadow-lg);margin:32px auto 0;max-width:420px;">
    </div>
  </section>

{cta("Pick your flavors at the cart", "Book the Kreme Cruiser for your event and let your guests choose. Send us your date to get started.")}
"""

# ----------------------------------------------------------------- AREA
area_chips = "".join(f"<li>{a}, TX</li>" for a in AREAS)
area_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Service Area</span>
      <h1>Where the Kreme Cruiser travels</h1>
      <p class="lede">We are based in the south Houston area and serve the communities below. If your event is just outside this list, ask anyway. We travel for the right date.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Cities and communities we serve</h2>
      <ul class="area-list mt-32">{area_chips}</ul>
      <p class="mt-32">Plus the neighborhoods in between, including Lakes of Savannah, Savannah Lakes, Southern Trails, Shadow Creek Ranch, Silverlake, Pomona and Meridiana.</p>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="grid grid-2">
        <div class="card">
          <h3>Booking outside the area</h3>
          <p>We do take events beyond the list. Travel outside the core service area may add a fee depending on distance and the time of day. Send your address with your request and we will tell you up front whether travel applies and what it costs. No surprises on the invoice.</p>
        </div>
        <div class="card">
          <h3>Recurring stops</h3>
          <p>Daycares, camps and after school programs can book a recurring slot for a season instead of one date at a time. If you want the cart on the same day every week during summer, say so in your first message and we will hold the slot.</p>
        </div>
      </div>
    </div>
  </section>

{cta("Not sure if we come to you?", "Send your address with your date. We will confirm whether it is inside the service area and what travel looks like if it is not.")}
"""

# ----------------------------------------------------------------- ABOUT
about_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">About</span>
      <h1>About Kreme Cruiser</h1>
      <p class="lede">A locally owned water ice cart serving the south Houston area. Small setup, real service, and a flavor board kids can read from across the yard.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Why a cart instead of a truck</h2>
          <p>Most of the events people wanted us at were not truck friendly. A daycare courtyard behind a locked gate. A gym floor. A backyard with a three foot side gate. A church fellowship hall. A truck cannot get into any of those, and a trailer parked at the curb means somebody has to walk a hundred kids out to the street and back.</p>
          <p>The cart solves that. It rolls where the people already are, sets up in about fifteen minutes and does not need a generator running next to a group of children.</p>
          <h2 class="mt-32">How we work an event</h2>
          <p>We show up early enough to be ready before your start time. Servers wear branded shirts so guests know who to walk up to. We keep the serving area clean while we work, and when service ends we pack out and take our own trash with us.</p>
          <p>If you tell us a headcount, we bring enough for that headcount. If you tell us a time window, we hold that window. That is most of what event hosts actually want from a vendor.</p>
        </div>
        <div>{picture("kreme-cruiser-team-event", "Kreme Cruiser servers in matching branded shirts standing in front of the water ice cart", sizes="(max-width: 860px) 90vw, 500px")}</div>
      </div>
    </div>
  </section>

  <section class="section section-shell">
    <div class="wrap">
      <div class="section-head center"><h2>What we care about</h2></div>
      <div class="grid grid-3">
        <div class="card"><h3>Showing up on time</h3><p>Set up finishes before your start time, not after it. Late vendors ruin schedules that other people planned around.</p></div>
        <div class="card"><h3>Keeping the line moving</h3><p>Nobody remembers a great flavor if they waited twenty five minutes for it. We pre portion during gaps and staff to the headcount.</p></div>
        <div class="card"><h3>Leaving it clean</h3><p>We clean our serving area and haul our trash. Your custodian, your host or your homeowner should not be finding cups an hour later.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow">
      <h2>Community events</h2>
      <p>We work alongside local nonprofits and community organizations at their events, including children focused nonprofit gatherings in the area. If you run a community organization and want to talk about a partnership or a sponsored serving, reach out and tell us what you are planning.</p>
      <div class="btn-row mt-32"><a class="btn btn-secondary" href="contact.html">Start a conversation</a></div>
    </div>
  </section>

{cta("Bring the cart to your next event", "Send your date, location and headcount and we will get back to you with availability.")}
"""

# ----------------------------------------------------------------- GALLERY
gallery_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Gallery</span>
      <h1>The cart, the flavors and the events</h1>
      <p class="lede">Real photos from real stops. Schools, camps, neighborhoods, indoor halls and community events.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="gallery-grid">
        <figure>
          {picture("cart-menu-board", "The Kreme Cruiser cart parked on grass outside a school with its teal umbrella up and the flavor menu board beside it", sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>The full setup: cart, shade umbrella and A frame flavor board. This is a school field day.</figcaption>
        </figure>
        <figure>
          {picture("cart-neighborhood-ride", "A Kreme Cruiser rider pedaling the cart with its teal umbrella down a residential street", widths=(546,), sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>It really does pedal. The cart rides into the neighborhood under its own power.</figcaption>
        </figure>
        <figure>
          {picture("kids-lined-up-at-cart", "A line of children waiting at the Kreme Cruiser cart outside a building while a server hands out a cup", widths=(541,), sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>A line moves fast when servers portion cups between groups.</figcaption>
        </figure>
        <figure>
          {picture("kids-school-event", "Two boys holding cups of water ice in front of the Kreme Cruiser cart at an outdoor school event", widths=(600,725), sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>School celebration. The cart sits alongside the other stalls without needing power.</figcaption>
        </figure>
        <figure>
          {picture("serving-community-event", "A Kreme Cruiser server scooping water ice for families waiting at an outdoor community event", widths=(600,722), sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>Community event service, with families lined up along the lot.</figcaption>
        </figure>
        <figure>
          {picture("guests-ordering-at-cart", "Two guests standing at the Kreme Cruiser cart under its umbrella at an outdoor event", widths=(547,), sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>Adults order as often as the kids do.</figcaption>
        </figure>
        <figure>
          {picture("daycare-shaved-ice-party", "Children seated around a table indoors at a daycare eating cups of water ice", sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>Camp week at a daycare. Cups are handed out at the table so the room stays calm.</figcaption>
        </figure>
        <figure>
          {picture("kreme-cruiser-team-event", "Two Kreme Cruiser servers in branded shirts holding cups in front of the cart at an indoor event", sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>Indoor community event. The cart rolls straight into the hall.</figcaption>
        </figure>
        <figure>
          {picture("rainbow-shaved-ice", "A cup of rainbow water ice layered in red, yellow, green and blue", sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>The Rainbow. The most requested cup at nearly every kids event we work.</figcaption>
        </figure>
        <figure>
          {picture("sour-apple-orange-shaved-ice", "A cup of orange and green water ice resting on the Kreme Cruiser cart", sizes="(max-width: 560px) 90vw, (max-width: 900px) 45vw, 340px")}
          <figcaption>Two flavors in one cup. Just ask your server.</figcaption>
        </figure>
      </div>
    </div>
  </section>

{cta("Want photos like these from your event?", "Book the cart and we will bring the whole setup, umbrella and menu board included.")}
"""

# ----------------------------------------------------------------- FAQ
FAQ_ITEMS = [
    ("What is Kreme Cruiser?",
     "Kreme Cruiser is a mobile water ice cart serving the south Houston area. The cart is a pedal powered trike with a shade umbrella and a flavor menu board. We bring it to schools, daycares, birthday parties, church events and community gatherings."),
    ("How far in advance should I book?",
     "As early as you can, especially for spring and summer Saturdays and for school field days. Those dates fill first. If your date is flexible, tell us and we will show you what is open."),
    ("What areas do you serve?",
     "Pearland, Manvel, Rosharon, Iowa Colony, Alvin, Friendswood, Fresno, Missouri City, Sienna, Arcola, League City, South Houston and the neighborhoods in between. Events outside that area may add a travel fee, which we quote up front."),
    ("How many flavors are there?",
     "Seventeen, including Rainbow, Cotton Candy, Blue Razz and Pistachio. The number included with your event depends on the package you book, and extra flavors can be added for a small charge. The full list is on the flavor menu page."),
    ("Is there dairy or alcohol in any flavor?",
     "No. Every flavor on the cart is dairy free, and there is no alcohol in any of them. Pi&ntilde;a Colada and Orange Creamsicle taste creamy but contain neither."),
    ("Can you set up indoors?",
     "Yes. The cart fits through a standard double door and works on gym floors, cafeterias, fellowship halls and clubhouses. Because there is no generator, indoor service is not a problem."),
    ("Do you need electricity or water?",
     "Not at most events. Tell us about your serving spot when you book and we will confirm whether anything is needed from you."),
    ("How much space does the cart need?",
     "Roughly a ten foot by ten foot flat area to park and serve, and about three feet of clearance to roll the cart in. A standard yard gate is wide enough."),
    ("How long does setup take?",
     "About fifteen minutes. We arrive early enough to be fully ready before your service start time."),
    ("What does it cost?",
     "Cups are $6 for a small and $9 for a large. Your event total depends on headcount, service window and location, so send those three things with your date and we will send a real quote rather than a range."),
    ("Can you serve a school with several hundred students?",
     "Often yes, with rotation service and enough time. Tell us your total count and the window you have and we will tell you honestly whether one cart can cover it."),
    ("What happens if it rains?",
     "We talk about it before the event. Most hosts either move service indoors or set a rain date. Let us know at booking which one you plan to use."),
    ("How do I secure my date?",
     "A 50% non-refundable retainer holds your event date. Until that retainer is received the date stays open to other bookings."),
    ("Do you do recurring bookings?",
     "Yes. Daycares, camps and after school programs can hold a recurring slot for a season instead of booking one date at a time."),
    ("Can you provide invoicing or vendor paperwork?",
     "Yes. Send your district, venue or company requirements with your request and we will get you what your business office needs."),
]

faq_schema = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(
    '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
    % (q.replace('"', "'"), a.replace('"', "'").replace("&ntilde;", "n"))
    for q, a in FAQ_ITEMS
) + "]}"

faq_html = "".join(
    f"<details><summary>{q}</summary><div><p>{a}</p></div></details>" for q, a in FAQ_ITEMS
)

faq_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">FAQ</span>
      <h1>Questions about booking the cart</h1>
      <p class="lede">The things hosts ask most often, answered straight. If your question is not here, send it with your booking request.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap narrow">
      <div class="faq">{faq_html}</div>
    </div>
  </section>

{cta("Still have a question?", "Send it along with your event date and we will answer it before you commit to anything.")}
"""

# ----------------------------------------------------------------- CONTACT
EVENT_TYPES = ["School/Campus Event", "Birthday Party/Private Celebration",
               "Corporate/Community Event", "Other"]

SERVICE_STYLES = ["On Site Serving Experience", "Pre-Packaged Drop-Off"]

STATES = ["TX", "Other"]

flavor_boxes = "".join(
    '<label class="check"><input type="checkbox" name="flavors" value="%s"> <span>%s</span></label>' % (n, d)
    for n, d in zip(FLAVOR_NAMES, [f[0] for f in FLAVORS])
)

contact_body = f"""  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Catering Inquiry</span>
      <h1>Kreme Cruiser catering inquiry</h1>
      <p class="lede">Thanks for your interest in Kreme Cruiser. We serve handcrafted water ice at schools, corporate events, parties and community gatherings. Tell us about your event below and we will come back with availability and a custom quote.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split split-form" style="align-items:start;">
        <div>
          <form name="catering-inquiry" method="POST" data-netlify="true" netlify-honeypot="company-website" action="thank-you.html" id="inquiry-form">
            <input type="hidden" name="form-name" value="catering-inquiry">
            <p class="hp"><label>Do not fill this in <input name="company-website" tabindex="-1" autocomplete="off"></label></p>

            <fieldset>
              <legend>Your details</legend>
              <div class="form-grid">
                <div class="field">
                  <label for="first-name">First name <span class="req" aria-hidden="true">*</span></label>
                  <input id="first-name" name="first-name" type="text" autocomplete="given-name" required>
                </div>
                <div class="field">
                  <label for="last-name">Last name <span class="req" aria-hidden="true">*</span></label>
                  <input id="last-name" name="last-name" type="text" autocomplete="family-name" required>
                </div>
                <div class="field">
                  <label for="email">Email <span class="req" aria-hidden="true">*</span></label>
                  <input id="email" name="email" type="email" autocomplete="email" required>
                </div>
                <div class="field">
                  <label for="phone">Phone number <span class="req" aria-hidden="true">*</span></label>
                  <input id="phone" name="phone" type="tel" autocomplete="tel" placeholder="(000) 000-0000" required>
                </div>
              </div>
            </fieldset>

            <fieldset>
              <legend>Event details</legend>
              <div class="form-grid">
                <div class="field">
                  <label for="event-date">Date of event <span class="req" aria-hidden="true">*</span></label>
                  <input id="event-date" name="event-date" type="date" required>
                </div>
                <div class="field">
                  <label for="guests">Total number of guests <span class="req" aria-hidden="true">*</span></label>
                  <input id="guests" name="guests" type="number" min="1" inputmode="numeric" placeholder="Include adults" required>
                </div>
                <div class="field">
                  <label for="start-time">Event start time <span class="req" aria-hidden="true">*</span></label>
                  <input id="start-time" name="start-time" type="time" required>
                </div>
                <div class="field">
                  <label for="end-time">Event end time <span class="req" aria-hidden="true">*</span></label>
                  <input id="end-time" name="end-time" type="time" required>
                </div>
                <div class="field full">
                  <label for="event-type">Event type <span class="req" aria-hidden="true">*</span></label>
                  <select id="event-type" name="event-type" required>
                    <option value="">Please select</option>
                    {"".join(f'<option value="{t}">{t}</option>' for t in EVENT_TYPES)}
                  </select>
                </div>
                <div class="field full">
                  <label for="service-style">Service style <span class="req" aria-hidden="true">*</span></label>
                  <select id="service-style" name="service-style" required>
                    <option value="">Please select</option>
                    {"".join(f'<option value="{t}">{t}</option>' for t in SERVICE_STYLES)}
                  </select>
                  <span class="hint">On-site service includes professional setup. Service upgrades may apply. Final pricing is provided with your custom quote.</span>
                </div>
              </div>

              <fieldset class="choice-set">
                <legend>This event is</legend>
                <div class="choice-row">
                  <label class="check"><input type="radio" name="venue" value="Indoors"> <span>Indoors</span></label>
                  <label class="check"><input type="radio" name="venue" value="Outdoor"> <span>Outdoor</span></label>
                  <label class="check"><input type="radio" name="venue" value="Both"> <span>Both</span></label>
                </div>
              </fieldset>
            </fieldset>

            <fieldset>
              <legend>Address and event location</legend>
              <div class="form-grid">
                <div class="field full">
                  <label for="street">Street address <span class="req" aria-hidden="true">*</span></label>
                  <input id="street" name="street" type="text" autocomplete="address-line1" required>
                </div>
                <div class="field full">
                  <label for="street2">Street address line 2</label>
                  <input id="street2" name="street2" type="text" autocomplete="address-line2">
                </div>
                <div class="field">
                  <label for="city">City <span class="req" aria-hidden="true">*</span></label>
                  <input id="city" name="city" type="text" autocomplete="address-level2" required>
                </div>
                <div class="field">
                  <label for="state">State <span class="req" aria-hidden="true">*</span></label>
                  <input id="state" name="state" type="text" autocomplete="address-level1" value="TX" required>
                </div>
                <div class="field">
                  <label for="zip">Postal / zip code <span class="req" aria-hidden="true">*</span></label>
                  <input id="zip" name="zip" type="text" inputmode="numeric" autocomplete="postal-code" required>
                </div>
              </div>
            </fieldset>

            <fieldset>
              <legend>Flavors and cups</legend>
              <div class="field full">
                <span class="label-text">Flavor options</span>
                <span class="hint">Pick the ones you want at your event. The number of flavors included varies by package, and extra flavors can be added for a small charge.</span>
                <div class="choice-grid">{flavor_boxes}</div>
              </div>
              <fieldset class="choice-set">
                <legend>Select cup size</legend>
                <div class="choice-row">
                  <label class="check"><input type="radio" name="cup-size" value="Small cups $6"> <span>Small cups, $6</span></label>
                  <label class="check"><input type="radio" name="cup-size" value="Large cups $9"> <span>Large cups, $9</span></label>
                </div>
              </fieldset>
            </fieldset>

            <fieldset>
              <legend>Anything else</legend>
              <div class="field full">
                <label for="notes">Additional notes</label>
                <textarea id="notes" name="notes" placeholder="Where the cart will park, gate width, allergies, rain plan, invoicing or vendor paperwork"></textarea>
              </div>
            </fieldset>

            <fieldset>
              <legend>Booking acknowledgment</legend>
              <div class="field full">
                <label class="check start"><input type="checkbox" name="retainer-ack" value="Acknowledged" required>
                  <span>I understand that a 50% non-refundable retainer is required to secure my event date, and that events are not secured until the retainer is received. <span class="req" aria-hidden="true">*</span></span>
                </label>
              </div>
              <div class="field full">
                <label for="signature-name">Type your full name as your signature <span class="req" aria-hidden="true">*</span></label>
                <input id="signature-name" name="signature-name" type="text" class="signature-input" placeholder="Your full name" required>
                <span class="hint">Typing your name here acts as your signature on this inquiry.</span>
              </div>
            </fieldset>

            <div class="field full">
              <button class="btn btn-primary" type="submit">Send Catering Inquiry</button>
              <span class="hint">Sending this does not lock in your date. We will confirm availability and send your custom quote.</span>
            </div>
          </form>
        </div>

        <div>
          <div class="card">
            <h3>Other ways to reach us</h3>
            <ul style="list-style:none;padding:0;margin:0;display:grid;gap:12px;">
              <li data-contact-item hidden><strong>Call or text:</strong> <a data-contact="phone" href="#">Phone</a></li>
              <li data-contact-item hidden><strong>Email:</strong> <a data-contact="email" href="#">Email</a></li>
              <li data-contact-item hidden><strong>Facebook:</strong> <a data-contact="facebook" href="#" rel="noopener">Kreme Cruiser</a></li>
              <li data-contact-item hidden><strong>Instagram:</strong> <a data-contact="instagram" href="#" rel="noopener">@kreme_cruiser</a></li>
              <li data-contact-item hidden><strong>TikTok:</strong> <a data-contact="tiktok" href="#" rel="noopener">Kreme Cruiser</a></li>
            </ul>
          </div>
          <div class="card mt-32">
            <h3>Cup pricing</h3>
            <div class="table-wrap">
              <table>
                <tbody>
                  <tr><td>Small cup</td><td><strong>$6</strong></td></tr>
                  <tr><td>Large cup</td><td><strong>$9</strong></td></tr>
                </tbody>
              </table>
            </div>
            <p style="margin-top:14px;">Event pricing depends on your guest count, service window and location. Your custom quote comes back after we review your inquiry.</p>
          </div>
          <div class="card mt-32">
            <h3>Securing your date</h3>
            <p>A 50% non-refundable retainer holds your event date. Until that retainer is received, the date stays open to other bookings.</p>
          </div>
          <div class="card mt-32">
            <h3>Serving area</h3>
            <p>Pearland, Manvel, Rosharon, Iowa Colony, Alvin, Friendswood, Fresno, Missouri City, Sienna, Arcola, League City and South Houston. <a href="service-area.html">See the full list</a>.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

thanks_body = """  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Request received</span>
      <h1>Thanks, we have your request</h1>
      <p class="lede">We will check the date and get back to you with availability and a quote. If your event is close, reach out directly so we can move faster.</p>
      <div class="btn-row mt-32">
        <a class="btn btn-primary" href="index.html">Back to Home</a>
        <a class="btn btn-ghost" href="flavors.html">Browse the Flavors</a>
      </div>
    </div>
  </section>
"""

notfound_body = """  <section class="page-head">
    <div class="wrap narrow">
      <span class="eyebrow">Page not found</span>
      <h1>That page rolled off somewhere</h1>
      <p class="lede">The link you followed does not exist. Try one of these instead.</p>
      <div class="btn-row mt-32">
        <a class="btn btn-primary" href="index.html">Home</a>
        <a class="btn btn-ghost" href="flavors.html">Flavors</a>
        <a class="btn btn-ghost" href="contact.html">Book the Cart</a>
      </div>
    </div>
  </section>
"""

# ----------------------------------------------------------------- BUILD
H = ("index.html", "Home")

PAGES = [
    dict(slug="index.html",
         title="Kreme Cruiser | Mobile Water Ice Cart, South Houston",
         description="A pedal powered water ice cart for schools, daycares, birthdays and community events around Pearland, Manvel and Rosharon. Check your date.",
         body=home_body, trail=None),
    dict(slug="services.html",
         title="Water Ice Catering Services | Kreme Cruiser",
         description="Mobile water ice catering for schools, birthday parties and community events. See what comes with the cart, how service runs and what your venue needs.",
         body=services_body, trail=[H, ("services.html", "Services")]),
    dict(slug="schools-and-daycares.html",
         title="Water Ice for Schools &amp; Daycares | Kreme Cruiser",
         description="Field days, reward days, graduations and camp weeks. Rotation service that fits your bell schedule, indoors or out, across the south Houston area.",
         body=schools_body,
         trail=[H, ("services.html", "Services"), ("schools-and-daycares.html", "Schools &amp; Daycares")]),
    dict(slug="birthday-parties.html",
         title="Water Ice Cart Rental for Birthday Parties | Kreme Cruiser",
         description="Book the Kreme Cruiser water ice cart for a birthday party in Pearland, Manvel, Rosharon or nearby. Backyards, driveways, parks and clubhouses.",
         body=birthday_body,
         trail=[H, ("services.html", "Services"), ("birthday-parties.html", "Birthday Parties")]),
    dict(slug="community-and-corporate-events.html",
         title="Water Ice for Community &amp; Corporate Events | Kreme Cruiser",
         description="Sponsored cups or timed open service for church events, fundraisers, HOA nights, grand openings and staff appreciation days in the south Houston area.",
         body=community_body,
         trail=[H, ("services.html", "Services"), ("community-and-corporate-events.html", "Community &amp; Corporate")]),
    dict(slug="flavors.html",
         title="Water Ice Flavors | Kreme Cruiser Menu",
         description="Seventeen water ice flavors including Rainbow, Cotton Candy and Blue Razz. Every Kreme Cruiser flavor is dairy free. Cups are $6 small, $9 large.",
         body=flavors_body, trail=[H, ("flavors.html", "Flavors")],
         extra_schema=[flavor_schema]),
    dict(slug="service-area.html",
         title="Service Area | Kreme Cruiser Water Ice",
         description="Kreme Cruiser serves Pearland, Manvel, Rosharon, Iowa Colony, Alvin, Fresno, Missouri City and nearby communities. Ask about travel outside the area.",
         body=area_body, trail=[H, ("service-area.html", "Service Area")]),
    dict(slug="gallery.html",
         title="Photo Gallery | Kreme Cruiser Water Ice Cart",
         description="Photos of the Kreme Cruiser water ice cart at schools, daycares, indoor community events and parties, plus close ups of the flavors.",
         body=gallery_body, trail=[H, ("gallery.html", "Gallery")]),
    dict(slug="about.html",
         title="About Kreme Cruiser | Locally Owned Water Ice Cart",
         description="Why Kreme Cruiser runs a cart instead of a truck, how we work an event, and what we care about: showing up on time, moving the line and leaving it clean.",
         body=about_body, trail=[H, ("about.html", "About")]),
    dict(slug="faq.html",
         title="Booking Questions &amp; Answers | Kreme Cruiser",
         description="How far in advance to book, what space the cart needs, whether we serve indoors, allergy information and what a Kreme Cruiser event costs.",
         body=faq_body, trail=[H, ("faq.html", "FAQ")],
         extra_schema=[faq_schema]),
    dict(slug="contact.html",
         title="Book the Kreme Cruiser Water Ice Cart | Check Your Date",
         description="Send your date, location and headcount and we will confirm availability and send a quote for the Kreme Cruiser water ice cart.",
         body=contact_body, trail=[H, ("contact.html", "Book the Cart")]),
    dict(slug="thank-you.html",
         title="Request Received | Kreme Cruiser",
         description="Thanks for your booking request. We will confirm availability and send a quote.",
         body=thanks_body, trail=None, robots="noindex, follow"),
    dict(slug="404.html",
         title="Page Not Found | Kreme Cruiser",
         description="That page does not exist. Head back to the Kreme Cruiser home page or check your event date.",
         body=notfound_body, trail=None, robots="noindex, follow"),
]

if __name__ == "__main__":
    for page in PAGES:
        print("built", build(**page))
