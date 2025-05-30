<#
.SYNOPSIS
    Safe Shortcut Creator
#>

$scriptPath = Join-Path $PSScriptRoot "jupyter_launcher.ps1"

$shortcutArgs = @"
-NoExit -ExecutionPolicy Bypass -WindowStyle Hidden -Command `"& {
    Start-Process powershell -ArgumentList '-NoExit -ExecutionPolicy Bypass -File ""$scriptPath""' -Verb RunAs
}"
"@

$shortcutPath = "$env:USERPROFILE\Desktop\Jupyter Lab.lnk"
$targetPath = "powershell.exe"

try {
    $ws = New-Object -ComObject WScript.Shell
    $sc = $ws.CreateShortcut($shortcutPath)
    $sc.TargetPath = $targetPath
    $sc.Arguments = $shortcutArgs
    $sc.WorkingDirectory = "D:\workPythionSpase\AI\workJupyter"
    $sc.IconLocation = "C:\Users\wangz\miniconda3\envs\myenv\Scripts\jupyter.exe, 0"
    $sc.Save()
    Write-Host "Shortcut created successfully" -ForegroundColor Green
} catch {
    Write-Host "Failed to create shortcut: $_" -ForegroundColor Red
    Write-Host "`nALTERNATIVE SOLUTION:" -ForegroundColor Yellow
    Write-Host "1. Right-click desktop -> New -> Shortcut"
    Write-Host "2. Paste this command:"
    Write-Host "   powershell.exe -NoExit -ExecutionPolicy Bypass -File `"$scriptPath`"" -ForegroundColor White
}