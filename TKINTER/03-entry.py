import tkinter as tk # tk importa a biblioteca completa do TKINTER

janela = tk.Tk() # Tk() - Criar janela

janela.title("SNE") # title() - Coloca um Titulo na janela

mensagem = tk.Label(text="Sistema de Notas Escolares") # label(tipo="mensagem") Passo 1 - Criar o objeto
mensagem.pack() # pack() Passo 2 - Coloca o objeto dentro da janela

mensagem2 = tk.Label(text="Seja Bem Vindo(a)!", background='black', foreground='white')
mensagem2.pack()

mensagem3 = tk.Label(text="Professor(a)", bg='#6959CD', fg='white', width='20', height='5') # Tamanha e largura vão usar como parametros o TextUnit
mensagem3.pack()

professor = tk.Entry() # Entry - Cria uma caixa e pega o INPUT do USUÁRIO
professor.pack()

janela.mainloop() # mainloop() - faz com que a janela fique aparecendo