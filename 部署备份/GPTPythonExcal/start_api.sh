#!/bin/bash
# 启动 railway_parser_api 服务
cd "$(dirname "$0")"
echo "启动 railway_parser_api 服务..."
export FLASK_ENV=development
python3 app.py
