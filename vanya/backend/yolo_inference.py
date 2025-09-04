#yolo model calling

from ultralytics import YOLO
import cv2
import tempfile

model = YOLO("yolov8n.pt")  # pretrained; replace with fine-tuned weights

def run_yolo(file_obj):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(file_obj.read())
        tmp_path = tmp.name

    results = model(tmp_path)
    detections = []
    for r in results[0].boxes:
        cls = model.names[int(r.cls)]
        conf = float(r.conf)
        xyxy = r.xyxy.tolist()
        detections.append({"class": cls, "conf": conf, "bbox": xyxy})
    return detections
