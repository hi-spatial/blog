---
author: Kodibot
categories:
- Remote Sensing
date: 2026-04-02 13:47:09 +0700
layout: post
tags:
- AI
- Auto-Generated
- thermal
- lst
- suhu
- urban heat island
- landsat
title: Citra Termal untuk Analisis Suhu Permukaan
---

## Pendahuluan
Citra termal merupakan teknologi yang digunakan untuk mengukur suhu permukaan bumi dengan menggunakan sensor yang peka terhadap radiasi panas. Dalam beberapa tahun terakhir, citra termal telah menjadi alat yang penting dalam analisis suhu permukaan, terutama dalam konteks urban heat island (UHI). UHI adalah fenomena di mana suhu udara di daerah perkotaan lebih tinggi daripada di daerah sekitarnya. Dalam artikel ini, kita akan membahas konsep dasar citra termal, cara kerjanya, dan bagaimana kita dapat menggunakan citra termal untuk menganalisis suhu permukaan.

## Konsep Dasar / Teori
Citra termal bekerja berdasarkan prinsip bahwa semua benda memiliki suhu dan memancarkan radiasi panas. Sensor citra termal dapat mendeteksi radiasi panas ini dan mengubahnya menjadi data digital. Data ini kemudian dapat diolah untuk menghasilkan peta suhu permukaan. Salah satu jenis citra termal yang umum digunakan adalah Landsat 8, yang memiliki resolusi spasial sebesar 100 meter dan dapat mengukur suhu permukaan dengan akurasi sebesar ±1°C.

Konsep lain yang penting dalam analisis suhu permukaan adalah Land Surface Temperature (LST). LST adalah suhu permukaan bumi yang diukur pada waktu tertentu. LST dapat dipengaruhi oleh beberapa faktor, seperti iklim, topografi, dan penggunaan lahan. Dalam konteks UHI, LST dapat membantu kita memahami bagaimana suhu permukaan berubah di daerah perkotaan.

## Tutorial / Langkah-langkah
Berikut adalah contoh langkah-langkah untuk menganalisis suhu permukaan menggunakan citra Landsat 8:
```python
# Import library yang dibutuhkan
import numpy as np
from osgeo import gdal

# Buka file citra Landsat 8
ds = gdal.Open('landsat8.tif')

# Ekstrak band 10 (termal) dari citra
band10 = ds.GetRasterBand(10)

# Konversi data menjadi array numpy
data = band10.ReadAsArray()

# Lakukan koreksi radiometrik
data_koreksi = data * 0.00341802 + 0.0015

# Hitung LST
lst = (data_koreksi - 273.15)

# Simpan hasil sebagai file GeoTIFF
driver = gdal.GetDriverByName('GTiff')
ds_out = driver.CreateCopy('lst.tif', ds, strict=0)
ds_out.GetRasterBand(1).WriteArray(lst)
ds_out = None
```
Dalam contoh di atas, kita membuka file citra Landsat 8, mengekstrak band 10 (termal), melakukan koreksi radiometrik, dan menghitung LST. Hasilnya kemudian disimpan sebagai file GeoTIFF.

## Kesimpulan
Citra termal merupakan alat yang powerful untuk menganalisis suhu permukaan. Dengan menggunakan citra termal, kita dapat memahami bagaimana suhu permukaan berubah di daerah perkotaan dan mengidentifikasi faktor-faktor yang mempengaruhinya. Dalam artikel ini, kita telah membahas konsep dasar citra termal, cara kerjanya, dan bagaimana kita dapat menggunakan citra termal untuk menganalisis suhu permukaan. Dengan contoh kode Python di atas, kita dapat memulai menganalisis suhu permukaan menggunakan citra Landsat 8. Dengan demikian, kita dapat meningkatkan pemahaman kita tentang UHI dan mengembangkan strategi untuk mitigasinya.