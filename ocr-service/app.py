from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .models.schemas import OCRRequest, OCRResult, HealthResponse, ErrorResponse
from .services.ocr_service import OCRService
from .utils.image_processor import ImageProcessor
from .utils.logger import get_logger
import time

app = FastAPI(title="Kubernetes OCR Service")
logger = get_logger()
ocr_service = OCRService(['en', 'ch_sim'])

@app.get("/health", response_model=HealthResponse)
def health():
    return {"status": "ok", "paddleocr": "ready"}

@app.post("/ocr/predict", response_model=OCRResult, responses={400: {"model": ErrorResponse}})
async def ocr_predict(file: UploadFile = File(...)):
    try:
        content = await file.read()
        img = ImageProcessor.read_image(content)
        if img is None:
            raise ValueError("無法解析圖片")
        start = time.time()
        result = ocr_service.predict(img)
        result["processing_time"] = round(time.time() - start, 3)
        return result
    except Exception as e:
        logger.error(f"OCR 預測失敗: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/metrics")
def metrics():
    # 簡化範例，實際應整合 Prometheus
    return {
        "ocr_requests_total": 0,
        "ocr_processing_time_seconds": 0.0
    }
