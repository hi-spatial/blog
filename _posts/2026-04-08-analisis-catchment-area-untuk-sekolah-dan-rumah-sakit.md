---
author: Kodibot
categories:
- GIS
date: 2026-04-08 10:38:40 +0700
layout: post
tags:
- AI
- Auto-Generated
- catchment
- sekolah
- rumah sakit
- service area
- network
title: Analisis Catchment Area untuk Sekolah dan Rumah Sakit
---

## Pendahuluan
Analisis Catchment Area, atau yang dikenal juga sebagai analisis service area, adalah metode yang digunakan untuk menentukan area layanan atau jangkauan dari suatu fasilitas atau lokasi tertentu. Dalam konteks sekolah dan rumah sakit, analisis ini sangat berguna untuk mengetahui seberapa jauh jangkauan atau area yang dapat dilayani oleh fasilitas tersebut. Dengan menggunakan teknik analisis geospasial, kita dapat memahami bagaimana lokasi sekolah dan rumah sakit mempengaruhi aksesibilitas masyarakat terhadap fasilitas-fasilitas tersebut.

## Konsep Dasar / Teori
Dasar dari analisis catchment area adalah konsep jaringan (network) dan service area. Service area merupakan area yang dapat dijangkau dari suatu lokasi tertentu dalam waktu atau jarak tertentu. Analisis ini mempertimbangkan beberapa faktor seperti jarak, waktu tempuh, dan kondisi jalan. Dalam konteks GIS, analisis catchment area dapat dilakukan menggunakan tools seperti Network Analyst, yang memungkinkan pengguna untuk menganalisis jaringan transportasi dan menentukan area layanan berdasarkan parameter-parameter yang ditentukan.

## Tutorial / Langkah-langkah
Berikut adalah langkah-langkah dasar untuk melakukan analisis catchment area menggunakan QGIS dan plugin Network Analyst:
1. **Siapkan Data**: Kumpulkan data spasial yang diperlukan, seperti lokasi sekolah atau rumah sakit, jaringan jalan, dan batas administratif.
2. **Buat Jaringan**: Buat jaringan dari data jalan yang ada, pastikan untuk mengatur atribut jalan seperti kecepatan dan arah.
3. **Tentukan Lokasi**: Tentukan lokasi sekolah atau rumah sakit yang akan dianalisis.
4. **Jalankan Analisis**: Gunakan plugin Network Analyst untuk menjalankan analisis catchment area, tetapkan parameter seperti jarak atau waktu tempuh maksimum.
5. **Visualisasikan**: Visualisasikan hasil analisis untuk memahami area layanan dari lokasi yang dipilih.

Contoh kode Python untuk melakukan analisis catchment area menggunakan librari `networkx` dan `geopandas`:
```python
import geopandas as gpd
import networkx as nx

# Load data jalan dan lokasi
jalan = gpd.read_file('jalan.shp')
lokasi = gpd.read_file('lokasi.shp')

# Buat jaringan
G = nx.Graph()
G.add_edges_from(jalan['geometry'])

# Tentukan lokasi
lokasi_pusat = lokasi.geometry[0]

# Jalankan analisis
catchment_area = []
for edge in G.edges():
    jarak = G.get_edge_data(edge[0], edge[1])['length']
    if jarak <= 1000:  # contoh: 1 km
        catchment_area.append(edge)

# Visualisasikan
catchment_gdf = gpd.GeoDataFrame(catchment_area, geometry='geometry')
catchment_gdf.plot()
```
## Kesimpulan
Analisis catchment area merupakan teknik yang powerful untuk memahami aksesibilitas dan jangkauan suatu fasilitas atau lokasi. Dengan menggunakan GIS dan tools analisis jaringan, kita dapat membuat keputusan yang lebih baik dalam perencanaan dan pengembangan infrastruktur, seperti penempatan sekolah dan rumah sakit. Memahami konsep dasar dan menerapkan langkah-langkah yang tepat, akan membantu pemula hingga pengguna menengah di bidang geospasial untuk melakukan analisis catchment area yang efektif.