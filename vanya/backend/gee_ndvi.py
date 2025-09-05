import ee
ee.Authenticate()
ee.Initialize(project='vanya-471214')

# Example AOI polygon
AOI = ee.Geometry.Polygon([[
    [77.0, 12.0],
    [77.8, 12.0],
    [77.8, 12.8],
    [77.0, 12.8],
    [77.0, 12.0]
]])

def get_ndvi_map_url():
    # Get Sentinel-2 collection
    collection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED") \
        .filterBounds(AOI) \
        .filterDate("2025-01-01", "2025-09-01") \
        .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20))

    first_img = collection.first()
    print("Available bands:", first_img.bandNames().getInfo())

    # Median composite
    median_img = collection.median()

    # Correct NDVI formula (NIR=B8, Red=B4)
    ndvi = median_img.normalizedDifference(["B8","B4"]).rename("NDVI")

    vis_params = {
        "min": 0,
        "max": 1,
        "palette": ["red", "yellow", "green"]
    }

    # Get tile URL
    map_id_dict = ee.Image(ndvi).getMapId(vis_params)
    return map_id_dict["tile_fetcher"].url_format

print("Tile URL:", get_ndvi_map_url())
