---
author: Kodibot
categories:
- Python
date: 2026-02-11 20:50:26 +0700
layout: post
tags:
- AI
- Auto-Generated
- shapely
- python
- geometri
- spatial operations
title: Manipulasi Geometri dengan Shapely
---

## Pendahuluan
Manipulasi geometri adalah salah satu aspek penting dalam pengolahan data geospasial. Dalam Python, ada beberapa library yang dapat digunakan untuk melakukan manipulasi geometri, salah satunya adalah Shapely. Shapely adalah library Python yang memungkinkan kamu melakukan operasi-operasi geometri dasar seperti pembuatan, pengubahan, dan analisis bentuk-bentuk geometri. Pada artikel ini, kita akan membahas dasar-dasar manipulasi geometri dengan Shapely dan bagaimana cara menggunakannya dalam pengolahan data geospasial.

## Konsep Dasar / Teori
Sebelum kita mulai menggunakan Shapely, ada beberapa konsep dasar yang perlu kamu pahami. Geometri dalam Shapely dapat berupa titik (Point), garis (LineString), poligon (Polygon), dan koleksi dari objek-objek tersebut. Setiap objek geometri memiliki metode dan atribut yang memungkinkan kamu untuk melakukan operasi-operasi seperti perhitungan luas, panjang, dan interaksi dengan objek geometri lainnya.

Beberapa konsep dasar yang perlu diketahui antara lain:
- **Point**: Representasi dari sebuah titik di ruang 2D atau 3D.
- **LineString**: Sebuah garis yang terdiri dari dua atau lebih Point yang dihubungkan.
- **Polygon**: Sebuah bentuk yang terdiri dari satu atau lebih LineString yang tertutup.

## Tutorial / Langkah-langkah
Mari kita mulai dengan beberapa contoh sederhana menggunakan Shapely. Pastikan kamu telah menginstal Shapely di lingkungan Python kamu. Jika belum, kamu bisa menginstalnya menggunakan pip:
```bash
pip install shapely
```

### Membuat Objek Geometri
Kita bisa membuat objek geometri dasar seperti Point, LineString, dan Polygon menggunakan Shapely. Berikut adalah contoh kode untuk membuat objek-objek tersebut:
```python
from shapely.geometry import Point, LineString, Polygon

# Membuat sebuah Point
point = Point(1, 2)
print(point.x, point.y)  # Output: 1 2

# Membuat sebuah LineString
line = LineString([(1, 2), (3, 4), (5, 6)])
print(line.length)  # Output: panjang garis

# Membuat sebuah Polygon
polygon = Polygon([(0, 0), (1, 1), (1, 0)])
print(polygon.area)  # Output: luas poligon
```

### Operasi Geometri
Shapely juga mendukung berbagai macam operasi geometri seperti persimpangan, penggabungan, dan perhitungan jarak. Berikut adalah contoh operasi geometri antara dua objek Polygon:
```python
from shapely.geometry import Polygon

# Membuat dua Polygon
polygon1 = Polygon([(0, 0), (1, 1), (1, 0)])
polygon2 = Polygon([(0.5, 0), (1.5, 1), (1.5, 0)])

# Operasi persimpangan
intersection = polygon1.intersection(polygon2)
print(intersection.area)  # Output: luas persimpangan

# Operasi penggabungan
union = polygon1.union(polygon2)
print(union.area)  # Output: luas penggabungan
```

## Kesimpulan
Dalam artikel ini, kita telah membahas dasar-dasar manipulasi geometri dengan menggunakan Shapely di Python. Shapely memungkinkan kamu melakukan berbagai macam operasi geometri dengan mudah dan efisien. Dengan memahami konsep-konsep dasar dan cara menggunakan Shapely, kamu bisa meningkatkan kemampuan dalam pengolahan data geospasial. Shapely adalah tool yang sangat berguna bagi siapa saja yang bekerja dengan data geospasial, baik itu dalamAnalisis Geospasial, Pembuatan Peta, ataupun aplikasi-aplikasi lainnya yang terkait dengan lokasi dan ruang.