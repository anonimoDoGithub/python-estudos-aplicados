import tkinter as tk # tk importa a biblioteca completa do TKINTER

# GRID - Vai dividir em grades = linhas e colunas | começando no indice 0
# linha 0 | coluna 0
# linha 1 | coluna 1

janela = tk.Tk() # Tk() - Criar janela

janela.title("SNE") # title() - Coloca um Titulo na janela

janela.columnconfigure([0,1], weight=1) # [0,1,2] uma lista de colunas
janela.rowconfigure([0,1,2], weight=1) # rowconfigure = Ajusta automáticamente a janela (número de linhas, weight= 0 desligado - 1 ligado)

mensagem = tk.Label(text="Sistema de Notas Escolares", height='2') # label(tipo="mensagem") Passo 1 - Criar o objeto
mensagem.grid(row=0, column=0, columnspan=2) # grid(row=linha, column=coluna, columnspan=quantas colunas ocupar) | rowspan=(quantas linhas ocupar)

mensagem2 = tk.Label(text="Seja Bem Vindo(a)!", background='black', foreground='white', height='3') # width=(tamanho) e height(largura) vão usar como parametros o TextUnit
mensagem2.grid(row=1, column=0, columnspan=2, sticky="NSEW") # grid(row=linha, column=coluna, columnspan=quantas colunas ocupar, sticky="NSEW")

mensagem3 = tk.Label(text="Professor(a)", bg='#6959CD', fg='white', height='3') # Tamanha e largura vão usar como parametros o TextUnit
mensagem3.grid(row=2, column=0) # grid(row=linha, column=coluna) Passo 2 - Coloca o objeto dentro da janela

professor = tk.Entry() # Entry - Cria uma caixa e pega o INPUT do USUÁRIO
professor.grid(row=2, column=1) # grid(row=linha, column=coluna) Passo 2 - Coloca o objeto dentro da janela

janela.mainloop() # mainloop() - faz com que a janela fique aparecendo