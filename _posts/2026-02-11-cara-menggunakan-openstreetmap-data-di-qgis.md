---
author: Kodibot
categories:
- GIS
date: 2026-02-11 20:22:17 +0700
layout: post
tags:
- AI
- Auto-Generated
- openstreetmap
- osm
- qgis
- open data
title: Cara Menggunakan OpenStreetMap Data di QGIS
---

## Pendahuluan
OpenStreetMap (OSM) adalah sebuah proyek kolaboratif yang bertujuan untuk menciptakan sebuah peta dunia yang bebas dan terbuka. Data OSM tersedia secara gratis dan dapat digunakan untuk berbagai keperluan, termasuk pengembangan aplikasi GIS. QGIS adalah sebuah perangkat lunak GIS yang populer dan gratis, yang dapat digunakan untuk menganalisis dan memvisualisasikan data geospasial. Dalam artikel ini, kita akan membahas tentang cara menggunakan data OSM di QGIS, mulai dari konsep dasar hingga langkah-langkah teknis.

## Konsep Dasar / Teori
Sebelum memulai, ada beberapa konsep dasar yang perlu dipahami. OSM menggunakan format data XML untuk menyimpan informasi tentang fitur geospasial, seperti jalan, bangunan, dan lain-lain. Data OSM dapat diunduh dalam berbagai format, termasuk Shapefile, GeoJSON, dan lain-lain. QGIS memiliki kemampuan untuk membaca dan menulis berbagai format data geospasial, termasuk data OSM.

Beberapa istilah yang perlu dipahami dalam konteks OSM dan QGIS antara lain:
- **Node**: Representasi sebuah titik geospasial dalam data OSM.
- **Way**: Representasi sebuah garis atau poligon dalam data OSM.
- **Relation**: Representasi sebuah hubungan antara fitur geospasial dalam data OSM.
- **Layer**: Sebuah konsep dalam QGIS yang merepresentasikan sebuah kumpulan fitur geospasial yang terkait.

## Tutorial / Langkah-langkah
Berikut adalah langkah-langkah untuk menggunakan data OSM di QGIS:
1. **Mengunduh Data OSM**: Anda dapat mengunduh data OSM dari situs web OSM atau menggunakan alat seperti Overpass Turbo. Pilih area yang ingin Anda unduh dan format data yang diinginkan (misalnya, Shapefile).
2. **Membuka Data OSM di QGIS**: Setelah data OSM diunduh, buka QGIS dan pilih "Layer" > "Add Layer" > "Add Vector Layer". Pilih file data OSM yang telah diunduh dan klik "Open".
3. **Mengkonfigurasi Layer OSM**: Setelah layer OSM ditambahkan, Anda dapat mengkonfigurasi penampilan layer tersebut. Pilih "Layer" > "Properties" dan konfigurasikan warna, gaya, dan lain-lain sesuai keinginan.
4. **Menganalisis Data OSM**: Anda dapat menganalisis data OSM menggunakan berbagai alat dalam QGIS, seperti alat untuk menghitung jarak, area, dan lain-lain.

Contoh kode Python untuk mengunduh data OSM menggunakan Overpass API:
```python
import requests

# Definisikan area yang ingin diunduh
lat_min, lat_max, lon_min, lon_max = -7.75, -7.65, 110.35, 110.45

# Definisikan query Overpass
query = """
[out:csv][timeout:25];
(
  node(area:{{bbox}});
  <;
  relation(area:{{bbox}});
);
out;
"""

# Kirim request ke Overpass API
url = "https://overpass-api.de/api/interpreter"
params = {
    "data": query,
    "bbox": f"{lon_min},{lat_min},{lon_max},{lat_max}"
}
response = requests.get(url, params=params)

# Simpan hasil ke file
with open("data_osm.csv", "w") as f:
    f.write(response.text)
```
## Kesimpulan
Dalam artikel ini, kita telah membahas tentang cara menggunakan data OSM di QGIS, mulai dari konsep dasar hingga langkah-langkah teknis. Dengan menggunakan data OSM dan QGIS, Anda dapat menganalisis dan memvisualisasikan data geospasial dengan mudah dan efektif. Jangan ragu untuk mencoba sendiri dan mengexplorasi lebih lanjut kemampuan QGIS dan data OSM.