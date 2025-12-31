檔案: docs/agent_context/phase0/02_dev_flow_context.md

text
# Phase 0 - 專案初始化 開發流程

**階段**: Phase 0 - 專案初始化  
**持續時間**: 3-4 小時  
**負責 Agent**: @ARCH (架構師)  
**執行模式**: 混合模式

## 🔄 執行流程圖

Step 1: 環境檢查與專案初始化
↓
Step 2: 建立核心目錄結構
↓
Step 3: 建立 README.md 模板
↓
Step 4: 定義 API 規格 (api_spec.md)
↓
Step 5: 設計系統架構 (architecture.md)
↓
Step 6: 配置 .gitignore 與基礎檔案
↓
Step 7: 自動驗證 (05_validation_checklist.md)
↓
✅ Phase 0 完成 → 交接給 Phase 1 (@INFRA)

text

## 📋 詳細執行步驟

### Step 1: 環境檢查 (5 分鐘)
確認專案根目錄
pwd
ls -la

確認不存在衝突檔案
[ ! -d "kubernetes-ocr-service" ] && echo "✅ 根目錄乾淨"

text

### Step 2: 建立核心目錄結構 (10 分鐘)
mkdir -p kubernetes-ocr-service/{docs,ocr-service,k8s,scripts,test}
cd kubernetes-ocr-service
mkdir -p docs/{workflows,agent_context}
mkdir -p ocr-service/{services,models,utils,tests}
mkdir -p test/{functional,performance,chaos,reports}
mkdir -p test/test_images
tree . # 或 ls -R

text

**預期輸出**:
kubernetes-ocr-service/
├── docs/
├── k8s/
├── ocr-service/
│ ├── services/
│ ├── models/
│ ├── utils/
│ └── tests/
├── scripts/
└── test/
├── functional/
├── performance/
├── chaos/
├── reports/
└── test_images/

text

### Step 3: 建立 README.md 模板 (30 分鐘)
cd kubernetes-ocr-service
cat > README.md << 'EOF'

Kubernetes OCR Service 🐳☸️
Multi-Agent 開發專案 | FastAPI + PaddleOCR + Kubernetes

[![License](https://img.shields.io/badge/license-MIT-blue![Python](https://img.shields.io/badge/python-3.10-green## 🎯 專案概述

生產級 OCR 服務，部署於 3 節點 Kubernetes 叢集，展示：

MLOps 最佳實踐

雲原生架構

Multi-Agent 協作開發

核心功能:

中英文 OCR 辨識 (PaddleOCR 2.7+)

RESTful API (FastAPI)

Kubernetes 部署 (containerd + Calico)

自動擴展與故障恢復

🏗️ Multi-Agent 團隊
Agent	角色	職責
@ARCH	架構師	專案結構、技術選型
@INFRA	維運工程師	Docker、K8s 配置
@CODER	開發工程師	FastAPI、PaddleOCR
@ANALYST	品質工程師	測試、效能監控
🚀 快速開始
bash
# 1. 克隆專案
git clone <repo-url>
cd kubernetes-ocr-service

# 2. 本地開發
cd ocr-service
docker-compose up

# 3. Kubernetes 部署
./scripts/deploy.sh

# 4. 測試 API
curl -X POST http://<node-ip>:30080/ocr/predict -F "file=@test/test_images/invoice.jpg"
🏗️ 系統架構
text
[Client] → [NodePort:30080] → [Service] → [Deployment:3 Pods]
                                    ↓
                           [OCR Service] ← [PaddleOCR]
                                    ↓
                              [containerd]
📊 效能指標
指標	目標值
OCR 準確度	> 85%
API 延遲	< 500ms
CPU 使用率	< 60%
Pod 可用性	> 99%
📚 文檔
API 規格

系統架構

部署手冊

🏆 履歷價值
此專案展示：

text
✅ Kubernetes 生產部署經驗
✅ FastAPI + PaddleOCR 整合
✅ Multi-Agent 協作開發
✅ 端到端 MLOps 實作
✅ 效能優化與監控
EOF

text

### Step 4: 定義 API 規格 (30 分鐘)
cat > docs/api_spec.md << 'EOF'

API 規格定義
POST /ocr/predict
上傳圖片進行 OCR 辨識

Request
text
Content-Type: multipart/form-data

file: <image file> (JPEG/PNG, max 10MB)
Response
json
{
  "success": true,
  "data": {
    "text": "辨識結果",
    "confidence": 0.92,
    "bbox": [[x1,y1],[x2,y2]],
    "processing_time": 0.347
  }
}
GET /health
健康檢查

Response
json
{
  "status": "healthy",
  "paddleocr": "ready",
  "uptime": "2h30m"
}
GET /metrics
Prometheus 監控指標

text
ocr_requests_total{status="success"} 1234
ocr_processing_time_seconds 0.347
EOF

text

### Step 5: 設計系統架構 (30 分鐘)
cat > docs/architecture.md << 'EOF'

系統架構設計
高階架構圖
text
                    ┌─────────────────┐
                    │     Client      │
                    │   (curl/Postman)│
                    └─────────┬───────┘
                              │ HTTP
                ┌─────────────▼────────┐
                │   NodePort 30080     │
                │     (K8s Service)    │
                └─────────┬───────┘
                          │
┌─────────────────────────▼─────────────────┐
│            Kubernetes Cluster             │
│  ┌─────────────┐ ┌─────────────┐         │
│  │   Master    │ │   Worker1   │         │
│  │             │ │   Pod1      │         │
│  └─────────────┘ └──────┬──────┘         │
│                         │                │
│  ┌─────────────┐ ┌──────▼──────┐         │
│  │   Worker2   │ │   Pod2      │         │
│  │   Pod3      │ │             │         │
│  └─────────────┘ └─────────────┘         │
└──────────────────────────────────────────┘
                          │
                 ┌────────▼────────┐
                 │  OCR Service    │ ← PaddleOCR
                 │  (FastAPI)      │
                 └─────────────────┘
技術棧
層級	技術	版本
API Framework	FastAPI	0.104+
OCR Engine	PaddleOCR	2.7+
Container Runtime	containerd	1.7+
CNI	Calico	3.26+
Python	3.10	slim
EOF

text

### Step 6: 配置 .gitignore (10 分鐘)
cat > .gitignore << 'EOF

Python
pycache/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt

Docker
.dockerignore
Dockerfile*
docker-compose*
.docker/

Kubernetes
k8s/.log
k8s/.yaml.bak

Logs
*.log
logs/

IDE
.vscode/
.idea/
*.swp
*.swo

OS
.DS_Store
Thumbs.db

Test
.pytest_cache/
.coverage
htmlcov/
EOF

text

### Step 7: 最終驗證 (15 分鐘)
執行 `05_validation_checklist.md` 中的自動驗證腳本。

## ⏱️ 時間分配

| 步驟 | 預估時間 | 負責工作 |
|------|----------|----------|
| Step 1 | 5 分鐘 | 環境檢查 |
| Step 2 | 10 分鐘 | 目錄結構 |
| Step 3 | 30 分鐘 | README.md |
| Step 4 | 30 分鐘 | API 規格 |
| Step 5 | 30 分鐘 | 系統架構 |
| Step 6 | 10 分鐘 | .gitignore |
| Step 7 | 15 分鐘 | 最終驗證 |
| **總計** | **2.5 小時** | |

## 🔄 交接條件

Phase 0 完成後，@INFRA 接收以下檔案：
- `kubernetes-ocr-service/` 完整目錄結構
- `README.md` 完整模板
- `docs/api_spec.md` API 規格
- `docs/architecture.md` 系統架構
- `.gitignore` 配置完成

**交接指令**:
✅ Phase 0 完成，交接給 @INFRA 執行 Phase 1

