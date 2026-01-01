---
title: "Memahami Sistem Koordinat dan Proyeksi Peta"
date: 2026-01-04 10:00:00 +0700
categories: [Konsep, GIS]
description: "Panduan memahami sistem koordinat geografis, proyeksi peta, dan penggunaannya dalam GIS."
author: HI Spatial
---

Memahami sistem koordinat dan proyeksi peta adalah fundamental bagi siapa saja yang bekerja dengan data geospatial. Artikel ini akan menjelaskan konsep dasar yang perlu Anda ketahui.

## Sistem Koordinat Geografis

Sistem koordinat geografis menggunakan **latitude** dan **longitude** untuk menentukan posisi di permukaan bumi.

- **Latitude**: Sudut dari ekuator, range -90° (Kutub Selatan) hingga +90° (Kutub Utara)
- **Longitude**: Sudut dari Prime Meridian, range -180° hingga +180°

### Contoh Koordinat

| Lokasi | Latitude | Longitude |
|--------|----------|-----------|
| Jakarta | -6.2088 | 106.8456 |
| Bandung | -6.9175 | 107.6191 |
| Surabaya | -7.2575 | 112.7521 |

## Proyeksi Peta

Karena bumi berbentuk elipsoid, kita perlu "memproyeksikan" permukaannya ke bidang datar (peta). Setiap proyeksi memiliki distorsi tersendiri.

### Jenis Proyeksi Umum

1. **Web Mercator (EPSG:3857)**
   - Digunakan oleh Google Maps, OpenStreetMap
   - Bagus untuk navigasi, buruk untuk area analysis

2. **WGS84 (EPSG:4326)**
   - Sistem koordinat GPS
   - Menggunakan derajat lat/lng

3. **UTM (Universal Transverse Mercator)**
   - Membagi bumi menjadi 60 zona
   - Bagus untuk analisis jarak dan area

## EPSG Codes

EPSG adalah database standar untuk sistem koordinat. Beberapa kode yang sering digunakan:

```
EPSG:4326  - WGS84 (lat/lng dalam derajat)
EPSG:3857  - Web Mercator
EPSG:32748 - UTM Zone 48S (Indonesia Barat)
EPSG:32749 - UTM Zone 49S (Indonesia Tengah)
EPSG:32750 - UTM Zone 50S (Indonesia Timur)
```

## Transformasi Koordinat

Dalam praktek, Anda sering perlu mengkonversi antara sistem koordinat:

```javascript
// Menggunakan Proj4js
proj4.defs("EPSG:32748", "+proj=utm +zone=48 +south +datum=WGS84 +units=m");

// Konversi dari lat/lng ke UTM
const utm = proj4("EPSG:4326", "EPSG:32748", [106.8456, -6.2088]);
console.log(utm); // [699706.xx, 9312830.xx]
```

## Tips Praktis

1. **Selalu catat EPSG code** dari data Anda
2. **Gunakan Web Mercator** untuk tampilan web
3. **Gunakan UTM** untuk analisis yang memerlukan akurasi jarak/area
4. **Backup data asli** sebelum melakukan transformasi

## Kesimpulan

Pemahaman sistem koordinat dan proyeksi sangat penting untuk:
- Menghindari kesalahan posisi
- Melakukan analisis spasial yang akurat
- Mengintegrasikan data dari berbagai sumber

Pada artikel selanjutnya, kita akan membahas lebih detail tentang format data spasial populer.
