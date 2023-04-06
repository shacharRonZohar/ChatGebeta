from marshmallow import Schema, fields, validate


class GenerationInputSchema(Schema):
    message = fields.String(required=True, validate=validate.Length(max=1024))
    max_response_length = fields.Integer(
        required=False, validate=validate.Range(min=1, max=300))


def validate_input(request, schema):
    if not request.is_json:
        return {'error': 'Request must be a JSON request'}

    input_data = request.get_json()
    errors = schema().validate(input_data)
    if errors:
        return {'error': errors}

    return input_data


def validate_generation_input(request):
    return validate_input(request, GenerationInputSchema)
