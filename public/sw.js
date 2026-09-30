/* Removes the old site's service worker. Nothing on this site registers a service worker. */

// The tech-savvies.com site before the 2026 relaunch installed a service worker at /sw.js that cached
// its pages. Browsers that still have it fetch this file when they check for an update, install it,
// and it then deletes the old caches and unregisters itself. Keep this file: if /sw.js returned 404,
// the old worker would stay installed and could keep showing the old pages offline.
self.addEventListener("install", function () {
  self.skipWaiting();
});

self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys()
      .then(function (keys) {
        return Promise.all(keys.map(function (key) {
          return caches.delete(key);
        }));
      })
      .then(function () {
        return self.registration.unregister();
      })
  );
});
