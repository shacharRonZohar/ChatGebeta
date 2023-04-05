from flask import Flask, request, jsonify

from .services.gpt import get_response

app = Flask(__name__)


@app.get('/')
def welcome():
    return {'data': 'Welcome to ChatGebeta, a ChatGPT api wrapper'}


@app.post('/chat')
def chat():
    message = request.json['message']
    return {'data': get_response(message)}
