const CACHE_NAME = 'rhythm-booster-cache-v1';
const urlsToCache = [
  './',
  './index.html',
  './manifest.json',
  './Screenshot_2021-02-06-16-54-37-50_87e97a45f9a3192000df2c5452ac2d54.png'
  // 如果你有外部 CSS、JS 檔，也要加進去這裡
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});
