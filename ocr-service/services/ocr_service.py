import easyocr
from .base_service import BaseOCRService

class OCRService(BaseOCRService):
    def __init__(self, lang=["ch_sim"]):
        self.reader = easyocr.Reader(lang, gpu=True)

    def predict(self, image):
        result = self.reader.readtext(image)
        texts = []
        bboxes = []
        confidences = []
        for bbox, text, conf in result:
            texts.append(text)
            confidences.append(conf)
            bboxes.append(bbox)
        return {
            "text": "\n".join(texts),
            "confidence": float(sum(confidences) / len(confidences)) if confidences else 0.0,
            "bbox": bboxes,
        }
