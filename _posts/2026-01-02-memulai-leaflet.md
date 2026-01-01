---
title: "Memulai dengan Leaflet.js: Peta Interaktif Pertama Anda"
date: 2026-01-02 10:00:00 +0700
categories: [Tutorial, Leaflet, WebGIS]
description: "Tutorial langkah demi langkah untuk membuat peta interaktif menggunakan Leaflet.js dari awal."
author: HI Spatial
---

Leaflet.js adalah library JavaScript open-source yang paling populer untuk membuat peta interaktif. Dalam tutorial ini, kita akan membuat peta pertama dari nol.

## Persiapan

Pertama, buat file HTML sederhana dan tambahkan library Leaflet:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Peta Pertama Saya</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        #map { height: 400px; width: 100%; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script src="app.js"></script>
</body>
</html>
```

## Inisialisasi Peta

Buat file `app.js` dan tambahkan kode berikut:

```javascript
// Inisialisasi peta dengan center di Jakarta
const map = L.map('map').setView([-6.2088, 106.8456], 12);

// Tambahkan tile layer dari OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);
```

## Menambahkan Marker

Untuk menambahkan marker pada lokasi tertentu:

```javascript
// Tambahkan marker
const marker = L.marker([-6.2088, 106.8456]).addTo(map);

// Tambahkan popup ke marker
marker.bindPopup('<b>Halo!</b><br>Ini adalah Jakarta.').openPopup();
```

## Menambahkan Circle dan Polygon

Leaflet juga mendukung berbagai bentuk geometri:

```javascript
// Tambahkan circle
const circle = L.circle([-6.1751, 106.8650], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(map);

// Tambahkan polygon
const polygon = L.polygon([
    [-6.19, 106.82],
    [-6.20, 106.85],
    [-6.18, 106.84]
]).addTo(map);
```

## Event Handling

Anda dapat menambahkan interaksi dengan event listener:

```javascript
// Tampilkan koordinat saat klik pada peta
map.on('click', function(e) {
    alert('Koordinat: ' + e.latlng.lat + ', ' + e.latlng.lng);
});
```

## Kesimpulan

Anda telah berhasil membuat peta interaktif pertama dengan Leaflet! Pada tutorial selanjutnya, kita akan membahas cara:

- Menggunakan GeoJSON untuk menampilkan data
- Membuat layer control
- Styling marker custom

Selamat mencoba dan eksplorasi lebih lanjut!
