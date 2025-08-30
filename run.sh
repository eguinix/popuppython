#!/bin/bash

# Clippy Popup - Script de Execução para Linux/macOS

echo "========================================"
echo "   Clippy Popup - Assistente Interativo"
echo "========================================"
echo

# Verifica se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado!"
    echo
    echo "Por favor, instale o Python 3.11 ou superior:"
    echo "Ubuntu/Debian: sudo apt install python3"
    echo "macOS: brew install python3"
    echo
    exit 1
fi

echo "✅ Python encontrado!"
python3 --version

echo
echo "Verificando se o tkinter está disponível..."

# Verifica se o tkinter está disponível
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "❌ Tkinter não encontrado!"
    echo
    echo "Instale o tkinter:"
    echo "Ubuntu/Debian: sudo apt install python3-tk"
    echo "macOS: brew install python-tk"
    echo
    exit 1
fi

echo "✅ Tkinter disponível!"

echo
echo "========================================"
echo "   Iniciando Clippy Popup..."
echo "========================================"
echo
echo "Pressione Ctrl+C para sair do programa."
echo

# Executa o programa
python3 clippy_popup.py

echo
echo "Programa finalizado."
