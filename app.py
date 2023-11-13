import io
import traceback

import gradio as gr
from fastapi import FastAPI, File, UploadFile, HTTPException

from config import *
from models.detector import YoloDetector
from PIL import Image

app = FastAPI()
detector = YoloDetector(
    model_weights_path=MODEL_PATH,
    confidence_threshold=YOLO_CONF_THRESHOLD,
    iou_threshold=YOLO_IOU_THRESHOLD,
    device=YOLO_DEVICE,
)


@app.post("/recognize")
async def recognize(image: UploadFile = File(...)):
    try:
        image_stream = io.BytesIO(image.file.read())
        image = Image.open(image_stream)
        process_result = detector.predict(image=image)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": str(e), "traceback": traceback.format_exc()},
        )

    return process_result


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


demo = gr.Interface(detector.predict, gr.Image(), "text")
app = gr.mount_gradio_app(app, demo, path="/")
