# import functools
# import logging

# from dotenv import load_dotenv

from .services.gpt import query

from .schemas.chat import ChatInputSchema

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('model', __name__, url_prefix='/model')


@bp.post('/generate/')
def generate():
    input_data = validate_input(request)

    if isinstance(input_data, dict):
        return input_data, 400

    response = query(input_data)
    return response


def validate_input(request):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}

    input_data = request.get_json()
    errors = ChatInputSchema().validate(input_data)
    if errors:
        return {'error': errors}

    return input_data["message"]
