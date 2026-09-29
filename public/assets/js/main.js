/* Tech-Savvies: small progressive enhancements. Every page also works without JavaScript. */

// Loaded in <head> so the mobile menu is collapsed before the first paint.
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", function () {
  initMobileNav();
  initFocusClearance();
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

    // Keep keyboard focus out of the page hidden behind the open menu (no-op where inert is unsupported)
    var siblings = document.body.children;
    for (var i = 0; i < siblings.length; i++) {
      if (siblings[i] === header) continue;
      if (open) siblings[i].setAttribute("inert", "");
      else siblings[i].removeAttribute("inert");
    }
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

  // While the menu is open, Tab wraps from the last header link to the first and back
  header.addEventListener("keydown", function (event) {
    if (event.key !== "Tab" || !isOpen()) return;
    var items = header.querySelectorAll("a[href], button");
    var first = items[0];
    var last = items[items.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
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

// Tall focused elements (like the /privacy/ table) can land under the sticky header; nudge them below it
function initFocusClearance() {
  var header = document.querySelector(".site-header");
  if (!header) return;
  var tabbing = false;

  // Only act on focus moved by Tab, not on clicks or on focus coming back to the window
  document.addEventListener("keydown", function (event) {
    if (event.key === "Tab") tabbing = true;
  });
  window.addEventListener("blur", function () {
    tabbing = false;
  });

  document.addEventListener("focusin", function (event) {
    var target = event.target;
    if (!tabbing) return;
    tabbing = false;
    if (header.contains(target) || target.classList.contains("skip-link")) return;

    window.requestAnimationFrame(function () {
      var overlap = header.getBoundingClientRect().bottom - target.getBoundingClientRect().top;
      if (overlap > 0) window.scrollBy(0, -(overlap + 16));
    });
  });
}

function initFooterYear() {
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
}

// Netlify handles the submission itself. This adds text error messages and prevents double submits.
function initContactForm() {
  var form = document.querySelector("form[data-netlify]");
  if (!form) return;

  var button = form.querySelector('button[type="submit"]');
  var label = button && button.querySelector("[data-label]");
  if (!button || !label) return;

  var idleText = label.textContent;
  var status = document.getElementById("form-status");
  var messages = {
    name: "Enter your name.",
    email: "Enter your email address.",
    emailFormat: "Enter an email address like name@example.com.",
    service: "Choose what you need, or pick “Not sure yet”.",
    message: "Tell us a little about your project."
  };
  var fields = [];
  for (var i = 0; i < form.elements.length; i++) {
    var field = form.elements[i];
    if (field.required && document.getElementById(field.id + "-error")) fields.push(field);
  }

  // JavaScript shows its own messages; without it the browser's validation still runs
  form.noValidate = true;

  function errorFor(field) {
    if (!field.value.trim()) return messages[field.id];
    if (field.validity.typeMismatch) return messages[field.id + "Format"];
    return "";
  }

  function describedBy(field, id, add) {
    var ids = (field.getAttribute("aria-describedby") || "").split(" ").filter(function (value) {
      return value && value !== id;
    });
    if (add) ids.push(id);
    if (ids.length) field.setAttribute("aria-describedby", ids.join(" "));
    else field.removeAttribute("aria-describedby");
  }

  function showError(field, text) {
    var error = document.getElementById(field.id + "-error");
    var prefix = document.createElement("span");
    prefix.className = "visually-hidden";
    prefix.textContent = "Error: ";
    error.textContent = text;
    error.insertBefore(prefix, error.firstChild);
    error.hidden = false;
    field.setAttribute("aria-invalid", "true");
    describedBy(field, error.id, true);
  }

  function clearError(field) {
    var error = document.getElementById(field.id + "-error");
    error.textContent = "";
    error.hidden = true;
    field.setAttribute("aria-invalid", "false"); // "false", not removed: an empty required <select> is otherwise exposed as invalid
    describedBy(field, error.id, false);
  }

  // Screen readers read the role="status" paragraph without moving focus (WCAG 4.1.3)
  function announce(text) {
    if (status) status.textContent = text;
  }

  // Returns true when the field is valid
  function check(field) {
    var text = errorFor(field);
    if (text) showError(field, text);
    else clearError(field);
    return !text;
  }

  fields.forEach(function (field) {
    // Check a field once the visitor leaves it after typing, and clear its error as soon as it's fixed
    // Focus has usually moved on by then, so the error is also announced
    field.addEventListener("change", function () {
      announce(check(field) ? "" : "Error: " + errorFor(field));
    });
    field.addEventListener("input", function () {
      if (field.getAttribute("aria-invalid") === "true" && !errorFor(field)) clearError(field);
    });
  });

  form.addEventListener("submit", function (event) {
    var firstInvalid = null;
    fields.forEach(function (field) {
      if (!check(field) && !firstInvalid) firstInvalid = field;
    });

    // Focus moves to the first invalid field, whose description is its error, so nothing is announced
    if (firstInvalid) {
      event.preventDefault();
      announce("");
      firstInvalid.focus();
      return;
    }

    button.disabled = true;
    label.textContent = "Sending…";
    announce("Sending your message…");
  });

  // Restore the button if the visitor comes back with the Back button
  window.addEventListener("pageshow", function () {
    button.disabled = false;
    label.textContent = idleText;
    announce("");
  });
}
