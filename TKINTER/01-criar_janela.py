import tkinter as tk # tk importa a biblioteca completa do TKINTER

janela = tk.Tk() # Tk() - Criar janela

janela.title("SNE") # title() - Coloca um Titulo na janela

mensagem = tk.Label(text="Sistema de Notas Escolares") # label(tipo="mensagem") Passo 1 - Criar o objeto
mensagem.pack() # pack() Passo 2 - Coloca o objeto dentro da janela

janela.mainloop() # mainloop() - faz com que a janela fique aparecendo

