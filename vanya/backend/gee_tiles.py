# backend/gee_tiles.py
import ee
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

ee.Initialize(project='vanya-471214')

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AOI polygon
AOI = ee.Geometry.Polygon([[
    [77.0, 12.0],
    [77.8, 12.0],
    [77.8, 12.8],
    [77.0, 12.8],
    [77.0, 12.0]
]])

@app.get("/gee-tiles")
def gee_tiles():
    collection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED") \
        .filterBounds(AOI) \
        .filterDate("2025-01-01", "2025-09-01") \
        .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20)) \
        .median()

    # NDVI
    ndvi = collection.normalizedDifference(["B8", "B4"]).rename("NDVI")
    ndvi_vis = {"min": 0, "max": 1, "palette": ["red", "yellow", "green"]}
    ndvi_url = ee.Image(ndvi).getMapId(ndvi_vis)["tile_fetcher"].url_format

    # Satellite True-color
    rgb_vis = {"bands": ["B4","B3","B2"], "min":0, "max":3000}
    rgb_url = ee.Image(collection).getMapId(rgb_vis)["tile_fetcher"].url_format

    return {"ndvi": ndvi_url, "satellite": rgb_url}
