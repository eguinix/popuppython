# 📋 Guia de Instalação - Clippy Popup

## 🪟 Windows 11

### Método 1: Instalação Automática
1. Baixe todos os arquivos do projeto
2. Execute o arquivo `install.bat` com duplo clique
3. O script verificará automaticamente se o Python está instalado
4. Se necessário, será direcionado para baixar o Python

### Método 2: Instalação Manual
1. **Instale o Python 3.11+**
   - Acesse: https://www.python.org/downloads/
   - Baixe a versão mais recente
   - **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação
   - **IMPORTANTE**: Marque "tcl/tk and IDLE" para ter o tkinter

2. **Execute o programa**
   ```cmd
   python clippy_popup.py
   ```

## 🐧 Linux (Ubuntu/Debian)

### Instalação das Dependências
```bash
# Atualize o sistema
sudo apt update

# Instale o Python 3 e tkinter
sudo apt install python3 python3-tk

# Verifique a instalação
python3 --version
python3 -c "import tkinter; print('Tkinter OK')"
```

### Execução
```bash
# Torne o script executável
chmod +x run.sh

# Execute
./run.sh
```

## 🍎 macOS

### Instalação via Homebrew
```bash
# Instale o Homebrew (se não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instale o Python e tkinter
brew install python python-tk

# Verifique a instalação
python3 --version
python3 -c "import tkinter; print('Tkinter OK')"
```

### Execução
```bash
# Torne o script executável
chmod +x run.sh

# Execute
./run.sh
```

## 🔧 Solução de Problemas

### Erro: "Python não encontrado"
- **Windows**: Reinstale o Python marcando "Add Python to PATH"
- **Linux**: `sudo apt install python3`
- **macOS**: `brew install python3`

### Erro: "Tkinter não encontrado"
- **Windows**: Reinstale o Python marcando "tcl/tk and IDLE"
- **Linux**: `sudo apt install python3-tk`
- **macOS**: `brew install python-tk`

### Erro: "Permission denied" (Linux/macOS)
```bash
chmod +x run.sh
chmod +x clippy_popup.py
```

### Janela não aparece
- Verifique se não há firewall bloqueando
- Tente executar em modo administrador (Windows)
- Verifique se o display está configurado (Linux)

## 🎯 Teste Rápido

Para verificar se tudo está funcionando:

```bash
# Execute a demonstração (sem interface gráfica)
python3 demo.py

# Execute o programa principal
python3 clippy_popup.py
```

## 📱 Requisitos Mínimos

- **Sistema Operacional**: Windows 10+, Ubuntu 18.04+, macOS 10.14+
- **Python**: 3.11 ou superior
- **Memória RAM**: 512 MB
- **Espaço em Disco**: 50 MB
- **Resolução**: 1024x768 (mínimo)

## 🚀 Execução Rápida

### Windows
```cmd
install.bat
```

### Linux/macOS
```bash
./run.sh
```

### Manual (qualquer sistema)
```bash
python3 clippy_popup.py
```

---

**🎉 Pronto! Agora você pode usar o Clippy Popup!**
