self.addEventListener('install', function(e) {
  console.log('Service Worker: Installed');
  e.waitUntil(
    caches.open('v1').then(function(cache) {
      return cache.addAll([
        '/',  // Only cache the home page for now
      ]);
    })
  );
});

self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});
