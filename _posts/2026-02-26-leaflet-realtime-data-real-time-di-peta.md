---
author: Kodibot
categories:
- WebGIS
date: 2026-02-26 10:17:06 +0700
layout: post
tags:
- AI
- Auto-Generated
- leaflet
- realtime
- streaming
- live
- websocket
title: 'Leaflet Realtime: Data Real-time di Peta'
---

## Pendahuluan
Leaflet Realtime adalah sebuah library yang memungkinkan Anda untuk menampilkan data real-time di atas peta. Dengan menggunakan Leaflet Realtime, Anda dapat membuat aplikasi web yang menampilkan data yang terus-menerus berubah, seperti lokasi kendaraan, cuaca, atau kejadian lainnya. Pada artikel ini, kita akan membahas tentang konsep dasar Leaflet Realtime, bagaimana cara menggunakannya, dan beberapa contoh penggunaannya.

## Konsep Dasar / Teori
Leaflet Realtime menggunakan konsep websocket untuk melakukan komunikasi antara server dan klien. Websocket memungkinkan server untuk mengirimkan data ke klien tanpa harus menunggu request dari klien. Dengan demikian, data dapat dikirimkan secara real-time dan dapat diperbarui secara langsung di peta. Leaflet Realtime juga mendukung beberapa jenis data, seperti GeoJSON, CSV, dan lain-lain.

Untuk menggunakan Leaflet Realtime, Anda perlu memiliki server yang dapat mengirimkan data real-time ke klien. Anda dapat menggunakan teknologi seperti Node.js, Python, atau lainnya untuk membuat server. Pada klien, Anda perlu menggunakan library Leaflet Realtime untuk menampilkan data di atas peta.

## Tutorial / Langkah-langkah
Berikut adalah contoh langkah-langkah untuk menggunakan Leaflet Realtime:

1. Buatlah server yang dapat mengirimkan data real-time ke klien. Contohnya, Anda dapat menggunakan Node.js dan library `websocket` untuk membuat server WebSocket.
```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  console.log('Klien terhubung');

  // Kirimkan data ke klien setiap 1 detik
  setInterval(() => {
    const data = {
      type: 'Feature',
      geometry: {
        type: 'Point',
        coordinates: [106.816666, -6.166666]
      },
      properties: {
        nama: 'Lokasi 1'
      }
    };
    ws.send(JSON.stringify(data));
  }, 1000);
});
```
2. Buatlah klien yang dapat menampilkan data di atas peta. Contohnya, Anda dapat menggunakan library Leaflet Realtime dan library `leaflet` untuk menampilkan peta.
```javascript
const map = L.map('map').setView([ -6.166666, 106.816666], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a>',
  subdomains: ['a', 'b', 'c']
}).addTo(map);

const realtime = L.realtime({
  url: 'ws://localhost:8080',
  crossOrigin: true,
  type: 'json'
}, {
  pointToLayer: (feature, latlng) => {
    return L.circleMarker(latlng, {
      radius: 5,
      fillOpacity: 1,
      fillColor: '#ff0000'
    }).bindPopup(feature.properties.nama);
  }
}).addTo(map);
```
Dengan demikian, Anda dapat menampilkan data real-time di atas peta menggunakan Leaflet Realtime.

## Kesimpulan
Leaflet Realtime adalah sebuah library yang memungkinkan Anda untuk menampilkan data real-time di atas peta. Dengan menggunakan konsep websocket, Leaflet Realtime dapat mengirimkan data ke klien secara real-time dan dapat diperbarui secara langsung di peta. Pada artikel ini, kita telah membahas tentang konsep dasar Leaflet Realtime, bagaimana cara menggunakannya, dan beberapa contoh penggunaannya. Dengan demikian, Anda dapat membuat aplikasi web yang menampilkan data real-time di atas peta dengan menggunakan Leaflet Realtime.