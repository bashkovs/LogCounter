import io
import json

from typing import Dict

import numpy as np
import supervision as sv

from PIL import Image
from ultralytics import YOLO

COLORS = sv.ColorPalette.default()


class YoloDetector:
    def __init__(
        self,
        model_weights_path: str,
        confidence_threshold: float = 0.3,
        iou_threshold: float = 0.7,
        device: str = "cpu",
        draw_contours: bool = False,
    ) -> None:
        self.model = YOLO(model_weights_path)
        self.box_annotator = sv.BoxAnnotator(color=COLORS.colors[1])
        self.device = device
        self.conf_threshold = confidence_threshold
        self.iou_threshold = iou_threshold
        self.draw_contours = draw_contours

    def predict(self, image: bytes, return_image: bool = False) -> Dict:
        # print(type(image))
        if type(image) == bytes:
            image_stream = io.BytesIO(image)
            image = Image.open(image_stream)

        result = self.model(
            image,
            verbose=False,
            conf=self.conf_threshold,
            iou=self.iou_threshold,
            device=self.device,
        )[0]

        detections = sv.Detections.from_ultralytics(result)
        detections = self.sorting_detections(detections=detections)
        if return_image:
            return self.annotate_image(image=np.array(image), detections=detections)
        else:
            return self.formatting_response(detections)

    def formatting_response(self, detections: sv.Detections) -> Dict:
        response = {}
        response["total"] = len(detections.xyxy)

        converted_detections = {}
        for id, xyxy in enumerate(detections.xyxy):
            xyxy = [int(coord) for coord in xyxy]
            xyxyxyxy = [
                [xyxy[0], xyxy[1]],
                [xyxy[2], xyxy[1]],
                [xyxy[0], xyxy[3]],
                [xyxy[2], xyxy[3]],
            ]
            converted_detections[id] = xyxyxyxy

        response["detections"] = converted_detections
        return json.dumps(response)

    def sorting_detections(self, detections: sv.Detections) -> sv.Detections:
        top_left_corners = detections.xyxy[:, :2]
        sorted_indices = np.lexsort((top_left_corners[:, 1], top_left_corners[:, 0]))
        detections.xyxy = detections.xyxy[sorted_indices]
        return detections

    def annotate_image(self, image: np.ndarray, detections: sv.Detections) -> bytes:
        if self.draw_contours:
            annotated_image = self.box_annotator.annotate(
                scene=image.copy(), detections=detections, skip_label=True
            )
        else:
            annotated_image = image.copy()

        for id, xyxy in enumerate(detections.xyxy):
            xyxyxyxy = np.array(
                [xyxy[0], xyxy[1], xyxy[2], xyxy[1], xyxy[0], xyxy[3], xyxy[2], xyxy[3]]
            ).reshape((4, 2))

            polygon_center = sv.get_polygon_center(polygon=xyxyxyxy)
            text_anchor = sv.Point(x=polygon_center.x, y=polygon_center.y)

            annotated_image = sv.draw_text(
                scene=annotated_image,
                text=str(id + 1),
                text_anchor=text_anchor,
                text_scale=0.5,
                text_thickness=1,
                text_padding=5,
                background_color=COLORS.colors[5],
            )
        # print(type(annotated_image.tobytes()))
        return annotated_image.tobytes()


if __name__ == "__main__":
    from PIL import Image

    img_path = "test_image.jpeg"
    model = YoloDetector("../weights/best_yolov8m.pt")
    image = open(img_path, "rb").read()
    response = model.predict(image)
    print(response)
