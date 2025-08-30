@echo off
chcp 65001 >nul
title Clippy Popup - Instalador

echo.
echo ========================================
echo    Clippy Popup - Assistente Interativo
echo ========================================
echo.

echo Verificando se o Python 3.11+ está instalado...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ Python não encontrado!
    echo.
    echo Por favor, instale o Python 3.11 ou superior:
    echo https://www.python.org/downloads/
    echo.
    echo Certifique-se de marcar "Add Python to PATH" durante a instalação.
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado!
python --version

echo.
echo Verificando se o tkinter está disponível...
python -c "import tkinter; print('✅ Tkinter disponível!')" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ❌ Tkinter não encontrado!
    echo.
    echo Reinstale o Python e certifique-se de marcar "tcl/tk and IDLE".
    echo.
    pause
    exit /b 1
)

echo ✅ Tkinter disponível!

echo.
echo ========================================
echo    Iniciando Clippy Popup...
echo ========================================
echo.
echo Pressione Ctrl+C para sair do programa.
echo.

python clippy_popup.py

echo.
echo Programa finalizado.
pause
