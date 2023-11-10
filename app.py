import json
import traceback

from config import *

from flask import Flask, Response, request, render_template
from models.detector import YoloDetector
from PIL import Image

app = Flask("LogCounter-api")
detector = YoloDetector(
    model_weights_path=MODEL_PATH,
    confidence_threshold=YOLO_CONF_THRESHOLD,
    iou_threshold=YOLO_IOU_THRESHOLD,
    device=YOLO_DEVICE,
)


@app.route("/")
def index():
    # There will be a web form here to test the model from the browser
    return render_template("index.html")


@app.route("/recognize", methods=["POST"])
def recognize():
    if request.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        return Response(mimetype="application/json", status=400)

    img_as_byte = request.data

    try:
        pass
        process_result = detector.predict(img_as_byte)
    except Exception as e:
        return Response(
            json.dumps({"error": str(e), "traceback": traceback.format_exc()}),
            mimetype="application/json",
            status=500,
        )
    result = json.dumps(process_result)
    return Response(result, mimetype="application/json", status=200)


@app.route("/healthcheck")
def healthcheck():
    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=FLASK_PORT, debug=FLASK_DEBUG)
