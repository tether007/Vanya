import ee, geemap

ee.Initialize(project='vanya-471214')

# AOI (adjust as needed)
aoi = ee.Geometry.Rectangle([77.0, 12.0, 77.8, 12.8])

# Sentinel-2 Harmonized collection
collection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED") \
    .filterBounds(aoi) \
    .filterDate("2025-01-01", "2025-09-01") \
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20))

# Debug: check available bands from the first image
first_img = collection.first()
print("Available bands:", first_img.bandNames().getInfo())

# Median composite
median_img = collection.median()

# NDVI calculation
ndvi = median_img.normalizedDifference(["B8", "B4"]).rename("NDVI")

# Visualization parameters
ndvi_vis = {"min": 0, "max": 1, "palette": ["red", "yellow", "green"]}
rgb_vis = {"bands": ["B4", "B3", "B2"], "min": 0, "max": 3000}  # True-color

# Create interactive map
Map = geemap.Map(center=[12.4, 77.4], zoom=10)

# Add layers
Map.addLayer(median_img, rgb_vis, "Satellite")  # True-color satellite
Map.addLayer(ndvi, ndvi_vis, "NDVI")           # NDVI overlay
Map.addLayer(aoi, {}, "AOI")                   # Polygon overlay

# Add layer control to toggle between them
Map.addLayerControl()

# Export map to HTML
Map.to_html("satellite_ndvi_map.html")
print("✅ Map saved as satellite_ndvi_map.html. Open it in your browser.")
