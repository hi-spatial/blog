---
author: Kodibot
categories:
- Python
date: 2026-03-30 10:47:09 +0700
layout: post
tags:
- AI
- Auto-Generated
- geocoding
- batch
- python
- nominatim
- automation
title: Geocoding Batch dengan Nominatim dan Python
---

## Pendahuluan
Geocoding adalah proses mengubah alamat tekstual menjadi koordinat geografis (latitude dan longitude) yang dapat digunakan dalam sistem informasi geospasial (GIS) atau aplikasi pemetaan. Dalam banyak kasus, kita perlu melakukan geocoding dalam jumlah besar, yang dikenal sebagai geocoding batch. Nominatim adalah salah satu layanan geocoding yang populer dan gratis, tetapi memiliki keterbatasan dalam hal jumlah permintaan per detik. Dalam artikel ini, kita akan membahas bagaimana melakukan geocoding batch dengan Nominatim dan Python.

## Konsep Dasar / Teori
Sebelum memulai, kita perlu memahami beberapa konsep dasar tentang geocoding dan Nominatim. Geocoding dapat dilakukan dengan menggunakan berbagai metode, seperti pencarian berbasis teks atau menggunakan algoritma kompleks. Nominatim adalah layanan geocoding yang disediakan oleh OpenStreetMap (OSM), yang menggunakan data OSM untuk melakukan geocoding. Nominatim memiliki beberapa keterbatasan, seperti:
- Maksimum 1 permintaan per detik
- Maksimum 50 permintaan per menit
- Tidak boleh digunakan untuk keperluan komersial

Untuk melakukan geocoding batch dengan Nominatim, kita perlu menggunakan library Python yang dapat menghandle permintaan ke Nominatim dan melakukan penanganan kesalahan.

## Tutorial / Langkah-langkah
Dalam tutorial ini, kita akan menggunakan library `requests` untuk melakukan permintaan ke Nominatim dan `pandas` untuk menghandle data. Berikut adalah langkah-langkahnya:
1. Instal library yang dibutuhkan: `requests` dan `pandas`
```python
pip install requests pandas
```
2. Buat sebuah file Python untuk melakukan geocoding batch
```python
import requests
import pandas as pd
import time

# Buat sebuah fungsi untuk melakukan geocoding
def geocode(alamat):
    url = f"https://nominatim.openstreetmap.org/search?q={alamat}&format=json&limit=1"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]["lat"], data[0]["lon"]
    else:
        return None, None

# Buat sebuah dataframe untuk menyimpan data alamat
df = pd.DataFrame({
    "alamat": ["Jl. Raya Jogja, Yogyakarta", "Jl. Raya Solo, Surakarta", "Jl. Raya Semarang, Semarang"]
})

# Buat sebuah kolom untuk menyimpan koordinat
df["lat"] = None
df["lon"] = None

# Lakukan geocoding batch
for index, row in df.iterrows():
    try:
        lat, lon = geocode(row["alamat"])
        df.at[index, "lat"] = lat
        df.at[index, "lon"] = lon
        time.sleep(1)  # tunggu 1 detik sebelum melakukan permintaan berikutnya
    except Exception as e:
        print(f"Error: {e}")

# Simpan dataframe ke file CSV
df.to_csv("geocoded_data.csv", index=False)
```
Dalam contoh di atas, kita melakukan geocoding batch untuk beberapa alamat dan menyimpan hasilnya ke dalam sebuah file CSV.

## Kesimpulan
Dalam artikel ini, kita telah membahas bagaimana melakukan geocoding batch dengan Nominatim dan Python. Kita telah menggunakan library `requests` untuk melakukan permintaan ke Nominatim dan `pandas` untuk menghandle data. Dengan menggunakan contoh kode di atas, kita dapat melakukan geocoding batch untuk jumlah besar alamat dan menyimpan hasilnya ke dalam sebuah file CSV. Namun, perlu diingat bahwa Nominatim memiliki keterbatasan dalam hal jumlah permintaan per detik, sehingga kita perlu melakukan penanganan kesalahan dan tunggu beberapa detik sebelum melakukan permintaan berikutnya.