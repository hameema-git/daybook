self.addEventListener('install', function(e) {
  console.log('Service Worker: Installed');
  e.waitUntil(
    caches.open('v1').then(function(cache) {
      return cache.addAll([
        '/',
        '/offline/',  // This is an optional path, make sure the offline page exists or you can remove it
        '/static/css/styles.css',  // Example static files you may want to cache
        '/static/js/script.js',    // Example static files you may want to cache
      ]);
    })
  );
});

self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request).then(function(networkResponse) {
        // Optionally, cache the new response for future use
        caches.open('v1').then(function(cache) {
          cache.put(e.request, networkResponse.clone());
        });
        return networkResponse;
      });
    })
  );
});
