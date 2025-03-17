# 1 - Criar Ambiente Virtual de Desenvolvimento
#       python -m venv .venv
# 2 - Ativar o Ambiente Virtual de Desenvolvimento
#       Executando o arquivo ACTIVATE, dentro de SCRIPTS via terminal
#       .\.venv\Scripts\activate -> (.venv) mostra que esta ATIVADO
# 3 - Instalar o biblioteca do FLASK
#       pip install Flask

from flask import Flask

app = Flask(__name__)

# localhost:5000/
# localhost:5000/sobre

# flask --app app run --debug
# Ctrl + C para SAIR

@app.route('/')
def principal():
    return "Hello World"