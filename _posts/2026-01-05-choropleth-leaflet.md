---
title: "Membuat Peta Choropleth dengan Leaflet"
date: 2026-01-05 10:00:00 +0700
categories: [Tutorial, Leaflet, Visualisasi]
description: "Tutorial membuat peta choropleth untuk visualisasi data statistik per wilayah menggunakan Leaflet."
author: HI Spatial
---

Peta choropleth adalah jenis peta tematik yang menggunakan warna untuk merepresentasikan nilai data pada area geografis. Tutorial ini akan memandu Anda membuat peta choropleth dengan Leaflet.

## Kapan Menggunakan Peta Choropleth?

Peta choropleth cocok untuk menampilkan:
- Kepadatan penduduk per wilayah
- Tingkat pengangguran per provinsi
- Hasil pemilu per kabupaten
- Data statistik lainnya yang terikat area

## Persiapan Data

Anda memerlukan:
1. Data GeoJSON dengan geometri wilayah
2. Data statistik untuk setiap wilayah

```javascript
// Contoh struktur data
const provinces = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "name": "DKI Jakarta",
        "population": 10562088,
        "density": 15900
      },
      "geometry": { /* ... */ }
    }
  ]
};
```

## Membuat Skala Warna

Tentukan fungsi untuk menghasilkan warna berdasarkan nilai:

```javascript
function getColor(density) {
  return density > 10000 ? '#800026' :
         density > 5000  ? '#BD0026' :
         density > 2000  ? '#E31A1C' :
         density > 1000  ? '#FC4E2A' :
         density > 500   ? '#FD8D3C' :
         density > 200   ? '#FEB24C' :
         density > 100   ? '#FED976' :
                          '#FFEDA0';
}
```

## Styling Fitur

Terapkan warna berdasarkan data:

```javascript
function style(feature) {
  return {
    fillColor: getColor(feature.properties.density),
    weight: 2,
    opacity: 1,
    color: 'white',
    dashArray: '3',
    fillOpacity: 0.7
  };
}

L.geoJSON(provinces, { style: style }).addTo(map);
```

## Menambahkan Interaksi

Buat peta lebih interaktif dengan highlight dan info:

```javascript
function highlightFeature(e) {
  const layer = e.target;
  layer.setStyle({
    weight: 5,
    color: '#666',
    dashArray: '',
    fillOpacity: 0.7
  });
  layer.bringToFront();
}

function resetHighlight(e) {
  geojson.resetStyle(e.target);
}

function onEachFeature(feature, layer) {
  layer.on({
    mouseover: highlightFeature,
    mouseout: resetHighlight,
    click: zoomToFeature
  });
}
```

## Menambahkan Legend

Buat legend untuk membantu pembaca memahami peta:

```javascript
const legend = L.control({ position: 'bottomright' });

legend.onAdd = function(map) {
  const div = L.DomUtil.create('div', 'info legend');
  const grades = [0, 100, 200, 500, 1000, 2000, 5000, 10000];

  for (let i = 0; i < grades.length; i++) {
    div.innerHTML +=
      '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
      grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
  }
  return div;
};

legend.addTo(map);
```

## Tips untuk Choropleth yang Baik

1. **Pilih skala warna yang sesuai** - sequential untuk data kontinu, diverging untuk data dengan nilai tengah yang bermakna
2. **Normalisasi data** - gunakan density bukan nilai absolut
3. **Klasifikasi yang tepat** - natural breaks, quantile, atau equal interval
4. **Sediakan legend yang jelas**

## Kesimpulan

Peta choropleth adalah tools visualisasi yang powerful untuk menampilkan data statistik. Dengan Leaflet, Anda dapat membuat peta choropleth interaktif yang informatif.

Selamat mencoba!
