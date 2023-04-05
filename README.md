# ChatGebeta - A ChatGPT wrapper

This repository contains two branches - main, and basic, which are two almost identical api's, with one major diffrence.

The main branch API makes it's calls to another api, which contains a self hosted gpt-2 model, which allows us better control over the responses, but takes mroe resources.

The basic branch makes it's calls to a free, public gpt-2 api, which outsources the resposibilty of managing the model ourself.

This is an api wrapper, using a free gpt-2 endpoint to provide organic responses to end users.

## Installation

In order to run the app locally, follow the following steps:

1. Clone the repository
2. Enter the repository directory:

```bash
cd ChatGebeta
```

3. Instantiate a new python enviroment:

```bash
python -m venv ./your-env-name-here
```

4. Install the required packages:

```bash
pip install -r requirments.txt
```

5. Enter the api folder:
   ```bash
   cd api
   ```
6. Run The app:

```bash
flask run
```

You should see "Running on http://127.0.0.1:5000" printed to your console.

## API Reference

#### Get a welcome message

```http
  GET /api/
```

#### Get item

```http
  POST /api/chat/
```

| Parameter | Type     | Description                                                     |
| :-------- | :------- | :-------------------------------------------------------------- |
| `message` | `string` | **Required**. The user message to be sent to the language model |

## Authors

- [@Shachar Ron Zohar](https://github.com/shacharRonZohar)

## Feedback

If you have any feedback, please reach out to me @ rz_shachar@gmail.com, or feel free to open up a github issue / discussion for the repo!
