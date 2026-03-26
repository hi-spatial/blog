---
author: Kodibot
categories:
- Tutorial
date: 2026-03-26 13:43:47 +0700
layout: post
tags:
- AI
- Auto-Generated
- qgis
- expression
- labeling
- text
- cartography
title: 'QGIS Plugin: QGIS Expressions untuk Labelling'
---

## Pendahuluan
QGIS merupakan salah satu perangkat lunak Sistem Informasi Geografis (SIG) yang paling populer dan banyak digunakan karena kemampuan dan fleksibilitasnya yang tinggi. Salah satu fitur yang sangat berguna dalam QGIS adalah kemampuan labelling, yaitu proses memberikan label atau teks pada fitur geospasial seperti titik, garis, dan poligon. QGIS Expressions untuk labelling memungkinkan pengguna untuk membuat label yang dinamis dan interaktif dengan menggunakan ekspresi yang dapat disesuaikan dengan kebutuhan masing-masing. Dalam artikel ini, kita akan mempelajari konsep dasar QGIS Expressions untuk labelling dan melakukan tutorial praktis untuk menerapkan fitur ini.

## Konsep Dasar / Teori
QGIS Expressions adalah bahasa ekspresi yang digunakan dalam QGIS untuk melakukan pengolahan data dan visualisasi yang lebih kompleks. Dalam konteks labelling, ekspresi ini memungkinkan pengguna untuk mengontrol apa yang ditampilkan sebagai label, bagaimana tampilannya, dan di mana label tersebut ditempatkan. Ekspresi dapat berupa fungsi sederhana seperti menggabungkan field-field tertentu menjadi satu label, hingga ekspresi yang lebih kompleks yang melibatkan perhitungan geometri dan kondisi logika.

Beberapa konsep dasar yang perlu dipahami sebelum menggunakan QGIS Expressions untuk labelling adalah:
- **Field**: Kolom dalam tabel atribut yang terkait dengan layer.
- **Fungsi**: Operasi yang dapat dilakukan pada field atau nilai, seperti `concat` untuk menggabungkan string atau `sqrt` untuk menghitung akar kuadrat.
- **Variabel**: Nilai yang dapat digunakan dalam ekspresi untuk merepresentasikan sesuatu yang dinamis.

## Tutorial / Langkah-langkah
Untuk mempraktikkan QGIS Expressions dalam labelling, mari kita lakukan contoh sederhana:

1. **Buka QGIS dan Buat Layer**: Buka QGIS dan buat atau tambahkan layer yang ingin diberi label. Untuk contoh ini, kita akan menggunakan layer titik yang mewakili kota-kota besar di suatu negara.

2. **Buka Jendela Labelling**:
   - Pilih layer yang ingin diberi label di panel 'Layers'.
   - Klik kanan pada layer tersebut dan pilih 'Properties'.
   - Pilih tab 'Labels' di jendela 'Layer Properties'.

3. **Menggunakan QGIS Expressions**:
   - Di tab 'Labels', pastikan 'Label with' diatur ke 'Expression'.
   - Klik pada tombol '...' di sebelah kanan input 'Expression' untuk membuka jendela 'Expression String Builder'.
   - Di sini, Anda dapat membangun ekspresi Anda. Misalnya, untuk menggabungkan nama kota dan provinsi menjadi satu label, Anda bisa menggunakan fungsi `concat` seperti berikut:
     ```python
     concat("Nama_Kota", ', ', "Nama_Provinsi")
     ```
   - Klik 'OK' untuk menerapkan ekspresi.

4. **Menyesuaikan Tampilan Label**:
   - Setelah menerapkan ekspresi, Anda bisa menyesuaikan tampilan label seperti font, ukuran, warna, dan lain-lain di tab 'Labels'.

5. **Menerapkan Perubahan**:
   - Klik 'OK' di jendela 'Layer Properties' untuk menerapkan perubahan labelling.

## Kesimpulan
QGIS Expressions memberikan fleksibilitas yang tinggi dalam labelling di QGIS, memungkinkan pengguna untuk membuat label yang dinamis dan interaktif. Dengan memahami konsep dasar dan melakukan praktik seperti yang ditunjukkan dalam tutorial di atas, Anda dapat meningkatkan kemampuan visualisasi dan analisis data geospasial Anda. Ekspresi yang lebih kompleks dapat membuka lebih banyak kemungkinan dalam pengolahan dan presentasi data, menjadikan QGIS sebagai alat yang sangat powerful dalam bidang Geospasial/GIS.