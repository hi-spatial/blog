---
author: Kodibot
categories:
- WebGIS
date: 2026-02-25 13:38:56 +0700
layout: post
tags:
- AI
- Auto-Generated
- leaflet
- marker
- rotate
- direction
- navigation
title: 'Leaflet Marker Rotate: Rotasi Marker'
---

## Pendahuluan
Leaflet adalah salah satu library JavaScript yang paling populer untuk membangun aplikasi pemetaan web. Salah satu fitur yang paling berguna dalam Leaflet adalah kemampuan untuk menambahkan marker pada peta. Marker dapat digunakan untuk menandai lokasi-lokasi tertentu pada peta dan memberikan informasi lebih lanjut tentang lokasi tersebut. Namun, terkadang kita memerlukan kemampuan untuk merotasi marker agar sesuai dengan arah atau navigasi yang diinginkan. Dalam artikel ini, kita akan membahas tentang Leaflet Marker Rotate, yaitu fitur yang memungkinkan kita untuk merotasi marker pada peta.

## Konsep Dasar / Teori
Sebelum kita memulai dengan tutorial, ada beberapa konsep dasar yang perlu dipahami. Pertama, kita perlu memahami bahwa Leaflet menggunakan sistem koordinat yang berbeda dengan sistem koordinat geografi. Leaflet menggunakan sistem koordinat Cartesius, di mana titik (0, 0) berada di tengah-tengah peta. Kedua, kita perlu memahami bahwa marker dalam Leaflet dapat diatur menggunakan properti CSS, termasuk properti `transform` yang dapat digunakan untuk merotasi marker.

## Tutorial / Langkah-langkah
Untuk merotasi marker pada peta Leaflet, kita dapat menggunakan properti `transform` dalam CSS. Berikut adalah contoh cara melakukannya:
```javascript
// Buat peta
var map = L.map('map').setView([51.505, -0.09], 13);

// Tambahkan lapisan peta
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
    subdomains: ['a', 'b', 'c']
}).addTo(map);

// Buat marker
var marker = L.marker([51.505, -0.09]);

// Tambahkan marker ke peta
marker.addTo(map);

// Rotasi marker 45 derajat
marker.getElement().style.transform = 'rotate(45deg)';
```
Dalam contoh di atas, kita menggunakan metode `getElement()` untuk mendapatkan elemen HTML marker, kemudian kita atur properti `transform` menggunakan JavaScript. Nilai `rotate(45deg)` berarti bahwa marker akan diputar sebesar 45 derajat searah jarum jam.

## Kesimpulan
Dalam artikel ini, kita telah membahas tentang Leaflet Marker Rotate, yaitu fitur yang memungkinkan kita untuk merotasi marker pada peta. Kita telah membahas tentang konsep dasar yang perlu dipahami sebelum memulai, kemudian kita telah memberikan contoh cara merotasi marker menggunakan properti `transform` dalam CSS. Dengan menggunakan fitur ini, kita dapat membuat aplikasi pemetaan yang lebih interaktif dan menarik.