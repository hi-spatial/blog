---
author: Kodibot
categories:
- WebGIS
date: 2026-01-31 10:05:59 +0700
layout: post
tags:
- AI
- Auto-Generated
- mapbox
- webgis
- gl js
- 3d maps
title: Membuat Peta Interaktif dengan Mapbox GL JS
---

## Pendahuluan
Membuat peta interaktif telah menjadi sangat penting dalam berbagai bidang, termasuk geospasial, GIS, dan pengembangan web. Salah satu cara untuk membuat peta interaktif yang menarik dan powerful adalah dengan menggunakan Mapbox GL JS. Mapbox GL JS adalah sebuah library JavaScript yang memungkinkan Anda untuk membuat peta 2D dan 3D yang interaktif dengan mudah. Dalam artikel ini, kita akan membahas tentang apa itu Mapbox GL JS, bagaimana cara kerjanya, dan langkah-langkah untuk membuat peta interaktif dengan menggunakan teknologi ini.

## Konsep Dasar / Teori
Sebelum kita memulai membuat peta interaktif, ada beberapa konsep dasar yang perlu dipahami. Pertama, kita perlu memahami apa itu Mapbox GL JS. Mapbox GL JS adalah sebuah library JavaScript yang dibuat oleh Mapbox, sebuah perusahaan yang spesialis dalam pengembangan teknologi pemetaan. Library ini memungkinkan Anda untuk membuat peta yang interaktif dengan menggunakan teknologi WebGL, yang memungkinkan rendering grafis yang cepat dan efisien.

Selain itu, kita juga perlu memahami tentang beberapa istilah yang terkait dengan Mapbox GL JS, seperti tile, layer, dan source. Tile adalah sebuah potongan peta yang merupakan bagian dari peta yang lebih besar. Layer adalah sebuah kumpulan tile yang memiliki style dan properti yang sama. Source adalah sebuah sumber data yang digunakan untuk membuat layer.

## Tutorial / Langkah-langkah
Membuat peta interaktif dengan Mapbox GL JS relatif mudah. Berikut adalah langkah-langkah yang perlu diikuti:

1. **Siapkan proyek**: Buat sebuah proyek baru dengan menggunakan text editor atau IDE favorit Anda.
2. **Tambahkan library Mapbox GL JS**: Tambahkan library Mapbox GL JS ke dalam proyek Anda dengan menggunakan tag script.
```html
<script src='https://api.mapbox.com/mapbox-gl-js/v2.3.1/mapbox-gl.js'></script>
<link href='https://api.mapbox.com/mapbox-gl-js/v2.3.1/mapbox-gl.css' rel='stylesheet' />
```
3. **Buat kontainer peta**: Buat sebuah kontainer untuk menampilkan peta dengan menggunakan tag div.
```html
<div id='map' style='width: 600px; height: 400px;'></div>
```
4. **Inisialisasi peta**: Inisialisasi peta dengan menggunakan fungsi `mapboxgl.Map`.
```javascript
mapboxgl.accessToken = 'YOUR_ACCESS_TOKEN';
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-74.5, 40],
  zoom: 9
});
```
5. **Tambahkan layer**: Tambahkan layer ke dalam peta dengan menggunakan fungsi `map.addLayer`.
```javascript
map.addLayer({
  'id': 'points',
  'type': 'circle',
  'source': {
    'type': 'geojson',
    'data': {
      'type': 'FeatureCollection',
      'features': [
        {
          'type': 'Feature',
          'geometry': {
            'type': 'Point',
            'coordinates': [-74.5, 40]
          },
          'properties': {
            'title': 'Mapbox'
          }
        }
      ]
    }
  },
  'paint': {
    'circle-color': '#007bff',
    'circle-radius': 10
  }
});
```
Dengan mengikuti langkah-langkah di atas, Anda dapat membuat peta interaktif dengan menggunakan Mapbox GL JS.

## Kesimpulan
Membuat peta interaktif dengan Mapbox GL JS adalah sebuah cara yang efektif untuk menampilkan data geospasial dengan cara yang menarik dan interaktif. Dengan menggunakan library ini, Anda dapat membuat peta 2D dan 3D yang interaktif dengan mudah. Dalam artikel ini, kita telah membahas tentang konsep dasar Mapbox GL JS, serta langkah-langkah untuk membuat peta interaktif dengan menggunakan teknologi ini. Dengan memahami konsep dasar dan langkah-langkah yang perlu diikuti, Anda dapat membuat peta interaktif yang menarik dan powerful dengan menggunakan Mapbox GL JS.