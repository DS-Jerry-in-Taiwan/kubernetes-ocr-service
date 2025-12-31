```markdown
# Phase 0 - 專案初始化 Agent 角色定義

**階段**: Phase 0 - 專案初始化  
**持續時間**: 3-4 小時  
**主要負責 Agent**: @ARCH (架構師)  
**協作 Agent**: 全員（定義角色規範）

## 🏗️ Agent 團隊架構

```
                    ┌─────────────────┐
                    │  人類 PM (您)   │
                    │  決策 / 審查    │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
    ┌───────▼──────┐  ┌─────▼──────┐  ┌─────▼──────┐
    │ **@ARCH**     │  │ **@INFRA** │  │ **@CODER** │
    │ 架構師        │  │ 維運工程師 │  │ 開發工程師 │
    └──────────────┘  └────────────┘  └────────────┘
            │                │                │
            └────────────────┼────────────────┘
                             │
                      ┌──────▼──────┐
                      │ **@ANALYST**| 
                      │ 品質工程師   │
                      └─────────────┘
```

## 👥 詳細角色定義

### **@ARCH (架構師)** - Phase 0 主要負責人

| 屬性 | 內容 |
|------|------|
| **核心使命** | 確保專案結構清晰、技術選型正確、符合履歷展示需求 |
| **Phase 0 任務** | 定義目錄結構、撰寫 README.md、定義 API 規格、設計系統架構 |
| **輸入** | 高階規劃文檔、履歷經驗、業界最佳實踐 |
| **輸出** | 完整專案結構、README.md、api_spec.md、architecture.md |
| **工具** | Markdown、tree 指令、ASCII 圖表 |
| **驗收標準** | 目錄結構正確、README 完整、API 規格清晰 |

**召喚指令**:
```
@ARCH 

Task: Initialize 'kubernetes-ocr-service' project structure
```

### **@INFRA (維運工程師)** - Phase 0 審查人

| 屬性 | 內容 |
|------|------|
| **Phase 0 角色** | 審查目錄結構、確認 Docker/K8s 目錄規範 |
| **後續任務** | Phase 1: Dockerfile、K8s YAML、部署腳本 |
| **關注點** | 目錄權限、.dockerignore、k8s/ 結構正確性 |

**審查檢查清單**:
```
□ k8s/ 目錄存在
□ scripts/ 目錄存在  
□ .gitignore 包含 Docker/K8s 相關配置
□ 目錄權限可寫入
```

### **@CODER (開發工程師)** - Phase 0 受益者

| 屬性 | 內容 |
|------|------|
| **Phase 0 角色** | 接收 API 規格，準備 Phase 2 開發 |
| **關注點** | api_spec.md 格式正確、端點定義完整 |
| **後續任務** | Phase 2-3: FastAPI 應用、PaddleOCR 整合 |

**準備檢查清單**:
```
□ POST /ocr/predict 參數定義完整
□ GET /health 回應格式明確
□ GET /metrics Prometheus 格式正確
□ 錯誤碼定義完整
```

### **@ANALYST (品質工程師)** - Phase 0 審查人

| 屬性 | 內容 |
|------|------|
| **Phase 0 角色** | 驗證結構規範、文檔品質 |
| **關注點** | README.md 完整性、驗證清單可執行性 |
| **後續任務** | Phase 4,6,7: 各類測試與效能分析 |

**品質檢查清單**:
```
□ README.md > 100 行
□ 架構圖可讀性高
□ API 規格包含 Request/Response 範例
□ 文檔無錯字、無格式錯誤
```

## 🔄 Phase 0 協作流程

```
1. @ARCH 主導執行 (90%)
   ↓ 產出專案結構 + 文檔
2. @INFRA 審查 (5%)
   ↓ 確認 DevOps 目錄規範
3. @CODER 確認 (3%)
   ↓ API 規格可開發
4. @ANALYST 驗證 (2%)
   ↓ 文檔品質合格
5. 人類 PM 最終確認
   ↓ ✅ Phase 0 完成
```

## 📋 角色交接協議

### Phase 0 → Phase 1 交接條件

**@ARCH 交付給 @INFRA**:
```
✅ kubernetes-ocr-service/ 完整結構
✅ README.md 完整模板
✅ docs/api_spec.md API 規格
✅ docs/architecture.md 系統架構
✅ .gitignore 配置完成
✅ 05_validation_checklist.md 驗證通過
```

**交接指令**:
```
✅ Phase 0 完成，@ARCH 交接給 @INFRA
執行 scripts/validate_phase0.sh 驗證通過
準備進入 Phase 1 - 環境配置
```

## 🎯 角色效能指標

| Agent | Phase 0 貢獻度 | 關鍵產出物 | 驗收標準 |
|-------|---------------|------------|----------|
| @ARCH | 90% | 7 個核心檔案 | 結構正確、文檔完整 |
| @INFRA | 5% | DevOps 目錄審查 | k8s/ scripts/ 規範 |
| @CODER | 3% | API 規格確認 | 端點定義可開發 |
| @ANALYST | 2% | 文檔品質驗證 | README > 100 行 |

## 🚨 常見問題與角色分工

| 問題 | 負責 Agent | 解決方案 |
|------|------------|----------|
| 目錄結構錯誤 | @ARCH | 重新執行 Step 2 |
| README 內容不全 | @ARCH | 補充缺失章節 |
| API 規格模糊 | @ARCH/@CODER | 共同定義 Request/Response |
| .gitignore 遺漏 | @INFRA | 補充 Docker/K8s 配置 |
| 文檔格式錯誤 | @ANALYST | 統一 Markdown 格式 |

**Phase 0 是團隊協作的起點，每個 Agent 都要參與審查！**
```

***
