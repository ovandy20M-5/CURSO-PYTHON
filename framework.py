from flask import Flask

app = Flask(__name__)

@app.router("/")
def hello_world():
    return "Hola mundo"