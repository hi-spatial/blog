---
author: Kodibot
categories:
- WebGIS
date: 2026-01-29 10:10:35 +0700
layout: post
tags:
- AI
- Auto-Generated
- leaflet
- javascript
- webgis
- peta interaktif
title: Cara Membuat Peta Web Sederhana menggunakan Leaflet JS
---

## Pendahuluan
Dalam beberapa tahun terakhir, teknologi WebGIS telah berkembang pesat, memungkinkan pengguna untuk membuat peta interaktif di web dengan mudah. Salah satu library JavaScript yang paling populer untuk membuat peta web adalah Leaflet JS. Pada artikel ini, kita akan membahas cara membuat peta web sederhana menggunakan Leaflet JS, mulai dari konsep dasar hingga langkah-langkah praktis.

Leaflet JS adalah perpustakaan sumber terbuka yang memungkinkan Anda membuat peta interaktif dengan fitur seperti zoom, pan, dan overlay. Dengan menggunakan Leaflet, Anda dapat membuat peta yang menarik dan interaktif dengan mudah, bahkan jika Anda tidak memiliki pengalaman sebelumnya dalam pengembangan web atau geospasial.

## Konsep Dasar / Teori
Sebelum kita mulai membuat peta web, ada beberapa konsep dasar yang perlu dipahami. Pertama, kita perlu memahami struktur dasar dari Leaflet JS. Leaflet terdiri dari beberapa komponen utama, yaitu:
- Map: Objek yang mewakili peta itu sendiri.
- TileLayer: Lapisan yang menampilkan data peta, seperti tiles dari OpenStreetMap atau layanan lainnya.
- Marker: Objek yang digunakan untuk menandai lokasi tertentu di peta.
- Popup: Jendela yang muncul ketika pengguna mengklik sebuah marker, menampilkan informasi lebih lanjut.

Leaflet juga mendukung berbagai sumber data peta, termasuk OpenStreetMap, Mapbox, dan lain-lain. Anda dapat memilih sumber data yang sesuai dengan kebutuhan Anda.

## Tutorial / Langkah-langkah
Berikut adalah langkah-langkah untuk membuat peta web sederhana menggunakan Leaflet JS:
1. **Siapkan Proyek**: Buat sebuah folder untuk proyek Anda dan tambahkan file HTML (`index.html`), CSS (`style.css`), dan JavaScript (`script.js`).
2. **Tambahkan Leaflet**: Tambahkan Leaflet JS ke dalam proyek Anda dengan menambahkan tag `<script>` yang mengarah ke URL Leaflet di dalam tag `<head>` file `index.html`.
   ```html
   <head>
       <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
       <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
   </head>
   ```
3. **Buat Kontainer Peta**: Tambahkan sebuah elemen `<div>` di dalam file `index.html` yang akan menjadi kontainer untuk peta.
   ```html
   <body>
       <div id="map" style="width: 800px; height: 600px;"></div>
   </body>
   ```
4. **Inisialisasi Peta**: Di dalam file `script.js`, inisialisasi peta dan tambahkan lapisan tile.
   ```javascript
   // Inisialisasi peta
   var map = L.map('map').setView([37.7749, -122.4194], 13);
   
   // Tambahkan lapisan tile
   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
       attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
       subdomains: ['a', 'b', 'c']
   }).addTo(map);
   ```
5. **Tambahkan Marker dan Popup**: Tambahkan marker dan popup ke peta.
   ```javascript
   // Tambahkan marker
   var marker = L.marker([37.7749, -122.4194]).addTo(map);
   
   // Tambahkan popup
   marker.bindPopup("<b>Halo, Dunia!</b><br>Lokasi ini ditandai oleh marker.");
   ```

## Kesimpulan
Membuat peta web sederhana menggunakan Leaflet JS adalah proses yang cukup sederhana dan dapat dilakukan oleh siapa saja yang memiliki pengetahuan dasar tentang HTML, CSS, dan JavaScript. Dengan menggunakan Leaflet, Anda dapat membuat peta interaktif yang menarik dan efektif untuk mengkomunikasikan informasi geospasial. Pada contoh di atas, kita telah membuat peta web dasar dengan Leaflet JS, termasuk menambahkan lapisan tile, marker, dan popup. Ini hanya awal dari apa yang bisa Anda lakukan dengan Leaflet. Anda dapat mengeksplorasi lebih lanjut dengan menambahkan lebih banyak fitur dan interaktivitas ke peta Anda.