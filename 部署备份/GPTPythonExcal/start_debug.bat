@echo off
cd /d %~dp0
echo 启动 railway_parser_api 服务 (Debug 模式)...
set FLASK_ENV=development
python app.py
pause
