# Model Service API

This is the API which hosts the gpt-2 model, and provides an endpoint for text-generation.

## API Reference

#### Generate Text from the model

```http
  POST /api/model/generate
```

Accepts a JSON object in the request body, with the following properties:
message: The text to generate text from.

Returns a JSON object with the generated text.

##### Example Request

```http
  POST /api/model/generate
```

```json
{
  "message": "Hi, how are you?"
}
```

##### Example Response

```json
{
  "data": {
    "user_input": "Hi, how are you?",
    "bot_response": "Ominous ramblings about how AI's gonna take over the world, and i'm first in line."
  }
}
```

##### Example Request & Response

Request:

```http
  POST /api/model/generate
```

```json
{
  "message": 1
}
```

Response:

```json
{
  "error": {
    "message": ["Not a valid string."]
  }
}
```
