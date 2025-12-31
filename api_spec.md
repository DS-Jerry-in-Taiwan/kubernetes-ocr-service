# API 規格定義

## POST /ocr/predict
上傳圖片進行 OCR 辨識

**Request**
- Content-Type: multipart/form-data
- file: <image file> (JPEG/PNG, max 10MB)

**Response**
```json
{
  "success": true,
  "data": {
    "text": "辨識結果",
    "confidence": 0.92,
    "bbox": [[100,200],[300,400]],
    "processing_time": 0.347
  }
}
```

## GET /health
健康檢查

**Response**
```json
{
  "status": "healthy",
  "paddleocr": "ready",
  "uptime": "2h30m"
}
```

## GET /metrics
Prometheus 監控指標

**Response**
```
ocr_requests_total{status="success"} 1234
ocr_processing_time_seconds 0.347
```
