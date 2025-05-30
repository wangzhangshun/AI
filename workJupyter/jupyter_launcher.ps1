<#
.SYNOPSIS
    Jupyter Lab Ultimate Launcher (Crash-Proof)
.DESCRIPTION
    Features:
    - Anti-flash protection
    - Auto-error recovery
    - Persistent logging
#>

# 1. 强制编码和错误捕获
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = "Stop"
Start-Transcript -Path "$env:TEMP\jupyter_launcher.log" -Append -Force

# 2. 安全配置（根据您的实际路径修改）
$CONFIG = @{
    CondaEnv     = "myenv"
    WorkDir      = "D:\workPythionSpase\AI\workJupyter"
    CondaHome    = "C:\Users\wangz\miniconda3"
    JupyterPort  = 8888
}

# 3. 防闪退欢迎界面
function Show-Welcome {
    Clear-Host
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host " JUPYTER LAB ULTIMATE LAUNCHER v4.0      " -ForegroundColor White -BackgroundColor DarkBlue
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host "Crash-Proof System Initializing..." -ForegroundColor Gray
    Write-Host ""
}

# 4. 安全确认（带输入验证）
function Get-SafeConfirmation {
    do {
        Write-Host "=== SAFETY LOCK ===" -ForegroundColor Yellow
        Write-Host "Will execute:" -ForegroundColor Cyan
        Write-Host "1. Activate: $($CONFIG.CondaEnv)"
        Write-Host "2. WorkDir: $($CONFIG.WorkDir)"
        Write-Host "3. Port: $($CONFIG.JupyterPort)"

        $choice = Read-Host "`nType EXACTLY 'GO' to proceed (or 'STOP' to cancel)"

        if ($choice -eq "STOP") {
            Write-Host "Operation cancelled by user" -ForegroundColor Red
            exit 0
        }
    } while ($choice -ne "GO")
}

# 5. 关键路径验证（防崩溃）
function Test-CriticalPaths {
    $checks = @(
        @{ Path="$($CONFIG.CondaHome)\Scripts\conda.exe"; Name="Conda" },
        @{ Path="$($CONFIG.CondaHome)\envs\$($CONFIG.CondaEnv)\python.exe"; Name="Python" },
        @{ Path="$($CONFIG.CondaHome)\envs\$($CONFIG.CondaEnv)\Scripts\jupyter.exe"; Name="Jupyter" }
    )

    foreach ($check in $checks) {
        if (-not (Test-Path $check.Path)) {
            throw "[FATAL] Missing $($check.Name) at: $($check.Path)"
        }
    }
}

# 6. 主流程（带崩溃保护）
try {
    Show-Welcome
    Get-SafeConfirmation

    # 验证环境
    Test-CriticalPaths

    # 激活环境
    & "$($CONFIG.CondaHome)\Scripts\conda.exe" activate $CONFIG.CondaEnv

    # 工作目录
    if (-not (Test-Path $CONFIG.WorkDir)) {
        New-Item -Path $CONFIG.WorkDir -ItemType Directory -Force | Out-Null
    }
    Set-Location $CONFIG.WorkDir

    # 启动服务（分离进程）
    $jupyterPath = "$($CONFIG.CondaHome)\envs\$($CONFIG.CondaEnv)\Scripts\jupyter.exe"
    Start-Process $jupyterPath -ArgumentList "lab","--port=$($CONFIG.JupyterPort)" -NoNewWindow

    # 打开浏览器
    Start-Process "http://localhost:$($CONFIG.JupyterPort)/lab"

    # 保持窗口
    Write-Host "`n==========================================" -ForegroundColor Green
    Write-Host " SERVICE IS RUNNING                      " -ForegroundColor White -BackgroundColor DarkGreen
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host "Access: http://localhost:$($CONFIG.JupyterPort)/lab" -ForegroundColor Magenta
    Write-Host "Press ANY KEY to close this window" -ForegroundColor Yellow
    Write-Host "==========================================" -ForegroundColor Green
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

} catch {
    Write-Host "`n[CRITICAL ERROR] $_" -ForegroundColor Red
    Write-Host "`nAUTO-RECOVERY ATTEMPTED" -ForegroundColor Yellow

    # 尝试自动修复
    try {
        & "$($CONFIG.CondaHome)\Scripts\conda.exe" init powershell
        Write-Host "Conda PS profile regenerated" -ForegroundColor Cyan
    } catch {
        Write-Host "Auto-recovery failed" -ForegroundColor Red
    }

    Write-Host "`nView log: $env:TEMP\jupyter_launcher.log" -ForegroundColor White
    Write-Host "Press ANY KEY to exit" -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
} finally {
    Stop-Transcript
}