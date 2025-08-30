#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clippy Popup - Um assistente interativo inspirado no Clippy do Windows 98
Desenvolvido para Python 3.11 e Windows 11
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import sys
import os

class ClippyPopup:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
        self.position_window()
        
    def setup_window(self):
        """Configura a janela principal"""
        self.root.title("Clippy Fofo Assistant")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        
        # Tenta fazer a janela ficar sempre no topo
        try:
            self.root.attributes('-topmost', True)
        except:
            pass
            
        # Remove a barra de título padrão para um visual mais limpo
        # self.root.overrideredirect(True)
        
        # Configura o ícone da janela (se disponível)
        try:
            self.root.iconbitmap('clippy.ico')
        except:
            pass
            
        # Define a cor de fundo mais suave
        self.root.configure(bg='#f8f9fa')
        
    def create_widgets(self):
        """Cria todos os widgets da interface"""
        # Frame principal com gradiente suave
        main_frame = tk.Frame(self.root, bg='#f8f9fa', padx=25, pady=25)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Carregar imagens
        try:
            mascote_image = Image.open('mascote_fofo.png')
            mascote_image = mascote_image.resize((120, 120), Image.Resampling.LANCZOS)
            self.mascote_photo = ImageTk.PhotoImage(mascote_image)
        except Exception as e:
            print(f"Erro ao carregar mascote: {e}")
            self.mascote_photo = None
            
        try:
            balao_image = Image.open('balao_fala.png')
            balao_image = balao_image.resize((220, 80), Image.Resampling.LANCZOS)
            self.balao_photo = ImageTk.PhotoImage(balao_image)
        except Exception as e:
            print(f"Erro ao carregar balão: {e}")
            self.balao_photo = None
        
        # Header com mascote centralizado
        header_frame = tk.Frame(main_frame, bg='#f8f9fa')
        header_frame.pack(pady=(0, 20))
        
        if self.mascote_photo:
            mascote_label = tk.Label(header_frame, image=self.mascote_photo, 
                                   bg='#f8f9fa')
            mascote_label.pack()
        else:
            # Fallback ASCII art mais bonito
            mascote_text = """    ╭─────────╮
    │  (^_^)  │
    │   /|\\   │
    │  / \\   │
    ╰─────────╯"""
            mascote_label = tk.Label(header_frame, text=mascote_text, 
                                   font=('Courier', 12), bg='#f8f9fa', fg='#6c757d')
            mascote_label.pack()
        
        # Nome do mascote
        nome_label = tk.Label(header_frame, text="Clippy Fofo v2.0", 
                           font=('Arial', 12, 'bold'), bg='#f8f9fa', fg='#495057')
        nome_label.pack(pady=(5, 0))
        
        # Balão de fala centralizado
        speech_frame = tk.Frame(main_frame, bg='#f8f9fa')
        speech_frame.pack(pady=(0, 25))
        
        if self.balao_photo:
            balao_label = tk.Label(speech_frame, image=self.balao_photo, 
                                 bg='#f8f9fa')
            balao_label.pack()
        else:
            # Fallback para texto estilizado
            welcome_text = "Oi! Precisa de ajuda com seu código?"
            welcome_label = tk.Label(speech_frame, text=welcome_text, 
                                   font=('Arial', 14, 'bold'), bg='#f8f9fa', fg='#495057',
                                   wraplength=280, justify=tk.CENTER)
            welcome_label.pack()
        
        # Frame para os botões com espaçamento melhorado
        buttons_frame = tk.Frame(main_frame, bg='#f8f9fa')
        buttons_frame.pack(pady=(0, 20))
        
        # Botão "Sim" - Estilo moderno
        sim_button = tk.Button(buttons_frame, text="💡 Sim, me ajude!", 
                             font=('Arial', 11, 'bold'),
                             bg='#007bff', fg='white',
                             relief=tk.FLAT, bd=0,
                             command=self.show_python_tip,
                             width=18, height=2,
                             cursor='hand2')
        sim_button.pack(pady=8)
        
        # Botão "Não" - Estilo moderno
        nao_button = tk.Button(buttons_frame, text="❌ Não, obrigado", 
                             font=('Arial', 11, 'bold'),
                             bg='#dc3545', fg='white',
                             relief=tk.FLAT, bd=0,
                             command=self.close_popup,
                             width=18, height=2,
                             cursor='hand2')
        nao_button.pack(pady=8)
        
        # Botão "Me mostre algo legal" - Estilo moderno
        legal_button = tk.Button(buttons_frame, text="🤖 Me mostre algo legal!", 
                               font=('Arial', 11, 'bold'),
                               bg='#6f42c1', fg='white',
                               relief=tk.FLAT, bd=0,
                               command=self.show_cool_stuff,
                               width=18, height=2,
                               cursor='hand2')
        legal_button.pack(pady=8)
        
        # Botão "Sobre" - Estilo discreto
        about_button = tk.Button(main_frame, text="ℹ️ Sobre", 
                               font=('Arial', 9),
                               bg='#6c757d', fg='white',
                               relief=tk.FLAT, bd=0,
                               command=self.show_about,
                               width=10, height=1,
                               cursor='hand2')
        about_button.pack(side=tk.BOTTOM, pady=(15, 0))
        
    def position_window(self):
        """Posiciona a janela no canto inferior direito da tela"""
        self.root.update_idletasks()
        
        # Obtém as dimensões da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Obtém as dimensões da janela
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        
        # Calcula a posição (canto inferior direito com margem)
        x = screen_width - window_width - 20
        y = screen_height - window_height - 40
        
        # Define a posição da janela
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
    def show_python_tip(self):
        """Exibe uma dica de programação em Python"""
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
        
        tip = random.choice(tips)
        messagebox.showinfo("💡 Dica Python", tip)
        
    def show_cool_stuff(self):
        """Exibe curiosidades geek ou piadas nerds"""
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
        
        stuff = random.choice(cool_stuff)
        messagebox.showinfo("🤖 Curiosidade Geek", stuff)
        
    def show_about(self):
        """Exibe informações sobre o programa"""
        about_text = """Clippy Popup v2.0

Um assistente interativo inspirado no famoso Clippy do Windows 98!

Desenvolvido em Python 3.11
Interface: Tkinter
Sistema: Windows 11

Características:
• Mascote ASCII art
• Dicas de programação Python
• Curiosidades geek e piadas nerds
• Posicionamento automático na tela

Divirta-se programando! 🐍✨"""
        
        messagebox.showinfo("Sobre Clippy", about_text)
        
    def close_popup(self):
        """Fecha o popup"""
        self.root.destroy()
        
    def run(self):
        """Inicia o loop principal da aplicação"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def main():
    """Função principal"""
    print("Iniciando Clippy Popup...")
    print("Pressione Ctrl+C para sair.")
    
    try:
        app = ClippyPopup()
        app.run()
    except Exception as e:
        print(f"Erro ao iniciar o aplicativo: {e}")
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
