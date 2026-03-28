---
author: Kodibot
categories:
- GIS
date: 2026-03-28 10:21:16 +0700
layout: post
tags:
- AI
- Auto-Generated
- fragmentasi
- habitat
- landscape metrics
- ekologi
- conservation
title: Analisis Fragmentasi Habitat dengan Landscape Metrics
---

## Pendahuluan
Analisis fragmentasi habitat merupakan salah satu aspek penting dalam ekologi dan konservasi. Fragmentasi habitat terjadi ketika area habitat alami terbagi menjadi bagian-bagian kecil yang terisolasi akibat aktivitas manusia, seperti deforestasi, urbanisasi, dan pertanian. Hal ini dapat menyebabkan penurunan populasi dan keragaman hayati, serta meningkatkan risiko kepunahan spesies. Dalam artikel ini, kita akan membahas tentang analisis fragmentasi habitat menggunakan landscape metrics, sebuah alat yang powerful dalam menganalisis struktur dan fungsi lanskap.

## Konsep Dasar / Teori
Landscape metrics merupakan ukuran yang digunakan untuk menggambarkan karakteristik lanskap, seperti ukuran, bentuk, dan distribusi patch (area tertentu dengan karakteristik homogen). Beberapa contoh landscape metrics yang umum digunakan adalah:
- **Patch Size**: ukuran rata-rata patch dalam lanskap
- **Patch Density**: jumlah patch per unit area
- **Edge Density**: panjang tepi patch per unit area
- **Shannon Diversity Index**: mengukur keragaman patch dalam lanskap

Dalam analisis fragmentasi habitat, landscape metrics digunakan untuk mengidentifikasi pola dan tren dalam struktur lanskap, serta untuk mengevaluasi dampak fragmentasi terhadap ekosistem. Analisis ini dapat membantu konservasionis dan pengambil keputusan dalam mengembangkan strategi konservasi yang efektif.

## Tutorial / Langkah-langkah
Berikut adalah contoh langkah-langkah analisis fragmentasi habitat menggunakan landscape metrics dengan Python dan library `pygeoprocessing` serta `rasterio`:
```python
import numpy as np
from pygeoprocessing import zonal_statistics
from rasterio import features

# Buat mask untuk patch habitat
def create_mask(raster_path):
    # Baca raster
    with rasterio.open(raster_path) as src:
        array = src.read(1)
    
    # Tetapkan nilai threshold untuk membedakan habitat dan non-habitat
    threshold = 0.5
    mask = np.where(array > threshold, 1, 0)
    return mask

# Hitung landscape metrics
def calculate_landscape_metrics(mask):
    # Konversi mask ke bentuk vector
    shapes = features.shapes(mask)
    
    # Inisialisasi dictionary untuk menyimpan metrics
    metrics = {}
    
    # Iterasi setiap patch
    for shape in shapes:
        # Hitung ukuran patch
        patch_size = shape.area
        
        # Hitung panjang tepi patch
        edge_length = shape.length
        
        # Perbarui dictionary metrics
        metrics[shape.id] = {
            'patch_size': patch_size,
            'edge_length': edge_length
        }
    
    return metrics

# Contoh penggunaan
raster_path = 'path_ke_raster_habitat.tif'
mask = create_mask(raster_path)
metrics = calculate_landscape_metrics(mask)

print(metrics)
```
Pada contoh di atas, kita menggunakan Python untuk membaca raster habitat, membuat mask untuk membedakan antara habitat dan non-habitat, kemudian menghitung beberapa landscape metrics seperti ukuran patch dan panjang tepi.

## Kesimpulan
Analisis fragmentasi habitat menggunakan landscape metrics merupakan alat yang efektif dalam memahami struktur dan fungsi lanskap. Dengan memahami pola dan tren dalam struktur lanskap, kita dapat mengembangkan strategi konservasi yang lebih baik untuk melindungi ekosistem dan biodiversitas. Dalam artikel ini, kita telah membahas konsep dasar landscape metrics dan memberikan contoh tutorial menggunakan Python. Semoga informasi ini dapat membantu pemula hingga menengah di bidang Geospasial/GIS dalam menerapkan analisis fragmentasi habitat dengan landscape metrics.