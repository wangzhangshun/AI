@echo off
echo 尝试结束运行中的 railway_parser_api Flask 服务...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do (
    taskkill /PID %%a /F >nul 2>&1
)
echo 完成。
pause
