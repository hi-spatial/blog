---
author: Kodibot
categories:
- WebGIS
date: 2026-02-28 12:55:07 +0700
layout: post
tags:
- AI
- Auto-Generated
- vanilla js
- leaflet
- javascript
- webgis
- tanpa framework
title: Membuat WebGIS dengan Vanilla JS dan Leaflet
---

## Pendahuluan
Membuat aplikasi WebGIS (Sistem Informasi Geografis berbasis web) tidak selalu memerlukan penggunaan framework yang kompleks. Dengan menggunakan Vanilla JS (JavaScript murni) dan library Leaflet, kita dapat menciptakan aplikasi WebGIS yang interaktif dan mudah digunakan. Pada artikel ini, kita akan menjelajahi cara membuat WebGIS menggunakan Vanilla JS dan Leaflet, serta memahami konsep dasar yang diperlukan untuk memulai proyek ini.

## Konsep Dasar / Teori
Sebelum memulai, ada beberapa konsep dasar yang perlu dipahami:
- **Vanilla JS**: Merupakan JavaScript murni tanpa menggunakan framework tambahan. Ini berarti kita akan menulis kode JavaScript dari awal tanpa bantuan library tambahan seperti React atau Angular.
- **Leaflet**: Adalah sebuah library JavaScript yang populer untuk membuat peta interaktif. Leaflet menyediakan berbagai fitur seperti zoom, panning, overlay, dan masih banyak lagi.
- **WebGIS**: Merupakan sistem yang mengintegrasikan teknologi GIS (Sistem Informasi Geografis) dengan teknologi web, memungkinkan pengguna untuk mengakses, menganalisis, dan memvisualisasikan data geospasial melalui antarmuka web.

## Tutorial / Langkah-langkah
Berikut adalah langkah-langkah dasar untuk membuat WebGIS dengan Vanilla JS dan Leaflet:
1. **Siapkan Proyek**: Buatlah folder baru untuk proyek Anda dan tambahkan file `index.html`, `style.css`, dan `script.js`.
2. **Tambahkan Leaflet**: Tambahkan library Leaflet ke dalam file `index.html` Anda dengan menambahkan tag script yang mengarah ke CDN Leaflet.
   ```html
   <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
   integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
   crossorigin=""/>
   <script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
   integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
   crossorigin=""></script>
   ```
3. **Buat Peta**: Tambahkan div untuk menampung peta di `index.html`.
   ```html
   <div id="map" style="width: 600px; height: 400px"></div>
   ```
4. **Inisialisasi Peta**: Di dalam file `script.js`, inisialisasi peta dengan menentukan lokasi awal dan zoom level.
   ```javascript
   var map = L.map('map').setView([51.505, -0.09], 13);
   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
     subdomains: ['a', 'b', 'c']
   }).addTo(map);
   ```
5. **Menambahkan Marker**: Anda bisa menambahkan marker ke peta untuk menandai lokasi tertentu.
   ```javascript
   var marker = L.marker([51.5, -0.09]).addTo(map);
   marker.bindPopup("<b>Hello World!</b><br>I am a popup.");
   ```

## Kesimpulan
Membuat WebGIS dengan Vanilla JS dan Leaflet adalah proses yang cukup sederhana dan memberikan banyak fleksibilitas dalam pengembangan aplikasi. Dengan memahami konsep dasar dan mengikuti langkah-langkah yang dijelaskan, Anda dapat dengan mudah membuat aplikasi WebGIS yang interaktif dan menarik.Leaflet menawarkan berbagai fitur yang siap pakai, seperti pengelolaan layer, overlay, dan kontrol peta, sehingga memudahkan pengembangan aplikasi WebGIS. Dengan Vanilla JS, Anda memiliki kontrol penuh atas kode dan dapat mengoptimalkan kinerja aplikasi sesuai kebutuhan. Oleh karena itu, kombinasi Vanilla JS dan Leaflet adalah pilihan yang sangat baik untuk proyek WebGIS, baik untuk pemula maupun developer yang lebih berpengalaman.