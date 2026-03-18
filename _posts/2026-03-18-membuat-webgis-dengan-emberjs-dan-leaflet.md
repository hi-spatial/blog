---
author: Kodibot
categories:
- WebGIS
date: 2026-03-18 10:25:00 +0700
layout: post
tags:
- AI
- Auto-Generated
- ember
- emberjs
- leaflet
- framework
- opinionated
title: Membuat WebGIS dengan EmberJS dan Leaflet
---

## Pendahuluan
Membuat aplikasi WebGIS yang interaktif dan dinamis merupakan salah satu tantangan dalam pengembangan sistem informasi geospasial. Dengan kemajuan teknologi web dan framework JavaScript, kita dapat membangun aplikasi WebGIS dengan mudah dan efisien. Dalam artikel ini, kita akan membahas tentang bagaimana membuat WebGIS dengan menggunakan EmberJS dan Leaflet, dua teknologi yang populer dalam pengembangan web dan geospasial.

EmberJS adalah sebuah framework JavaScript yang opinionated, artinya memiliki pendekatan yang kuat terhadap struktur dan arsitektur aplikasi. Sementara itu, Leaflet adalah sebuah library JavaScript yang dirancang untuk membangun aplikasi pemetaan web yang interaktif dan dinamis. Dengan menggabungkan kedua teknologi ini, kita dapat membangun aplikasi WebGIS yang kuat, fleksibel, dan mudah dipelajari.

## Konsep Dasar / Teori
Sebelum memulai, mari kita bahas beberapa konsep dasar yang perlu dipahami. EmberJS memiliki konsep tentang "routes", "models", dan "controllers" yang memungkinkan kita untuk membangun aplikasi dengan struktur yang jelas. Sementara itu, Leaflet memiliki konsep tentang "layer", "marker", dan "map" yang memungkinkan kita untuk membangun aplikasi pemetaan web yang interaktif.

Dalam konteks WebGIS, kita perlu memahami konsep tentang "spasial data" yang merepresentasikan informasi geografis dalam bentuk koordinat x, y, dan z. Kita juga perlu memahami konsep tentang "projeksi" yang mengubah koordinat geografis menjadi koordinat kartesian.

## Tutorial / Langkah-langkah
Berikut adalah langkah-langkah untuk membuat WebGIS dengan EmberJS dan Leaflet:

1. **Instalasi EmberJS**: Pertama, kita perlu menginstal EmberJS menggunakan npm dengan perintah `npm install -g ember-cli`.
2. **Buat Proyek Baru**: Buat proyek baru dengan perintah `ember new webgis`.
3. **Instalasi Leaflet**: Instal Leaflet dengan perintah `npm install leaflet`.
4. **Konfigurasi Route**: Buat route baru dengan perintah `ember generate route map`.
5. **Buat Template**: Buat template baru untuk menampilkan peta dengan menggunakan Leaflet.
```javascript
// app/templates/map.hbs
<div id="map" style="width: 800px; height: 600px;"></div>
```
6. **Buat Controller**: Buat controller baru untuk mengatur peta dan menambahkan layer.
```javascript
// app/controllers/map.js
import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class MapController extends Controller {
  @action
  setupMap() {
    const map = L.map('map').setView([51.505, -0.09], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
      subdomains: ['a', 'b', 'c']
    }).addTo(map);
  }
}
```
7. **Buat Model**: Buat model baru untuk menyimpan data spasial.
```javascript
// app/models/feature.js
import Model from '@ember/data/model';
import { attr } from '@ember/data';

export default class Feature extends Model {
  @attr('string') name;
  @attr('number') latitude;
  @attr('number') longitude;
}
```
8. **Tampilkan Peta**: Tampilkan peta dengan menggunakan Leaflet dan menambahkan layer.
```javascript
// app/routes/map.js
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class MapRoute extends Route {
  @service store;

  model() {
    return this.store.findAll('feature');
  }

  afterModel(model) {
    this.controllerFor('map').setupMap();
    model.forEach((feature) => {
      const marker = L.marker([feature.latitude, feature.longitude]).addTo(this.controllerFor('map').map);
      marker.bindPopup(feature.name);
    });
  }
}
```
## Kesimpulan
Dalam artikel ini, kita telah membahas tentang bagaimana membuat WebGIS dengan menggunakan EmberJS dan Leaflet. Dengan menggabungkan kedua teknologi ini, kita dapat membangun aplikasi WebGIS yang kuat, fleksibel, dan mudah dipelajari. EmberJS memungkinkan kita untuk membangun aplikasi dengan struktur yang jelas, sementara Leaflet memungkinkan kita untuk membangun aplikasi pemetaan web yang interaktif dan dinamis. Dengan menggunakan contoh kode yang disediakan, kita dapat memulai membuat aplikasi WebGIS sendiri dan meningkatkan kemampuan dalam pengembangan sistem informasi geospasial.