from marshmallow import Schema, fields, validate


class ChatInputSchema(Schema):
    message = fields.String(required=True, validate=validate.Length(max=1024))
