import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

#criando janela 'win'
win = tk.Tk() #janela = win
win.title('TO-DO') #titulo da janela
win.configure(bg='#F0F0F0') #cor de fundo
win.geometry('500x600') #tamanho da janela
win.resizable(False, False) #tamanho maximo da janela


#definindo cabeçalho
fonte_cabecalho = font.Font(family='Garamond', size=24, weight='bold')
rotulo_cabecalho = tk.Label(win, text='Meu App de Tarefas', font=fonte_cabecalho, bg="#F0F0F0", fg='#333' ).pack(pady=20)

#definindo frame
frame_container = tk.Frame(win, bg="#F0F0F0").pack(pady= 10)

#definiindo entrada de dados
entrada_tarefa = tk.Entry(frame_container, font=('Garamond', 14), relief='flat', bg="white", fg='grey', width=30).pack(side='left', padx=10)

#definindo botão
botao_add = tk.Button(frame_container, text='Adiconar Tarefa', bg='#4CAF50', fg='white', height=1, width=15, font=('Robot', 11), relief='flat').pack(side='left', padx=10)

#definindo lista de tarefas
frame_lista_tarefas = tk.Frame(win, bg='white').pack(fill='both', expand=True, padx=10, pady=10)

#definindo canvas
canvas = tk.Canvas(frame_lista_tarefas, bg="white").pack(side='left', fill='both', expand=True)

#definindo scrollbar
scrollbar = ttk.Scrollbar(frame_lista_tarefas, orient='vertical').pack(side='right', fill='y')


#loop para funcionamento do programa
win.mainloop()
