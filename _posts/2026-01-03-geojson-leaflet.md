---
title: "Menampilkan Data GeoJSON pada Peta Leaflet"
date: 2026-01-03 10:00:00 +0700
categories: [Tutorial, Leaflet, GeoJSON]
description: "Pelajari cara memuat dan menampilkan data GeoJSON pada peta Leaflet dengan styling custom."
author: HI Spatial
---

GeoJSON adalah format standar untuk merepresentasikan data geografis dalam format JSON. Dalam tutorial ini, kita akan mempelajari cara menampilkan data GeoJSON pada peta Leaflet.

## Apa itu GeoJSON?

GeoJSON mendukung berbagai tipe geometri:

- **Point**: Titik koordinat tunggal
- **LineString**: Garis dengan beberapa titik
- **Polygon**: Area dengan batas tertutup
- **MultiPoint, MultiLineString, MultiPolygon**: Koleksi geometri

## Contoh Data GeoJSON

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "name": "Monas",
        "category": "landmark"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [106.8272, -6.1754]
      }
    }
  ]
}
```

## Menampilkan GeoJSON di Leaflet

```javascript
// Data GeoJSON
const geojsonData = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "Area A" },
      "geometry": {
        "type": "Polygon",
        "coordinates": [[
          [106.82, -6.18],
          [106.84, -6.18],
          [106.84, -6.16],
          [106.82, -6.16],
          [106.82, -6.18]
        ]]
      }
    }
  ]
};

// Tambahkan ke peta
L.geoJSON(geojsonData).addTo(map);
```

## Styling GeoJSON

Anda dapat memberikan style custom pada fitur GeoJSON:

```javascript
L.geoJSON(geojsonData, {
  style: function(feature) {
    return {
      color: '#333',
      weight: 2,
      fillColor: '#3388ff',
      fillOpacity: 0.5
    };
  }
}).addTo(map);
```

## Popup pada Fitur

Tambahkan popup yang menampilkan properties dari setiap fitur:

```javascript
L.geoJSON(geojsonData, {
  onEachFeature: function(feature, layer) {
    if (feature.properties && feature.properties.name) {
      layer.bindPopup(feature.properties.name);
    }
  }
}).addTo(map);
```

## Load GeoJSON dari File Eksternal

Untuk memuat GeoJSON dari file eksternal:

```javascript
fetch('data/wilayah.geojson')
  .then(response => response.json())
  .then(data => {
    L.geoJSON(data).addTo(map);
  });
```

## Kesimpulan

GeoJSON adalah format yang sangat fleksibel untuk data spasial. Dengan Leaflet, Anda dapat dengan mudah menampilkan dan styling data GeoJSON sesuai kebutuhan.

Tutorial selanjutnya akan membahas tentang menggunakan data dari Web Map Service (WMS).
