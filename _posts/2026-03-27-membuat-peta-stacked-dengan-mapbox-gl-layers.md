---
author: Kodibot
categories:
- WebGIS
date: 2026-03-27 10:38:05 +0700
layout: post
tags:
- AI
- Auto-Generated
- mapbox gl
- layers
- stacked
- visualization
- composite
title: Membuat Peta Stacked dengan Mapbox GL Layers
---

## Pendahuluan
Membuat peta yang menarik dan informatif adalah salah satu tujuan utama dalam pengembangan aplikasi Geospasial. Salah satu cara untuk mencapai hal ini adalah dengan menggunakan peta stacked, yaitu peta yang memiliki beberapa lapisan (layer) yang dapat diatur untuk menampilkan informasi yang berbeda-beda. Dalam artikel ini, kita akan membahas tentang bagaimana membuat peta stacked dengan menggunakan Mapbox GL Layers.

Mapbox GL adalah library JavaScript yang memungkinkan kita untuk membuat peta yang interaktif dan kaya fitur. Dengan menggunakan Mapbox GL, kita dapat membuat peta yang memiliki beberapa lapisan, seperti lapisan peta dasar, lapisan titik lokasi, lapisan polyline, dan lain-lain. Kita juga dapat mengatur properti dari setiap lapisan, seperti warna, opacity, dan lain-lain.

## Konsep Dasar / Teori
Sebelum kita memulai membuat peta stacked, kita perlu memahami beberapa konsep dasar tentang Mapbox GL Layers. Berikut adalah beberapa konsep yang perlu kita ketahui:

*   **Layer**: Layer adalah sebuah objek yang merepresentasikan sebuah lapisan dalam peta. Setiap layer memiliki props yang dapat diatur, seperti `id`, `type`, `source`, dan lain-lain.
*   **Source**: Source adalah sebuah objek yang merepresentasikan sumber data untuk sebuah layer. Contohnya, kita dapat menggunakan source `vector` untuk menampilkan data shapefile.
*   **Type**: Type adalah sebuah prop yang menentukan jenis dari sebuah layer. Contohnya, kita dapat menggunakan type `fill` untuk menampilkan layer sebagai polygon.

## Tutorial / Langkah-langkah
Berikut adalah contoh kode untuk membuat peta stacked dengan menggunakan Mapbox GL Layers:
```javascript
// Import library mapbox gl
import mapboxgl from 'mapbox-gl';

// Inisialisasi map
mapboxgl.accessToken = 'YOUR_ACCESS_TOKEN';
const map = new mapboxgl.Map({
  container: 'map', // container element
  style: 'mapbox://styles/mapbox/streets-v11', // style URL
  center: [-74.5, 40], // starting position [lng, lat]
  zoom: 9, // starting zoom
});

// Tambahkan layer peta dasar
map.on('load', () => {
  // Tambahkan layer titik lokasi
  map.addLayer({
    id: 'points',
    type: 'circle',
    source: {
      type: 'geojson',
      data: {
        type: 'FeatureCollection',
        features: [
          {
            type: 'Feature',
            geometry: {
              type: 'Point',
              coordinates: [-74.5, 40],
            },
            properties: {
              title: 'Mapbox',
            },
          },
        ],
      },
    },
    paint: {
      'circle-color': '#007bff',
      'circle-radius': 10,
    },
  });

  // Tambahkan layer polyline
  map.addLayer({
    id: 'polyline',
    type: 'line',
    source: {
      type: 'geojson',
      data: {
        type: 'FeatureCollection',
        features: [
          {
            type: 'Feature',
            geometry: {
              type: 'LineString',
              coordinates: [
                [-74.5, 40],
                [-74.6, 40.1],
              ],
            },
          },
        ],
      },
    },
    paint: {
      'line-color': '#ff69b4',
      'line-width': 2,
    },
  });
});
```
Dalam contoh kode di atas, kita menambahkan dua layer, yaitu layer titik lokasi dan layer polyline. Kita menggunakan prop `id` untuk mengidentifikasi setiap layer, prop `type` untuk menentukan jenis dari setiap layer, dan prop `source` untuk menentukan sumber data dari setiap layer. Kita juga menggunakan prop `paint` untuk mengatur properti visual dari setiap layer.

## Kesimpulan
Membuat peta stacked dengan menggunakan Mapbox GL Layers adalah sebuah cara yang efektif untuk menampilkan informasi yang berbeda-beda dalam sebuah peta. Dengan menggunakan konsep dasar tentang layer, source, dan type, kita dapat membuat peta yang interaktif dan kaya fitur. Dalam contoh kode di atas, kita menambahkan dua layer, yaitu layer titik lokasi dan layer polyline, untuk menampilkan informasi yang berbeda-beda dalam sebuah peta. Dengan menggunakan Mapbox GL, kita dapat membuat peta yang lebih menarik dan informatif untuk pengguna.