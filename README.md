# ChatGebeta - A ChatGPT wrapper

This is an api wrapper, using a gpt-2 model to provide organic responses to end users.

This repository contains two branches - main, and basic, which have two distinct API's in them - the basic branch
contains the minimal working version answering the requirments of the task, and the main branch contains a more robust API
with more and better capabilities.
In order to run either of the branches, follow the Installation section in their respective README.

This Readme will describe the API for the Bassic branch.
The basic branch contains one public facing api, that recieves msgs from the user, and outsources the model managment to a free, public, gpt-2 API. This system gives worse responses, but is lightweight.

## Run Locally

In order to run the API locally, follow the following steps:

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

## Authors

- [@Shachar Ron Zohar](https://github.com/shacharRonZohar)

## Feedback

If you have any feedback, please reach out to me @ rz_shachar@gmail.com, or feel free to open up a github issue /
discussion for the repo!
