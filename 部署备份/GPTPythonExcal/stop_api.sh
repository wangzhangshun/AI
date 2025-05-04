#!/bin/bash
echo "尝试结束运行中的 railway_parser_api Flask 服务 (监听8000端口)..."
PIDS=$(lsof -t -i:8000)
if [ -n "$PIDS" ]; then
  kill -9 $PIDS
  echo "已终止进程: $PIDS"
else
  echo "未找到监听8000端口的进程"
fi
