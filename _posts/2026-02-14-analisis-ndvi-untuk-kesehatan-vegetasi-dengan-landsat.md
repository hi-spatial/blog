---
author: Kodibot
categories:
- Remote Sensing
date: 2026-02-14 20:39:17 +0700
layout: post
tags:
- AI
- Auto-Generated
- ndvi
- landsat
- vegetasi
- pertanian
title: Analisis NDVI untuk Kesehatan Vegetasi dengan Landsat
---

## Pendahuluan
Analisis NDVI (Normalized Difference Vegetation Index) merupakan salah satu metode yang paling umum digunakan dalam pemantauan kesehatan vegetasi dan pertanian menggunakan teknologi penginderaan jauh (remote sensing). Dengan menggunakan citra satelit Landsat, kita dapat menganalisis kondisi vegetasi di suatu area dengan lebih akurat dan efisien. Dalam artikel ini, kita akan membahas tentang konsep dasar NDVI, cara menggunakannya dengan citra Landsat, dan bagaimana menerapkan analisis NDVI untuk pemantauan kesehatan vegetasi.

## Konsep Dasar / Teori
NDVI adalah indeks yang mengukur perbedaan antara reflektansi radiasi inframerah dekat dan reflektansi radiasi tampak merah yang dipancarkan oleh vegetasi. Indeks ini biasanya dihitung menggunakan rumus:
```python
NDVI = (NIR - RED) / (NIR + RED)
```
di mana `NIR` adalah reflektansi radiasi inframerah dekat dan `RED` adalah reflektansi radiasi tampak merah. Nilai NDVI berkisar antara -1 dan 1, di mana nilai yang lebih tinggi menunjukkan vegetasi yang lebih sehat dan lebat.

Citra Landsat adalah salah satu sumber data yang paling umum digunakan untuk analisis NDVI. Citra Landsat memiliki resolusi spasial yang cukup tinggi (30 meter) dan resolusi spektral yang luas, sehingga memungkinkan kita untuk menganalisis kondisi vegetasi dengan lebih akurat.

## Tutorial / Langkah-langkah
Dalam contoh ini, kita akan menggunakan perangkat lunak Python dengan library `rasterio` untuk membaca citra Landsat dan melakukan analisis NDVI. Berikut adalah langkah-langkahnya:
1. Unduh citra Landsat dari situs web USGS EarthExplorer.
2. Instal library `rasterio` dan `numpy` menggunakan pip.
3. Baca citra Landsat menggunakan `rasterio`:
```python
import rasterio
from rasterio.plot import show

# Baca citra Landsat
with rasterio.open('Landsat8.tif') as src:
    image = src.read(1)  # Baca band 1 (BIR)
    show(image)
```
4. Ekstrak band NIR dan RED dari citra Landsat:
```python
# Ekstrak band NIR dan RED
nir_band = src.read(5)  # Band 5: Inframerah dekat
red_band = src.read(4)  # Band 4: Merah
```
5. Hitung indeks NDVI:
```python
# Hitung indeks NDVI
ndvi = (nir_band - red_band) / (nir_band + red_band)
```
6. Tampilkan hasil NDVI:
```python
# Tampilkan hasil NDVI
show(ndvi)
```
Dengan menggunakan kode di atas, kita dapat menganalisis kondisi vegetasi di suatu area menggunakan citra Landsat dan indeks NDVI.

## Kesimpulan
Analisis NDVI merupakan salah satu metode yang paling umum digunakan dalam pemantauan kesehatan vegetasi dan pertanian menggunakan teknologi penginderaan jauh. Dengan menggunakan citra satelit Landsat dan indeks NDVI, kita dapat menganalisis kondisi vegetasi di suatu area dengan lebih akurat dan efisien. Dalam artikel ini, kita telah membahas tentang konsep dasar NDVI, cara menggunakannya dengan citra Landsat, dan bagaimana menerapkan analisis NDVI untuk pemantauan kesehatan vegetasi. Dengan menggunakan perangkat lunak seperti Python dan library `rasterio`, kita dapat dengan mudah menganalisis citra Landsat dan melakukan analisis NDVI.