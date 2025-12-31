# Phase 0 - 專案初始化 驗證清單

**階段**: Phase 0 - 專案初始化  
**負責驗證**: @ANALYST (品質工程師)  
**自動化腳本**: `scripts/validate_phase0.sh`

## ✅ 自動驗證腳本

執行以下指令驗證 Phase 0 完成度：

```bash
#!/bin/bash
# scripts/validate_phase0.sh

echo "【Phase 0 驗證】專案初始化"
cd kubernetes-ocr-service

# 1. 檢查核心目錄結構 (10 個必須目錄)
echo "→ 檢查目錄結構..."
REQUIRED_DIRS=(
    "docs" "ocr-service" "k8s" "scripts" "test"
    "ocr-service/services" "ocr-service/models" 
    "ocr-service/utils" "ocr-service/tests"
    "test/functional" "test/performance" "test/chaos" 
    "test/reports" "test/test_images"
)

PASS=0
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir 存在"
        ((PASS++))
    else
        echo "❌ $dir 缺失"
    fi
done

if [ $PASS -eq ${#REQUIRED_DIRS[@]} ]; then
    echo "✅ 目錄結構完整 (100%)"
else
    echo "❌ 目錄結構不完整 (${PASS}/${#REQUIRED_DIRS[@]})"
    exit 1
fi

# 2. 檢查核心檔案
echo "→ 檢查核心檔案..."
CORE_FILES=("README.md" "docs/api_spec.md" "docs/architecture.md" ".gitignore")
for file in "${CORE_FILES[@]}"; do
    if [ -f "$file" ] && [ -s "$file" ]; then
        LINES=$(wc -l < "$file")
        echo "✅ $file (${LINES} 行)"
    else
        echo "❌ $file 缺失或空白"
        exit 1
    fi
done

# 3. README.md 品質檢查
README_LINES=$(wc -l < README.md)
if [ $README_LINES -gt 100 ]; then
    echo "✅ README.md 完整 (${README_LINES} 行 > 100)"
else
    echo "❌ README.md 過短 (${README_LINES} 行)"
    exit 1
fi

# 4. API 規格檢查
API_ENDPOINTS=$(grep -c "^## " docs/api_spec.md)
if [ $API_ENDPOINTS -ge 3 ]; then
    echo "✅ API 規格完整 (${API_ENDPOINTS} 個端點)"
else
    echo "❌ API 端點不足 (${API_ENDPOINTS}/3)"
    exit 1
fi

# 5. 架構圖檢查
ARCH_ASCII=$(grep -c "│\|┌\|└\|─" docs/architecture.md)
if [ $ARCH_ASCII -gt 10 ]; then
    echo "✅ 架構圖完整 (${ARCH_ASCII} 個 ASCII 元素)"
else
    echo "❌ 架構圖缺失"
    exit 1
fi

# 6. .gitignore 檢查
GITIGNORE_DOCKER=$(grep -c "docker" .gitignore || true)
GITIGNORE_PYTHON=$(grep -c "pycache" .gitignore || true)
if [ $GITIGNORE_DOCKER -gt 0 ] && [ $GITIGNORE_PYTHON -gt 0 ]; then
    echo "✅ .gitignore 配置完整"
else
    echo "❌ .gitignore 配置不全"
    exit 1
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "【✅ Phase 0 驗證通過 100%】"
echo "📁 總檔案數: $(find . -type f | wc -l)"
echo "📂 總目錄數: $(find . -type d | wc -l)"
echo "👉 準備進入 Phase 1 (@INFRA)"
📋 手動驗證清單
結構驗證 (10 項)
text
□ [ ] kubernetes-ocr-service/ 根目錄存在
□ [ ] docs/ 目錄包含 api_spec.md, architecture.md
□ [ ] ocr-service/ 包含 4 個子目錄 (services,models,utils,tests)
□ [ ] k8s/ 目錄存在
□ [ ] scripts/ 目錄存在
□ [ ] test/ 包含 5 個子目錄 (functional,performance,chaos,reports,test_images)
□ [ ] .gitignore 存在且非空白
□ [ ] README.md > 100 行
□ [ ] 所有目錄權限 755
□ [ ] 無意外檔案 (.DS_Store, Thumbs.db)
文檔品質驗證 (8 項)
text
□ [ ] README.md 包含 Multi-Agent 團隊表格
□ [ ] README.md 包含快速開始指南 (4 步驟)
□ [ ] README.md 包含系統架構圖 (ASCII)
□ [ ] api_spec.md 定義 3 個端點
□ [ ] api_spec.md 每個端點有 Request/Response 範例
□ [ ] architecture.md 包含完整 K8s 架構圖
□ [ ] architecture.md 包含技術棧表格
□ [ ] 文檔無錯字、無格式錯誤
規範驗證 (5 項)
text
□ [ ] 目錄命名全小寫+連字號
□ [ ] 檔案命名規範 (kebab-case)
□ [ ] Python Package 結構正確
□ [ ] DevOps 目錄規範 (k8s/, scripts/)
□ [ ] 12-Factor App 原則符合
🎯 驗證通過標準
Phase 0 視為驗證通過當且僅當：

text
✅ 自動化腳本執行無錯誤 (100% 通過)
✅ 手動清單 23 項全勾選
✅ README.md > 100 行
✅ API 端點 3 個全定義
✅ 架構圖包含 K8s 叢集結構
✅ .gitignore 涵蓋 Python/Docker/K8s
✅ 總檔案數 > 15 個
✅ 總目錄數 > 20 個
🚨 驗證失敗處理
失敗項目	負責修正	修正指令
目錄缺失	@ARCH	重新執行 Step 2
README 過短	@ARCH	補充內容至 100+ 行
API 規格不全	@ARCH/@CODER	補充缺失端點
架構圖缺失	@ARCH	重新繪製 ASCII 圖
.gitignore 錯誤	@INFRA	更新忽略規則
📊 驗證報告模板
text
【Phase 0 驗證報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ANALYST
📍 Phase: Phase 0 - 專案初始化
⏰ 驗證時間: 2025-12-31 12:30:00

✅ 自動化驗證: 100% (6/6)
✅ 手動清單: 23/23
✅ README.md: 128 行
✅ API 端點: 3/3
✅ 架構圖: 完整
✅ 總檔案: 18 個
✅ 總目錄: 24 個

📁 產出統計:
  kubernetes-ocr-service/ (完整結構)
  README.md (128 行)
  docs/api_spec.md (45 行)
  docs/architecture.md (62 行)

👉 驗證狀態: ✅ 通過
👉 下一步: 交接給 @INFRA (Phase 1)
━━━━━━━━━━━━━━━━━━━━━━━━━━
執行 scripts/validate_phase0.sh 後，若顯示「✅ Phase 0 驗證通過 100%」，則 Phase 0 完成！