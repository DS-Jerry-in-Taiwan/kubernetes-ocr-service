# Phase 0 - 專案初始化 Agent Prompt 模板

**階段**: Phase 0 - 專案初始化  
**負責 Agent**: @ARCH (架構師)  
**用途**: Cline/Claude 中的召喚指令

## 🎯 @ARCH Prompt 模板 (Phase 0 主要執行者)

### 完整啟動指令
你現在是 [@ARCH] 架構師，專案：kubernetes-ocr-service

當前任務: Phase 0 - 專案初始化
執行模式: 混合模式

請閱讀 Phase 0 的 7 份 Context 文件：

docs/agent_context/phase0/01_dev_goal_context.md

docs/agent_context/phase0/02_dev_flow_context.md

docs/agent_context/phase0/03_agent_roles_context.md

docs/agent_context/phase0/04_agent_prompts_context.md

docs/agent_context/phase0/05_validation_checklist.md

docs/agent_context/phase0/06_delivery_record.md

docs/agent_context/phase0/07_checkpoint_protocol.md

立即執行 Step 1-7（參考 02_dev_flow_context.md）：

環境檢查

建立核心目錄結構

建立 README.md 模板

定義 API 規格

設計系統架構

配置 .gitignore

執行自動驗證

產出格式：

text
【@ARCH Phase 0 執行報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 當前步驟: Step X
✅ 完成項目: ...
📁 產出檔案: ...
🔍 驗證結果: ...
👉 下一步: ...
完成後自動執行下一個步驟。

text

## 🔧 細分任務 Prompt

### Task 1: 目錄結構
@ARCH

Task: 建立 kubernetes-ocr-service 完整目錄結構

需求：

遵循 Python Package 最佳實踐

包含 docs/ocr-service/k8s/scripts/test

ocr-service/ 內含 services/models/utils/tests

test/ 內含 functional/performance/chaos/reports/test_images

請提供完整 mkdir 指令序列 + tree 輸出預覽。

text

### Task 2: README.md
@ARCH

Task: 建立 README.md 完整模板

需求：

包含專案概述（100+ 字）

Multi-Agent 團隊介紹（4 個 Agent 表格）

快速開始指南（4 步驟）

系統架構圖（ASCII）

效能指標表格

文檔連結

履歷價值說明

請提供完整 cat > README.md << 'EOF' 指令。

text

### Task 3: API 規格
@ARCH

Task: 定義 docs/api_spec.md

端點規格：

POST /ocr/predict - 上傳圖片，返回辨識結果

GET /health - 健康檢查

GET /metrics - Prometheus 指標

每個端點包含：

Request 格式（multipart/form-data, JSON）

Response 範例（JSON）

錯誤碼定義

參數說明

請提供完整 cat > docs/api_spec.md << 'EOF' 指令。

text

### Task 4: 系統架構
@ARCH

Task: 設計 docs/architecture.md

需求：

高階架構圖（Client → NodePort → K8s → OCR Service）

技術棧表格（FastAPI/PaddleOCR/containerd/Calico）

部署架構說明（3 節點：1 Master + 2 Worker）

資料流程圖

請提供完整 ASCII 架構圖 + Markdown 內容。

text

## 👥 其他 Agent 審查 Prompt

### @INFRA 審查指令
@INFRA

Task: 審查 Phase 0 DevOps 相關配置

檢查項目：

k8s/ scripts/ 目錄存在

.gitignore 包含 Docker/K8s 配置

目錄權限正確

執行以下檢查並回報：
ls -ld k8s/ scripts/
cat .gitignore | grep -E "(docker|k8s)"
find . -type d -perm -755 | head -10

text

### @CODER 確認指令
@CODER

Task: 確認 Phase 0 API 規格可開發性

檢查 docs/api_spec.md：

POST /ocr/predict 參數完整

Response 格式明確（text, confidence, bbox）

錯誤處理定義清晰

FastAPI 可直接實作

請確認規格無歧義，回報：
✅ API 規格可開發
❌ 需要調整：[具體建議]

text

### @ANALYST 驗證指令
@ANALYST

Task: 驗證 Phase 0 文檔品質

檢查清單：

README.md > 100 行：wc -l README.md

架構圖可讀性：視覺檢查

API 規格完整性：3 個端點全定義

Markdown 格式統一：無破圖

執行驗證並回報結果。

text

## 🎯 Prompt 執行順序

@ARCH 啟動完整指令 → 自動執行 Step 1-7

@INFRA 審查 DevOps 配置

@CODER 確認 API 規格

@ANALYST 驗證文檔品質

人類 PM Checkpoint 確認

text

## 📋 Prompt 效能指標

| Prompt 類型 | 預期回應時間 | 成功率目標 |
|-------------|-------------|------------|
| @ARCH 完整指令 | 15-20 分鐘 | 95% |
| 細分任務 | 3-5 分鐘 | 98% |
| @INFRA 審查 | 2 分鐘 | 100% |
| @CODER 確認 | 2 分鐘 | 100% |
| @ANALYST 驗證 | 3 分鐘 | 100% |

## 🚨 常見 Prompt 問題

| 問題 | 解決方案 |
|------|----------|
| Agent 角色混亂 | 明確使用 `@AGENT_NAME` 開頭 |
| 上下文丟失 | 每次 Prompt 重複列出 7 份 Context 文件 |
| 產出不完整 | 使用「請提供完整 cat > filename << 'EOF' 指令」 |
| 驗證失敗 | 執行對應 Agent 的審查指令 |
| 執行順序錯誤 | 嚴格按照「完整啟動 → 審查 → 驗證」順序 |

**複製上方任一 Prompt 即可召喚對應 Agent！**
