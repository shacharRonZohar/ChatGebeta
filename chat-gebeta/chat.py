from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get('/')
def welcome():
    return {'data': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@app.post('/chat')
def chat():
    print(request.json["message"])

    return
