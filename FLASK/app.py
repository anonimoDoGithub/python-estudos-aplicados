from flask import Flask

app = Flask(__name__)

# localhost:5000/
# localhost:5000/sobre

# flask --app app run --debug
# Ctrl + C para SAIR

@app.route('/')
def principal():
    return "Hello World"