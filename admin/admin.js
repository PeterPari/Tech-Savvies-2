/* Tech-Savvies: internal prompt checklist. Saves checkmarks in this browser and copies prompts. */

(function () {
  var STORAGE_KEY = "ts-admin-done";

  // Storage can be blocked (private mode, site data off); the page still works, just unsaved
  function loadDone() {
    try {
      var saved = JSON.parse(window.localStorage.getItem(STORAGE_KEY));
      return Array.isArray(saved) ? saved : [];
    } catch (error) {
      return [];
    }
  }

  function saveDone(ids) {
    try {
      window.localStorage.setItem(STORAGE_KEY, JSON.stringify(ids));
    } catch (error) {
      /* not saved; nothing else to do */
    }
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    // Fallback for plain-http previews
    return new Promise(function (resolve, reject) {
      var area = document.createElement("textarea");
      area.value = text;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      var ok = document.execCommand("copy");
      document.body.removeChild(area);
      if (ok) resolve();
      else reject(new Error("copy failed"));
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var boxes = Array.prototype.slice.call(document.querySelectorAll("[data-done]"));
    var count = document.querySelector("[data-done-count]");
    var reset = document.querySelector("[data-reset]");
    var status = document.querySelector("[data-copy-status]");

    function refresh() {
      var done = boxes.filter(function (box) { return box.checked; });
      boxes.forEach(function (box) {
        box.closest(".prompt-row").classList.toggle("is-done", box.checked);
      });
      count.textContent = String(done.length);
      reset.hidden = done.length === 0;
      return done.map(function (box) { return box.getAttribute("data-done"); });
    }

    var saved = loadDone();
    boxes.forEach(function (box) {
      box.checked = saved.indexOf(box.getAttribute("data-done")) !== -1;
      box.addEventListener("change", function () {
        saveDone(refresh());
      });
    });
    refresh();

    reset.addEventListener("click", function () {
      if (!window.confirm("Clear all checkmarks?")) return;
      boxes.forEach(function (box) { box.checked = false; });
      saveDone(refresh());
    });

    // Copy buttons need JavaScript, so they stay hidden without it
    Array.prototype.slice.call(document.querySelectorAll("[data-copy]")).forEach(function (button) {
      var label = button.querySelector("[data-copy-label]");
      var timer;
      button.hidden = false;

      button.addEventListener("click", function () {
        var source = document.getElementById(button.getAttribute("data-copy"));
        copyText(source.textContent).then(function () {
          button.classList.add("is-copied");
          label.textContent = "Copied";
          status.textContent = "Prompt copied to the clipboard.";
          clearTimeout(timer);
          timer = setTimeout(function () {
            button.classList.remove("is-copied");
            label.textContent = "Copy";
            status.textContent = "";
          }, 2000);
        }, function () {
          label.textContent = "Copy failed";
          status.textContent = "Copy failed. Open View prompt and copy it by hand.";
        });
      });
    });
  });
})();
