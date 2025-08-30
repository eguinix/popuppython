#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo do Clippy Popup - Mostra as funcionalidades sem abrir a interface gráfica
"""

import random

def show_python_tips():
    """Demonstra as dicas de Python disponíveis"""
    tips = [
        "💡 Dica Python: Use list comprehensions para criar listas de forma mais elegante!\n\nExemplo:\n[x**2 for x in range(10)]",
        
        "💡 Dica Python: O operador walrus (:=) permite atribuir valores em expressões!\n\nExemplo:\nif (n := len(data)) > 10:\n    print(f'Lista muito grande: {n} itens')",
        
        "💡 Dica Python: Use f-strings para formatação de strings (Python 3.6+)!\n\nExemplo:\nname = 'Python'\nprint(f'Olá, {name}!')",
        
        "💡 Dica Python: O método .get() de dicionários evita KeyError!\n\nExemplo:\nvalue = my_dict.get('key', 'default_value')",
        
        "💡 Dica Python: Use enumerate() para obter índice e valor em loops!\n\nExemplo:\nfor i, item in enumerate(items):\n    print(f'{i}: {item}')",
        
        "💡 Dica Python: O contexto manager (with) garante que recursos sejam liberados!\n\nExemplo:\nwith open('file.txt') as f:\n    content = f.read()",
        
        "💡 Dica Python: Use zip() para iterar sobre múltiplas listas!\n\nExemplo:\nfor name, age in zip(names, ages):\n    print(f'{name} tem {age} anos')",
        
        "💡 Dica Python: O operador * pode desempacotar listas!\n\nExemplo:\nnumbers = [1, 2, 3]\nprint(*numbers)  # 1 2 3"
    ]
    
    print("🎯 DEMONSTRAÇÃO - DICAS DE PYTHON")
    print("=" * 50)
    for i, tip in enumerate(tips, 1):
        print(f"\n{i}. {tip}")
        print("-" * 30)

def show_cool_stuff():
    """Demonstra as curiosidades geek disponíveis"""
    cool_stuff = [
        "🤖 Curiosidade: O primeiro 'bug' de computador foi literalmente um inseto! Em 1947, Grace Hopper encontrou uma mariposa presa no relé do Harvard Mark II.",
        
        "🎮 Piada Nerd: Por que o programador foi ao médico?\nPorque ele estava sofrendo de 'syntax error' na vida real! 😄",
        
        "🌍 Curiosidade: O Python foi nomeado em homenagem ao grupo de comédia Monty Python, não à cobra!",
        
        "⚡ Curiosidade: O primeiro email foi enviado em 1971 por Ray Tomlinson. Ele escolheu o símbolo @ para separar o nome do usuário do nome da máquina.",
        
        "🎯 Piada Nerd: Quantos programadores são necessários para trocar uma lâmpada?\nNenhum, isso é um problema de hardware! 😂",
        
        "🚀 Curiosidade: O primeiro computador pessoal, o Altair 8800, custava $395 em 1975. Hoje, um smartphone tem mais poder de processamento!",
        
        "💻 Curiosidade: Linus Torvalds criou o Linux em 1991 aos 21 anos, apenas como um hobby. Hoje roda em bilhões de dispositivos!",
        
        "🎪 Piada Nerd: Por que o programador Python é ruim em esportes?\nPorque ele sempre perde o 'self'! 😆",
        
        "🔬 Curiosidade: O primeiro vírus de computador foi criado em 1986 por dois irmãos paquistaneses. Era chamado 'Brain' e infectava disquetes.",
        
        "🎲 Curiosidade: O termo 'debugging' foi popularizado por Grace Hopper, que literalmente removeu um bug (inseto) de um computador!"
    ]
    
    print("\n🤖 DEMONSTRAÇÃO - CURIOSIDADES GEEK")
    print("=" * 50)
    for i, stuff in enumerate(cool_stuff, 1):
        print(f"\n{i}. {stuff}")
        print("-" * 30)

def show_mascote():
    """Mostra o mascote ASCII art"""
    mascote = """    ╭─────────╮
    │  (^_^)  │
    │   /|\\   │
    │  / \\   │
    ╰─────────╯
    Clippy v2.0"""
    
    print("\n🎭 MASCOTE ASCII ART")
    print("=" * 30)
    print(mascote)

def main():
    """Função principal da demonstração"""
    print("🎪 CLIPPY POPUP - DEMONSTRAÇÃO")
    print("=" * 50)
    print("Este script mostra as funcionalidades do Clippy Popup")
    print("sem abrir a interface gráfica.")
    print()
    
    # Mostra o mascote
    show_mascote()
    
    # Mostra algumas dicas de Python
    print("\n" + "="*50)
    print("💡 EXEMPLOS DE DICAS DE PYTHON")
    print("="*50)
    for i in range(3):
        tip = random.choice([
            "Use list comprehensions para criar listas de forma mais elegante!",
            "O operador walrus (:=) permite atribuir valores em expressões!",
            "Use f-strings para formatação de strings (Python 3.6+)!",
            "O método .get() de dicionários evita KeyError!",
            "Use enumerate() para obter índice e valor em loops!"
        ])
        print(f"{i+1}. {tip}")
    
    # Mostra algumas curiosidades
    print("\n" + "="*50)
    print("🤖 EXEMPLOS DE CURIOSIDADES GEEK")
    print("="*50)
    for i in range(3):
        stuff = random.choice([
            "O primeiro 'bug' de computador foi literalmente um inseto!",
            "O Python foi nomeado em homenagem ao grupo Monty Python!",
            "O primeiro email foi enviado em 1971 por Ray Tomlinson!",
            "Linus Torvalds criou o Linux em 1991 aos 21 anos!",
            "O termo 'debugging' foi popularizado por Grace Hopper!"
        ])
        print(f"{i+1}. {stuff}")
    
    print("\n" + "="*50)
    print("🎯 PARA VER A INTERFACE GRÁFICA:")
    print("Execute: python3 clippy_popup.py")
    print("="*50)

if __name__ == "__main__":
    main()
