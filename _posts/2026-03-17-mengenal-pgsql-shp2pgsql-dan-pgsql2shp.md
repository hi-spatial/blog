---
author: Kodibot
categories:
- Data
date: 2026-03-17 21:16:10 +0700
layout: post
tags:
- AI
- Auto-Generated
- pgsql
- shp2pgsql
- import
- export
- postgis
title: 'Mengenal PGSQL: Shp2pgsql dan Pgsql2shp'
---

## Pendahuluan
Dalam dunia Geospasial/GIS, pengolahan data spasial menjadi salah satu aspek paling kritis. PostgreSQL dengan ekstensi PostGIS merupakan salah satu pilihan populer untuk mengelola database spasial. Namun, seringkali kita perlu melakukan konversi antara format data spasial, seperti Shapefile (.shp), dengan database PostgreSQL. Di sinilah peran tool seperti `shp2pgsql` dan `pgsql2shp` menjadi sangat penting. Artikel ini akan membahas tentang apa itu `shp2pgsql` dan `pgsql2shp`, bagaimana mereka bekerja, dan bagaimana kita bisa menggunakannya untuk mengimport dan mengekspor data spasial.

## Konsep Dasar / Teori
`shp2pgsql` dan `pgsql2shp` adalah tool command-line yang disediakan oleh PostGIS untuk melakukan konversi data spasial. `shp2pgsql` digunakan untuk mengimport data dari Shapefile ke dalam database PostgreSQL dengan PostGIS, sedangkan `pgsql2shp` digunakan untuk mengekspor data dari database PostgreSQL ke dalam format Shapefile.

- `shp2pgsql`: Tool ini membaca file Shapefile dan mengubahnya menjadi perintah SQL yang dapat dijalankan di PostgreSQL untuk membuat tabel yang sesuai dan memasukkan data ke dalamnya. Ini memungkinkan pengguna untuk dengan mudah mengimport data spasial ke dalam database mereka.
- `pgsql2shp`: Sebaliknya, `pgsql2shp` membaca data dari tabel PostgreSQL yang memiliki kolom geometri dan mengekspor data tersebut ke dalam file Shapefile. Ini sangat berguna ketika Anda perlu membagikan data spasial atau menggunakannya dalam aplikasi lain yang mendukung format Shapefile.

## Tutorial / Langkah-langkah
Berikut adalah langkah-langkah dasar untuk menggunakan `shp2pgsql` dan `pgsql2shp`:

### Mengimport Data dengan shp2pgsql
1. Pastikan Anda memiliki PostGIS terinstal dan diaktifkan di database PostgreSQL Anda.
2. Buka terminal atau command prompt dan navigasi ke direktori tempat file Shapefile Anda berada.
3. Jalankan perintah berikut untuk mengimport data Shapefile ke dalam database PostgreSQL:
   ```bash
   shp2pgsql -s 4326 -c nama_file.shp nama_tabel | psql -d nama_database -U nama_pengguna
   ```
   - `-s 4326` menentukan sistem referensi spasial (Spatial Reference System, SRS) untuk data Anda. Pastikan ini sesuai dengan SRS yang digunakan oleh file Shapefile Anda.
   - `nama_file.shp` adalah nama file Shapefile yang ingin diimport.
   - `nama_tabel` adalah nama tabel di database PostgreSQL tempat data akan disimpan.
   - `nama_database` dan `nama_pengguna` harus diganti dengan nama database dan pengguna PostgreSQL Anda.
4. Setelah menjalankan perintah, data Shapefile Anda seharusnya sudah terimport ke dalam database PostgreSQL.

### Mengekspor Data dengan pgsql2shp
1. Pastikan Anda memiliki akses ke database PostgreSQL yang berisi data spasial yang ingin diekspor.
2. Jalankan perintah berikut untuk mengekspor data dari database PostgreSQL ke dalam format Shapefile:
   ```bash
   pgsql2shp -f output.shp nama_database nama_tabel
   ```
   - `output.shp` adalah nama file Shapefile yang dihasilkan.
   - `nama_database` dan `nama_tabel` harus diganti dengan nama database dan tabel yang ingin diekspor.
3. Setelah menjalankan perintah, Anda seharusnya melihat file Shapefile baru di direktori kerja Anda yang berisi data spasial dari database PostgreSQL.

## Kesimpulan
`shp2pgsql` dan `pgsql2shp` adalah tool yang sangat berguna dalam pengolahan data spasial, memungkinkan kita untuk dengan mudah mengimport dan mengekspor data antara format Shapefile dan database PostgreSQL dengan PostGIS. Dengan memahami dan menggunakan tool-tool ini, Anda dapat lebih efisien dalam mengelola dan menganalisis data spasial, yang pada akhirnya dapat membantu dalam pengambilan keputusan dan pemecahan masalah di berbagai bidang, termasuk perencanaan wilayah, lingkungan, dan transportasi.