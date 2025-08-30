# Clippy Popup - Assistente Interativo

Um popup interativo inspirado no famoso Clippy do Windows 98, desenvolvido em Python 3.11 para Windows 11.

## 🎯 Características

- **Interface amigável**: Mascote fofo com traje de coelho e balão de fala
- **Imagens personalizadas**: Mascote e balão de fala com fundo transparente
- **Dicas de Python**: 8 dicas úteis de programação em Python
- **Curiosidades Geek**: 10 curiosidades e piadas nerds
- **Posicionamento inteligente**: Aparece no canto inferior direito da tela
- **Compatibilidade**: Funciona perfeitamente no Windows 11 com Python 3.11
- **Fallback inteligente**: Se as imagens não carregarem, usa ASCII art

## 🚀 Como Executar

### Pré-requisitos
- Python 3.11 ou superior
- Windows 11 (testado e otimizado)
- Biblioteca tkinter (já incluída no Python)
- Biblioteca Pillow (para imagens)

### Instalação e Execução

1. **Clone ou baixe o projeto**
   ```bash
   git clone <url-do-repositorio>
   cd popup
   ```

2. **Execute o programa**
   ```bash
   python clippy_popup.py
   ```

   Ou se você tiver múltiplas versões do Python:
   ```bash
   python3.11 clippy_popup.py
   ```

3. **Para parar o programa**
   - Clique no botão "Não"
   - Ou pressione `Ctrl+C` no terminal

## 🎮 Como Usar

### Botões Disponíveis

- **"Sim"** (Azul): Exibe uma dica aleatória de programação Python
- **"Não"** (Vermelho): Fecha o popup
- **"Me mostre algo legal"** (Roxo): Mostra uma curiosidade geek ou piada nerd
- **"Sobre"** (Cinza): Exibe informações sobre o programa

### Funcionalidades

#### 💡 Dicas de Python
O botão "Sim" oferece dicas práticas como:
- List comprehensions
- Operador walrus (:=)
- F-strings
- Método .get() de dicionários
- enumerate() em loops
- Context managers (with)
- zip() para múltiplas listas
- Desempacotamento com *

#### 🤖 Curiosidades Geek
O botão "Me mostre algo legal" apresenta:
- História do primeiro bug de computador
- Origem do nome Python
- Primeiro email enviado
- Criação do Linux
- E muito mais!

## 🛠️ Personalização

### Modificando as Dicas
Edite a lista `tips` na função `show_python_tip()` para adicionar suas próprias dicas.

### Adicionando Curiosidades
Edite a lista `cool_stuff` na função `show_cool_stuff()` para incluir mais curiosidades.

### Alterando o Visual
- Modifique as cores alterando os valores hexadecimais (ex: `bg='#f0f0f0'`)
- Ajuste o tamanho da janela em `self.root.geometry("300x400")`
- Personalize o mascote ASCII art na variável `mascote_text`

## 🔧 Solução de Problemas

### Erro: "tkinter not found"
- Instale o Python com suporte a tkinter
- No Windows, certifique-se de marcar "tcl/tk and IDLE" durante a instalação

### Janela não aparece no canto correto
- O posicionamento é calculado automaticamente
- Se houver problemas, verifique a resolução da tela

### Problemas de codificação
- O arquivo está configurado com UTF-8
- Certifique-se de que seu terminal suporta caracteres especiais

## 📝 Estrutura do Código

```
clippy_popup.py
├── ClippyPopup (classe principal)
│   ├── __init__() - Inicialização
│   ├── setup_window() - Configuração da janela
│   ├── create_widgets() - Criação da interface
│   ├── position_window() - Posicionamento
│   ├── show_python_tip() - Dicas Python
│   ├── show_cool_stuff() - Curiosidades
│   ├── show_about() - Informações
│   └── close_popup() - Fechamento
└── main() - Função principal
```

## 🎨 Tecnologias Utilizadas

- **Python 3.11**: Linguagem principal
- **Tkinter**: Interface gráfica
- **ASCII Art**: Mascote personalizado
- **Windows 11**: Sistema operacional alvo

## 📄 Licença

Este projeto é de código aberto e pode ser usado livremente para fins educacionais e pessoais.

## 🤝 Contribuições

Sinta-se à vontade para:
- Adicionar mais dicas de Python
- Incluir novas curiosidades geek
- Melhorar o design da interface
- Reportar bugs ou sugerir melhorias

---

**Divirta-se programando com o Clippy! 🐍✨**
# popuppython
# popuppython
# popuppython
# popuppython
# popuppython
# popuppython
