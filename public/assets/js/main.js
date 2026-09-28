/* Tech-Savvies: small progressive enhancements. Every page also works without JavaScript. */

// Loaded in <head> so the mobile menu is collapsed before the first paint.
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", function () {
  initMobileNav();
  initFooterYear();
  initContactForm();
});

function initMobileNav() {
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (!header || !toggle || !nav) return;

  function isOpen() {
    return toggle.getAttribute("aria-expanded") === "true";
  }

  function setOpen(open) {
    toggle.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
    document.documentElement.classList.toggle("menu-open", open); // stop the page scrolling behind the menu
  }

  toggle.addEventListener("click", function () {
    setOpen(!isOpen());
  });

  // Close on Escape, on choosing a link, or on a click outside the header
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && isOpen()) {
      setOpen(false);
      toggle.focus();
    }
  });

  nav.addEventListener("click", function (event) {
    if (event.target.closest("a")) setOpen(false);
  });

  document.addEventListener("click", function (event) {
    if (isOpen() && !header.contains(event.target)) setOpen(false);
  });

  // Reset when the screen grows to the desktop layout
  window.matchMedia("(min-width: 48em)").addEventListener("change", function (event) {
    if (event.matches) setOpen(false);
  });
}

function initFooterYear() {
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
}

// Netlify handles the submission itself; this only prevents double submits.
function initContactForm() {
  var form = document.querySelector("form[data-netlify]");
  if (!form) return;

  var button = form.querySelector('button[type="submit"]');
  var label = button && button.querySelector("[data-label]");
  if (!button || !label) return;

  var idleText = label.textContent;

  form.addEventListener("submit", function () {
    button.disabled = true;
    label.textContent = "Sending…";
  });

  // Restore the button if the visitor comes back with the Back button
  window.addEventListener("pageshow", function () {
    button.disabled = false;
    label.textContent = idleText;
  });
}
