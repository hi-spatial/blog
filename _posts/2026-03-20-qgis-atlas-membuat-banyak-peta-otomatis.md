---
author: Kodibot
categories:
- Tutorial
date: 2026-03-20 10:15:10 +0700
layout: post
tags:
- AI
- Auto-Generated
- qgis
- atlas
- print layout
- automation
- batch
title: 'QGIS Atlas: Membuat Banyak Peta Otomatis'
---

## Pendahuluan
QGIS Atlas adalah fitur powerful dalam QGIS yang memungkinkan pengguna untuk membuat banyak peta secara otomatis dengan layout yang konsisten. Fitur ini sangat berguna ketika Anda perlu menghasilkan peta dalam jumlah besar untuk tujuan seperti pelaporan, presentasi, atau publikasi. Dalam artikel ini, kita akan menjelajahi cara menggunakan QGIS Atlas untuk membuat banyak peta secara otomatis dan memahami konsep dasar di balik fitur ini.

## Konsep Dasar / Teori
Sebelum kita memulai tutorial, penting untuk memahami beberapa konsep dasar tentang QGIS Atlas dan komponen-komponennya:
- **Atlas**: Secara umum, atlas merujuk pada kumpulan peta yang disusun dalam sebuah koleksi. Dalam konteks QGIS, atlas adalah fitur yang memungkinkan Anda untuk membuat koleksi peta dengan layout yang konsisten.
- **Print Layout**: Fitur ini dalam QGIS memungkinkan Anda untuk mendesain layout peta yang siap dicetak. Dengan Print Layout, Anda dapat menambahkan berbagai elemen seperti judul, legenda, skala, dan lain-lain ke dalam peta Anda.
- **Automation**: Dalam konteks QGIS Atlas, automasi memungkinkan Anda untuk membuat banyak peta dengan cepat dan efisien tanpa perlu mengulangi langkah-langkah yang sama untuk setiap peta.

## Tutorial / Langkah-langkah
Berikut adalah langkah-langkah untuk membuat banyak peta secara otomatis menggunakan QGIS Atlas:
1. **Siapkan Data**: Pastikan Anda memiliki data spasial yang ingin digunakan untuk membuat peta. Data ini bisa berupa shapefile, GeoJSON, atau format data spasial lainnya.
2. **Buat Project Baru**: Buat project baru di QGIS dan tambahkan layer data spasial Anda ke dalamnya.
3. **Desain Print Layout**: Buka dialog Print Layout dengan mengklik `Project` > `Print Layout`. Beri nama layout Anda dan mulai desain layout peta Anda. Tambahkan elemen-elemen yang diinginkan seperti judul, legenda, skala, dan lain-lain.
4. **Aktifkan Atlas**: Dalam dialog Print Layout, buka tab `Atlas` dan centang opsi `Generate an atlas`. Pilih layer yang ingin digunakan sebagai sumber atlas.
5. **Konfigurasi Atlas**: Anda perlu mengatur beberapa pengaturan seperti format peta output, ukuran kertas, dan lain-lain. QGIS juga memungkinkan Anda untuk menambahkan ekspresi untuk mengontrol isi dan tampilan peta.
6. **Jalankan Atlas**: Klik tombol `Generate Atlas` untuk memulai proses pembuatan peta. QGIS akan membuat peta secara otomatis berdasarkan konfigurasi Anda.

## Kesimpulan
QGIS Atlas adalah alat yang sangat berguna untuk membuat banyak peta secara otomatis dengan layout yang konsisten. Dengan memahami konsep dasar dan mengikuti langkah-langkah yang disebutkan di atas, Anda dapat menggunakan QGIS Atlas untuk meningkatkan produktivitas dan efisiensi dalam pekerjaan geospasial Anda. Ingatlah untuk selalu memperbarui pengetahuan Anda tentang fitur-fitur terbaru di QGIS untuk memanfaatkan kemampuan atlas secara maksimal.