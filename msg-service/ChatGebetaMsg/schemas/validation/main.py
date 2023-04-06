from marshmallow import Schema, fields, validate


class ChatInputSchema(Schema):
    message = fields.String(required=True, validate=validate.Length(max=1024))


def validate_input(request, schema):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}

    input_data = request.get_json()
    errors = schema().validate(input_data)
    if errors:
        return {'error': errors}

    return input_data


def validate_chat_input(request):
    return validate_input(request, ChatInputSchema)
