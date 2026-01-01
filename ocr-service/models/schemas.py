from pydantic import BaseModel, Field
from typing import List, Optional, Tuple

class OCRRequest(BaseModel):
    file: bytes = Field(..., description="上傳圖片檔案的二進位內容")

class OCRResult(BaseModel):
    text: str
    confidence: float
    bbox: List[List[Tuple[float, float]]]  # easyocr: 每個 bbox 是四個點的座標
    processing_time: float

class HealthResponse(BaseModel):
    status: str
    paddleocr: Optional[str]
    uptime: Optional[str]

class MetricsResponse(BaseModel):
    ocr_requests_total: int
    ocr_processing_time_seconds: float

class ErrorResponse(BaseModel):
    detail: str
    code: int
