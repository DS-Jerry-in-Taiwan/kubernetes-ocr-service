#!/bin/bash
echo "【Phase 0 驗證】專案初始化"
cd "$(dirname "$0")/.."

# 1. 檢查核心目錄結構
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
