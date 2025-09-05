#fastapi endpoints 
from fastapi import FastAPI, UploadFile
from yolo_inference import run_yolo
from NLP import make_story
from forecast import forecast_wildlife
from gee_ndvi import compute_ndvi_change

app = FastAPI()

@app.post("/detect/")
async def detect(file: UploadFile):
    results = run_yolo(file.file)
    story = make_story(results)
    return {"detections": results, "story": story}

@app.get("/forecast/")
def forecast():
    return forecast_wildlife()

@app.get("/ndvi/")
def ndvi():
    change, url = compute_ndvi_change()
    return {"ndvi_change": change, "map_url": url}

