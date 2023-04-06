from marshmallow import Schema, fields, validate


class GenerationInputSchema(Schema):
    message = fields.String(required=True, validate=validate.Length(max=1024))
    max_response_length = fields.Integer(
        required=False, validate=validate.Range(min=1, max=300))
