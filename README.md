# HI Spatial Blog

Blog tutorial seputar **Geospatial** dan **WebGIS** - Belajar Leaflet, Mapbox, QGIS, dan teknologi spasial lainnya.

![Jekyll](https://img.shields.io/badge/Jekyll-CC0000?style=flat&logo=jekyll&logoColor=white)
![Ruby](https://img.shields.io/badge/Ruby-CC342D?style=flat&logo=ruby&logoColor=white)

## 🚀 Quick Start

### Prasyarat

- Ruby 3.0+
- Bundler (`gem install bundler`)

### Instalasi

```bash
# Clone repository
git clone https://github.com/hispatial/hi-spatial-blog.git
cd hi-spatial-blog

# Install dependencies
bundle install

# Jalankan development server
bundle exec jekyll serve
```

Buka browser ke `http://localhost:4000`

## 📁 Struktur Proyek

```
hi-spatial-blog/
├── _config.yml        # Konfigurasi Jekyll
├── _includes/         # Partial components (header, footer, dll)
├── _layouts/          # Template layouts
├── _posts/            # Artikel blog (Markdown)
├── assets/
│   ├── css/           # Stylesheet
│   └── js/            # JavaScript
├── categories.html    # Halaman kategori
├── search.html        # Halaman pencarian
├── about.markdown     # Halaman tentang
├── robots.txt         # SEO robots file
└── index.html         # Halaman utama
```

## ✍️ Menulis Artikel

Buat file baru di `_posts/` dengan format nama:

```
YYYY-MM-DD-judul-artikel.md
```

Contoh front matter:

```yaml
---
layout: post
title: "Memulai dengan Leaflet.js"
date: 2026-01-02
categories: [leaflet, webgis]
tags: [javascript, mapping, tutorial]
excerpt: "Panduan lengkap memulai pemetaan web dengan Leaflet.js"
---

Konten artikel di sini...
```

## 🔧 Konfigurasi

Edit `_config.yml` untuk mengubah:

| Setting | Deskripsi |
|---------|-----------|
| `title` | Nama situs |
| `description` | Deskripsi untuk SEO |
| `url` | URL produksi |
| `author` | Informasi penulis |
| `paginate` | Jumlah post per halaman |

## 🔍 Fitur

- ✅ **Responsive Design** - Tampilan optimal di semua perangkat
- ✅ **Pencarian** - Cari artikel dengan cepat
- ✅ **Kategori** - Organisasi artikel berdasarkan topik
- ✅ **SEO Optimized** - Meta tags, sitemap, robots.txt
- ✅ **RSS Feed** - Subscribe untuk update artikel
- ✅ **Syntax Highlighting** - Code blocks dengan Rouge

## 📦 Plugins

| Plugin | Fungsi |
|--------|--------|
| `jekyll-feed` | Generate RSS feed |
| `jekyll-paginate` | Paginasi halaman |
| `jekyll-seo-tag` | Meta tags SEO otomatis |
| `jekyll-sitemap` | Generate sitemap.xml |

## 🌐 Deployment

### GitHub Pages

1. Push ke branch `main` atau `gh-pages`
2. Aktifkan GitHub Pages di Settings repository
3. Situs akan live di `https://username.github.io/repo-name`

### Netlify / Vercel

1. Connect repository
2. Build command: `bundle exec jekyll build`
3. Publish directory: `_site`

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## 📄 Lisensi

MIT License - Bebas digunakan untuk proyek pribadi maupun komersial.

---

**HI Spatial** - *Belajar Geospatial Jadi Mudah* 🌍
