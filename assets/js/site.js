/* Kreme Cruiser - shared site behavior
 * -----------------------------------------------------------------
 * EDIT ONE PLACE: fill in the CONTACT values below and every page
 * picks them up automatically. Leave a value as an empty string and
 * that link is hidden site wide instead of showing a placeholder.
 * ----------------------------------------------------------------- */

var CONTACT = {
  phone:     "(713) 530-6835",
  email:     "info@kremecruiser.com",
  facebook:  "https://www.facebook.com/p/Kreme-Cruiser-61588605541964/",
  instagram: "https://www.instagram.com/kreme_cruiser/",
  tiktok:    ""                       // full URL, optional
};

(function () {
  "use strict";

  function digits(s) { return String(s).replace(/[^0-9+]/g, ""); }

  /* Contact details -------------------------------------------------- */
  document.querySelectorAll("[data-contact]").forEach(function (node) {
    var key = node.getAttribute("data-contact");
    var value = CONTACT[key];
    var holder = node.closest("[data-contact-item]") || node;

    if (!value) { holder.hidden = true; return; }

    holder.hidden = false;
    if (key === "phone") {
      node.textContent = value;
      if (node.tagName === "A") { node.href = "tel:" + digits(value); }
    } else if (key === "email") {
      node.textContent = value;
      if (node.tagName === "A") { node.href = "mailto:" + value; }
    } else if (node.tagName === "A") {
      node.href = value;
    }
  });

  /* Mobile navigation ------------------------------------------------ */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* Current year in the footer --------------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (n) {
    n.textContent = new Date().getFullYear();
  });

  /* Prefill the booking form from links like contact.html?event=School */
  var eventField = document.getElementById("event-type");
  if (eventField) {
    var wanted = new URLSearchParams(window.location.search).get("event");
    if (wanted) {
      Array.prototype.forEach.call(eventField.options, function (opt) {
        if (opt.value.toLowerCase() === wanted.toLowerCase()) { opt.selected = true; }
      });
    }
  }

  /* Booking form date cannot be in the past --------------------------- */
  var dateField = document.getElementById("event-date");
  if (dateField && !dateField.min) {
    dateField.min = new Date().toISOString().split("T")[0];
  }
})();
