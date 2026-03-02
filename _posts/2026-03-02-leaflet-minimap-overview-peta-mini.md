---
author: Kodibot
categories:
- WebGIS
date: 2026-03-02 20:55:51 +0700
layout: post
tags:
- AI
- Auto-Generated
- leaflet
- minimap
- overview
- context
- plugin
title: 'Leaflet Minimap: Overview Peta Mini'
---

## Pendahuluan
Leaflet Minimap adalah fitur yang sangat berguna dalam visualisasi peta, terutama ketika bekerja dengan area yang luas atau kompleks. Minimap sendiri adalah peta mini yang menampilkan overview dari area yang sedang ditampilkan pada peta utama. Hal ini membantu pengguna untuk memahami konteks spasial dari data yang ditampilkan dan mempermudah navigasi. Dalam artikel ini, kita akan membahas konsep dasar Leaflet Minimap, cara kerjanya, dan bagaimana menggunakannya dalam proyek WebGIS.

## Konsep Dasar / Teori
Leaflet adalah sebuah library JavaScript yang populer untuk membuat peta interaktif di web. Salah satu kelebihan Leaflet adalah kemampuan untuk memperluas fungsionalitasnya melalui plugin. Leaflet Minimap adalah salah satu plugin yang paling berguna, karena memungkinkan pengguna untuk menampilkan peta mini di samping peta utama. Peta mini ini biasanya menampilkan keseluruhan area yang dipetakan, sehingga pengguna dapat melihat konteks spasial dari data yang ditampilkan pada peta utama.

## Tutorial / Langkah-langkah
Untuk menggunakan Leaflet Minimap, pertama-tama Anda perlu memasang Leaflet dan plugin Minimap di proyek Anda. Berikut adalah contoh cara melakukannya:
```javascript
// Memasang Leaflet dan plugin Minimap
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
   integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
   integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
   crossorigin=""></script>
<script src="https://github.com/Norkart/Leaflet-MiniMap/blob/master/dist/Leaflet:minimap.min.js"></script>
```
Setelah plugin terpasang, Anda dapat membuat peta utama dan minimap seperti berikut:
```javascript
// Membuat peta utama
var map = L.map('map').setView([51.505, -0.09], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
    subdomains: ['a', 'b', 'c']
}).addTo(map);

// Membuat minimap
var miniMap = new L.Control.MiniMap(
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
        subdomains: ['a', 'b', 'c']
    }), {
        position: 'bottomright'
    }
).addTo(map);
```
Dalam contoh di atas, kita membuat peta utama dengan tiles dari OpenStreetMap, kemudian membuat minimap dengan tiles yang sama dan menambahkannya ke peta utama pada posisi bottom-right.

## Kesimpulan
Leaflet Minimap adalah fitur yang sangat berguna dalam visualisasi peta, terutama ketika bekerja dengan area yang luas atau kompleks. Dengan menggunakan plugin Minimap, Anda dapat menampilkan peta mini di samping peta utama, sehingga mempermudah navigasi dan memahami konteks spasial dari data yang ditampilkan. Dalam artikel ini, kita telah membahas konsep dasar Leaflet Minimap, cara kerjanya, dan bagaimana menggunakannya dalam proyek WebGIS. Dengan demikian, Anda dapat memperluas fungsionalitas peta Anda dan membuatnya lebih interaktif dan mudah digunakan.