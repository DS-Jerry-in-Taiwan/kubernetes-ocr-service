# Kubernetes OCR Service 🐳☸️

Multi-Agent 開發專案 | FastAPI + PaddleOCR + Kubernetes

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10-green)]

---

## 🎯 專案概述

本專案為生產級 OCR 服務，部署於 3 節點 Kubernetes 叢集，展示 MLOps 最佳實踐、雲原生架構與 Multi-Agent 協作開發。  
核心功能包含中英文 OCR 辨識（PaddleOCR 2.7+）、RESTful API（FastAPI）、Kubernetes 部署（containerd + Calico）、自動擴展與故障恢復。  
專案強調結構規範、技術選型明確、履歷展示價值高，適合 DevOps/MLOps/AI 團隊協作與履歷加分。

---

## 🏗️ Multi-Agent 團隊

| Agent    | 角色           | 任務說明                                 |
|----------|----------------|------------------------------------------|
| @ARCH    | 架構師         | 專案結構、技術選型、文檔規範             |
| @INFRA   | 維運工程師     | Docker、K8s 配置、部署腳本               |
| @CODER   | 開發工程師     | FastAPI、PaddleOCR 實作                  |
| @ANALYST | 品質工程師     | 測試、效能監控、驗證                     |

---

## 🚀 快速開始

```bash
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
```

---

## 🏗️ 系統架構

```
[Client] → [NodePort:30080] → [Service] → [Deployment:3 Pods]
                                    ↓
                           [OCR Service] ← [PaddleOCR]
                                    ↓
                              [containerd]
```

---

## 📊 效能指標

| 指標         | 目標值      |
|--------------|-------------|
| OCR 準確度   | > 85%       |
| API 延遲     | < 500ms     |
| CPU 使用率   | < 60%       |
| Pod 可用性   | > 99%       |

---

## 📚 文檔

- [API 規格](docs/api_spec.md)
- [系統架構](docs/architecture.md)
- [部署手冊](docs/workflows/deploy.md)
- [Agent Context](docs/agent_context/)

---

## 🛠️ 技術亮點

- FastAPI 高效能 RESTful API
- PaddleOCR 支援多語言文字辨識
- Kubernetes 叢集自動擴展
- 容器化部署，支援 CI/CD
- Prometheus 監控與 Grafana 視覺化
- 多 Agent 協作開發流程

---

## 💡 使用案例

- 財務發票自動辨識
- 合約文件批次 OCR
- 圖片批量文字擷取
- 雲端 API 服務整合

---

## 📝 FAQ

**Q: 如何更換 OCR 模型？**  
A: 請參考 ocr-service/models/ 目錄，替換 PaddleOCR 欲用模型。

**Q: 如何擴展 API？**  
A: 於 ocr-service/services/ 新增 FastAPI 路由，並更新 api_spec.md。

**Q: 如何進行壓力測試？**  
A: 使用 test/performance/ 目錄內腳本，搭配 pytest 或 locust。

---

## 🧩 目錄結構預覽

```
kubernetes-ocr-service/
├── README.md
├── docs/
│   ├── api_spec.md
│   ├── architecture.md
│   ├── workflows/
│   └── agent_context/
├── ocr-service/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── tests/
├── k8s/
├── scripts/
│   └── validate_phase0.sh
├── test/
│   ├── functional/
│   ├── performance/
│   ├── chaos/
│   ├── reports/
│   └── test_images/
└── .gitignore
```

---

## 🏆 履歷價值

此專案展示：

- ✅ Kubernetes 生產部署經驗
- ✅ FastAPI + PaddleOCR 整合
- ✅ Multi-Agent 協作開發
- ✅ 端到端 MLOps 實作
- ✅ 效能優化與監控
- ✅ DevOps 流程規範
- ✅ 雲原生架構設計

---

## 📢 聯絡方式

如有問題或合作需求，請聯絡專案負責人：  
Email: ocr-team@example.com

