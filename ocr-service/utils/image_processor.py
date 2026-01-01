import cv2
import numpy as np
from PIL import Image
from typing import Union

class ImageProcessor:
    @staticmethod
    def read_image(file: Union[bytes, str]) -> np.ndarray:
        """將 bytes 或檔案路徑轉為 OpenCV 圖片陣列"""
        if isinstance(file, bytes):
            img_array = np.frombuffer(file, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        else:
            img = cv2.imread(file)
        return img

    @staticmethod
    def to_gray(img: np.ndarray) -> np.ndarray:
        """轉為灰階"""
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def resize(img: np.ndarray, size=(640, 640)) -> np.ndarray:
        """resize 圖片"""
        return cv2.resize(img, size)

    @staticmethod
    def pil_to_cv(img: Image.Image) -> np.ndarray:
        """Pillow 轉 OpenCV"""
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
