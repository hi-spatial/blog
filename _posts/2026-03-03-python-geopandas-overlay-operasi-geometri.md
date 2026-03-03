---
author: Kodibot
categories:
- Python
date: 2026-03-03 13:07:49 +0700
layout: post
tags:
- AI
- Auto-Generated
- geopandas
- overlay
- intersection
- union
- spatial
title: 'Python Geopandas Overlay: Operasi Geometri'
---

## Pendahuluan
Dalam dunia Geospasial dan GIS, operasi geometri merupakan salah satu konsep dasar yang sangat penting. Operasi ini memungkinkan kita untuk menganalisis dan memanipulasi data spasial dengan cara yang lebih efektif. Salah satu perangkat yang populer digunakan untuk operasi geometri adalah Geopandas, yaitu sebuah library Python yang membantu dalam menganalisis dan memvisualisasikan data spasial. Pada artikel ini, kita akan membahas tentang Python Geopandas Overlay, yaitu operasi geometri yang memungkinkan kita untuk melakukan overlay atau tumpang tindih antara dua atau lebih layer spasial.

## Konsep Dasar / Teori
Sebelum kita memulai dengan contoh kode, mari kita bahas beberapa konsep dasar yang perlu diketahui tentang operasi overlay. Operasi overlay adalah proses menganalisis hubungan spasial antara dua atau lebih layer data spasial. Terdapat beberapa jenis operasi overlay, yaitu:
- **Intersection**: Operasi ini akan menghasilkan layer baru yang berisi area yang tumpang tindih antara dua layer.
- **Union**: Operasi ini akan menghasilkan layer baru yang berisi semua area dari kedua layer, tanpa melakukan penghapusan area yang tumpang tindih.
- **Difference**: Operasi ini akan menghasilkan layer baru yang berisi area yang tidak tumpang tindih antara dua layer.
- **Symmetric Difference**: Operasi ini akan menghasilkan layer baru yang berisi area yang tidak tumpang tindih antara dua layer, tanpa memperhatikan urutan layer.

## Tutorial / Langkah-langkah
Berikut adalah contoh kode Python yang menggunakan Geopandas untuk melakukan operasi overlay:
```python
import geopandas as gpd
from shapely.geometry import Point, Polygon

# Buat layer spasial pertama
layer1 = gpd.GeoDataFrame(
    geometry=[
        Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
        Polygon([(0.5, 0), (1.5, 0), (1.5, 1), (0.5, 1)])
    ]
)

# Buat layer spasial kedua
layer2 = gpd.GeoDataFrame(
    geometry=[
        Polygon([(0.2, 0), (1.2, 0), (1.2, 1), (0.2, 1)]),
        Polygon([(0.8, 0), (1.8, 0), (1.8, 1), (0.8, 1)])
    ]
)

# Lakukan operasi intersection
intersection = gpd.overlay(layer1, layer2, how='intersection')

# Lakukan operasi union
union = gpd.overlay(layer1, layer2, how='union')

# Cetak hasil
print("Intersection:")
print(intersection)
print("Union:")
print(union)
```
Pada contoh di atas, kita membuat dua layer spasial yang masing-masing berisi dua buah poligon. Kemudian, kita melakukan operasi intersection dan union menggunakan fungsi `gpd.overlay`. Hasilnya akan berupa layer baru yang berisi area yang tumpang tindih atau semua area dari kedua layer.

## Kesimpulan
Dalam artikel ini, kita telah membahas tentang Python Geopandas Overlay, yaitu operasi geometri yang memungkinkan kita untuk melakukan overlay atau tumpang tindih antara dua atau lebih layer spasial. Kita juga telah membahas beberapa konsep dasar yang perlu diketahui tentang operasi overlay dan telah memberikan contoh kode Python yang menggunakan Geopandas untuk melakukan operasi overlay. Dengan menggunakan Geopandas, kita dapat dengan mudah melakukan analisis spasial dan memanipulasi data spasial dengan cara yang lebih efektif.