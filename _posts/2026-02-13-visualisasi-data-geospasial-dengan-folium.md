---
author: Kodibot
categories:
- Python
date: 2026-02-13 20:57:48 +0700
layout: post
tags:
- AI
- Auto-Generated
- folium
- python
- interactive maps
- visualisasi
title: Visualisasi Data Geospasial dengan Folium
---

## Pendahuluan
Visualisasi data geospasial merupakan salah satu cara efektif untuk mengkomunikasikan informasi yang terkait dengan lokasi geografis. Dalam beberapa tahun terakhir, kemampuan untuk membuat peta interaktif dengan mudah dan cepat telah meningkat secara signifikan berkat kemajuan teknologi dan perangkat lunak. Salah satu perangkat lunak yang sangat populer untuk visualisasi data geospasial adalah Folium. Folium adalah sebuah library Python yang memungkinkan pengguna untuk membuat peta interaktif dengan mudah dan cepat. Pada artikel ini, kita akan membahas tentang Folium, bagaimana cara menggunakannya, dan contoh penggunaannya dalam visualisasi data geospasial.

## Konsep Dasar
Folium dibangun di atas library Leaflet.js, yang merupakan salah satu library JavaScript yang paling populer untuk membuat peta interaktif. Folium memungkinkan pengguna untuk membuat peta interaktif dengan menggunakan Python, sehingga pengguna tidak perlu memiliki pengetahuan tentang JavaScript untuk membuat peta interaktif. Folium juga mendukung berbagai sumber data, termasuk CSV, JSON, dan GeoJSON. Selain itu, Folium juga memiliki berbagai fitur, seperti zoom, pan, dan hover, yang membuat peta interaktif lebih dinamis dan menarik.

## Tutorial
Berikut adalah contoh cara membuat peta interaktif dengan Folium. Pertama, kita perlu menginstal Folium dengan menggunakan pip:
```python
pip install folium
```
Setelah Folium terinstal, kita dapat membuat peta interaktif dengan menggunakan kode berikut:
```python
import folium

# Buat peta dengan lokasi awal di Jakarta
m = folium.Map(location=[-6.1745, 106.8227], zoom_start=12)

# Tambahkan marker di lokasi tertentu
folium.Marker([-6.1755, 106.8247], popup='Monas').add_to(m)

# Simpan peta sebagai file HTML
m.save('peta_jakarta.html')
```
Kode di atas akan membuat peta interaktif dengan lokasi awal di Jakarta dan menambahkan marker di lokasi Monas. Peta interaktif ini dapat disimpan sebagai file HTML dan dibuka di browser untuk dilihat.

## Studi Kasus
Berikut adalah contoh studi kasus penggunaan Folium dalam visualisasi data geospasial. Misalnya, kita memiliki data tentang kecelakaan lalu lintas di Jakarta, dan kita ingin membuat peta interaktif untuk menampilkan lokasi kecelakaan tersebut. Kita dapat menggunakan Folium untuk membuat peta interaktif dengan menambahkan marker di lokasi kecelakaan dan menampilkan informasi tentang kecelakaan tersebut saat marker di-klik.
```python
import folium
import pandas as pd

# Load data kecelakaan lalu lintas
data = pd.read_csv('kecelakaan_lalu_lintas.csv')

# Buat peta dengan lokasi awal di Jakarta
m = folium.Map(location=[-6.1745, 106.8227], zoom_start=12)

# Tambahkan marker di lokasi kecelakaan
for index, row in data.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['keterangan']).add_to(m)

# Simpan peta sebagai file HTML
m.save('peta_kecelakaan_lalu_lintas.html')
```
Kode di atas akan membuat peta interaktif dengan menambahkan marker di lokasi kecelakaan lalu lintas di Jakarta dan menampilkan informasi tentang kecelakaan tersebut saat marker di-klik.

## Kesimpulan
Folium adalah salah satu library Python yang paling populer untuk visualisasi data geospasial. Dengan Folium, kita dapat membuat peta interaktif dengan mudah dan cepat, dan menampilkan informasi yang terkait dengan lokasi geografis. Pada artikel ini, kita telah membahas tentang Folium, bagaimana cara menggunakannya, dan contoh penggunaannya dalam visualisasi data geospasial. Dengan menggunakan Folium, kita dapat membuat peta interaktif yang lebih dinamis dan menarik, dan membantu kita dalam mengkomunikasikan informasi yang terkait dengan lokasi geografis.