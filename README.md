# ChatGebeta - A ChatGPT wrapper

This is an api wrapper, using a gpt-2 model to provide organic responses to end users.

This repository contains two branches - main, and basic, which are two almost identical api's, with one major diffrence.

The main branch conatins two API's - One public facing api, that recieves msgs from the user, and makes calls to the second API, which runs the input through a self hosted gpt-2 model.
In order to run either of the branches, follow the Installation section in their respective README

The second API is hosted on railway, so you don't need to install and run it locally to run the public API, if for some reason you wish to do so, follow the "Self hosting" instructions in the installation section of the main branch.
This system allows us better control over the responses, but takes considerably more "personal" resources.

The basic branch contains one public facing api, that recieves msgs from the user, and outsources the model managment to a free, public, gpt-2 API.
This system gives worse responses, but is lightweight.

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

You should see "Running on http://127.0.0.1:5000" printed to your terminal.

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
