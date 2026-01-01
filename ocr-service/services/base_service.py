from abc import ABC, abstractmethod
from typing import Any

class BaseOCRService(ABC):
    @abstractmethod
    def predict(self, image: Any) -> dict:
        """
        執行 OCR 預測，回傳辨識結果 dict
        """
        pass
