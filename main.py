import traceback

import gradio as gr
from fastapi import FastAPI, Request, File, UploadFile, HTTPException

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


@app.post("/recognize/")
async def recognize(image: UploadFile):
    try:
        process_result = detector.predict(image=Image.open(image.file))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={"error": str(e), "traceback": traceback.format_exc()},
        )
    return process_result


@app.get("/healthcheck/")
async def healthcheck():
    return {"status": "ok"}


logo_URL = "https://i.ibb.co/LNmGNWR/banner.jpg"
description = "<center> <img src= {} width=100%></center>".format(logo_URL)
demo = gr.Interface(
    fn=lambda img: detector.predict(img, demo=True),
    inputs=gr.Image(type="pil", sources=["upload", "clipboard"]),
    outputs=[gr.Image(), gr.Textbox()],
    examples=[
        ["tests/test_image_1.jpeg"],
        ["tests/test_image_2.jpg"],
        ["tests/test_image_3.jpg"],
        ["tests/test_image_4.jpg"],
        ["tests/test_image_5.jpg"],
    ],
    allow_flagging="never",
    theme=gr.themes.Base(),
    description=description,
)
app = gr.mount_gradio_app(app, demo, path="/")
