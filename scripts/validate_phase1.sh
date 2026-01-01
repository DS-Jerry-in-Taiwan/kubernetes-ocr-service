#!/bin/bash
set -e
echo "【Phase 1 驗證】Docker 建置與健康檢查"
docker compose build
docker compose up -d
sleep 10
STATUS=$(curl -s http://localhost:8080/health | grep -c '"status":"ok"')
if [ "$STATUS" -eq 1 ]; then
  echo "✅ /health API 回應正確"
else
  echo "❌ /health API 回應錯誤"
  docker compose logs
  exit 1
fi
docker compose down
echo "【✅ Phase 1 驗證通過】"
