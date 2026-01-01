---
title: "Pengenalan QGIS untuk Pemula"
date: 2026-01-06 10:00:00 +0700
categories: [Tutorial, QGIS, GIS]
description: "Panduan memulai dengan QGIS, software GIS open source yang powerful untuk analisis dan pemetaan."
author: HI Spatial
---

QGIS (Quantum GIS) adalah software Geographic Information System open source yang free dan powerful. Dalam tutorial ini, kita akan membahas dasar-dasar penggunaan QGIS.

## Mengapa QGIS?

QGIS menawarkan banyak keunggulan:

- **Gratis dan open source** - tidak perlu biaya lisensi
- **Cross-platform** - berjalan di Windows, Mac, dan Linux
- **Plugin ecosystem** - ribuan plugin untuk berbagai kebutuhan
- **Support format luas** - vector, raster, database spasial
- **Komunitas aktif** - dokumentasi dan support yang baik

## Instalasi QGIS

Download QGIS dari [qgis.org](https://qgis.org/). Pilih versi LTR (Long Term Release) untuk stabilitas.

## Interface QGIS

Ketika membuka QGIS, Anda akan melihat:

1. **Menu Bar** - akses ke semua fitur
2. **Toolbar** - shortcut untuk fitur umum
3. **Layers Panel** - daftar layer aktif
4. **Map Canvas** - area tampilan peta
5. **Browser Panel** - navigasi file dan database
6. **Status Bar** - informasi koordinat dan skala

## Menambahkan Layer

### Layer Vector (Shapefile)

```
Layer → Add Layer → Add Vector Layer...
```

Pilih file `.shp` dari komputer Anda.

### Layer Raster

```
Layer → Add Layer → Add Raster Layer...
```

Untuk file `.tif`, `.jpg`, dll.

### Basemap dari Internet

Gunakan plugin **QuickMapServices**:

1. Plugins → Manage and Install Plugins
2. Cari "QuickMapServices"
3. Install
4. Web → QuickMapServices → OSM → OSM Standard

## Operasi Dasar

### Navigasi Peta

| Aksi | Shortcut |
|------|----------|
| Zoom In | Scroll atas / `+` |
| Zoom Out | Scroll bawah / `-` |
| Pan | Klik tengah + drag |
| Zoom to Layer | Klik kanan layer → Zoom to Layer |

### Identifikasi Fitur

Klik tombol **Identify** (ikon `i`) lalu klik pada fitur untuk melihat atributnya.

### Styling Layer

1. Klik kanan pada layer → Properties
2. Tab Symbology
3. Ubah warna, ukuran, atau style lainnya

## Membuat Layout Peta

Untuk export peta profesional:

1. Project → New Print Layout
2. Tambahkan elemen: peta, legend, scale bar, north arrow
3. Export sebagai PDF atau gambar

## Plugin yang Direkomendasikan

- **QuickMapServices** - basemap
- **OpenLayers Plugin** - layer dari Google, Bing, dll
- **Qgis2Web** - export ke web map
- **Processing** - tools geoprocessing

## Tips untuk Pemula

1. **Simpan project** secara berkala (Ctrl+S)
2. **Gunakan CRS yang konsisten** untuk semua layer
3. **Backup data** sebelum melakukan editing
4. **Manfaatkan dokumentasi** QGIS yang lengkap

## Selanjutnya

Setelah menguasai dasar, Anda dapat mempelajari:
- Digitasi dan editing data
- Analisis spasial
- Styling dan kartografi
- Automatisasi dengan Python

Selamat belajar QGIS!
