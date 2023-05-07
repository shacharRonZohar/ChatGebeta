# ChatGebeta - A ChatGPT wrapper

This is an api wrapper, using a gpt-2 model to provide organic responses to end users.

This repository contains two branches - main, and basic, which have two distinct API's in them - the basic branch
contains the minimal working version answering the requirments of the task, and the main branch contains a robust API
with powerfull capabilities.
In order to run either of the branches, follow the Installation section in their respective README.

This Readme will describe the API for the Main branch.

The main branch conatins two API's - One public facing api, that recieves msgs from the user, and makes calls to the
second API, which runs the input through a self hosted gpt-2 model, ran by PyTorch.

This system allows us better control over the responses, but takes considerably more "personal" resources.

IMPORTANT: I took down the hosted project, self hosting the model cost too much per month to justify for a hobby project.
While both API's are hosted on Railway and publicly availabe, and can also both be ran locally, I recommend against
running the Model Service API, as it is about 10GB in size when fully installed and ran (because it stores the entire
gpt2 model locally), and the code in the Msg Service API is designed by default to talk with the deployed Model service
API even in local enviroments.

If for some reason you wish to do so, follow the "Model Self Hosting" instructions in the Run Locally section of the
main branch.

You can find API refrences in the README's inside the respective API folder.

The msg API also contains a frontend served statically using templates, demonstrating the app's abilities.

#### API's Root URL's:

Here are the links for the deployed API's, feel free to give them a few hits and see how they feel before diving into
the code!

- https://chatgebeta-msg-service.up.railway.app/
- https://chatgebeta-model-service.up.railway.app/api

## Run Locally

In order to run the Msg Service API locally, follow the following steps:
The API uses a Dockerfile and docker-compose to package it's enviroment, so you can use the dev versions of those to run
a local version of the API.

Alternatively, you can find the DIY instructions below

### General

1. Clone the repository
2. Enter the repository & Msg Service directory:

```bash
cd ChatGebeta/msg-service
```

### Docker

3. Run the docker compose command, pointing it to to the docker-compose.dev file

```bash
docker compose -f ./docker-compose.dev.yml up -d
```

You shoule see several printouts in the container terminal, the major ones are:

```bash
msg-service-web-1  |  * Running on all addresses (0.0.0.0)
msg-service-web-1  |  * Running on http://127.0.0.1:5000
msg-service-web-1  |  * Running on http://your.ip.here:5000
```

And you're good to go!

### DIY

3. Instantiate a new python enviroment:

```bash
python -m venv ./your-env-name-here
```

5. Run the Enviroment:

```powershell
Windows:
your-env-name-here\Scripts\activate
```

```bash
Mac \ Linux:
source your-env-name-here/bin/activate
```

6. Install the required packages:

```bash
pip install -r requirements.txt
```

7. Install the app as a package (optional):

```bash
pip install -e .
```

8. Run The app:

```bash
flask --app ChatGebetaMsg run --debug
```

You should see several logs in your terminal, the major one being

```bash
" * Running on http://127.0.0.1:5000".
```

And you're good to go!

### Model Self Hosting

Clone the repository if you haven't done so, if you previously installed the msg service, there's no need to reclone.

Go through steps 2-3 of the Docker option, or 2-4 of the DIY option, but replace "msg-service with "model-service".

The installation of the packages \ env should take a while depending on your machine, so grab a coffee / tea / chocolate
milk.

We need to point the API_URL in the Msg Service API to the local address of the Model Service API, so let's open the
following file in our favourite text editor \ IDE:

your\path\here\ChatGebeta\msg-service\ChatGebetaMsg\services\gpt.py

You shoule see the following code:

```python
from requests import post

# For local self hosted model
# API_URL = 'http://localhost:5050/api/model/'
# For self hosted model
API_URL = 'https://chatgebeta-model-production.up.railway.app/api/model/'

def query(payload):
    endpoint = 'generate'
    url = f'{API_URL}{endpoint}'
    return post(url, json=payload).json()

```

We need to uncomment the "For local self hosted model" API_URL, and comment the "For self hosted model" API_URL, which
will point it at the localhost, instead of the remote model, it should looke like this:

```python
from requests import post

# For local self hosted model
API_URL = 'http://localhost:5050/api/model/'
# For self hosted model
# API_URL = 'https://chatgebeta-model-production.up.railway.app/api/model/'

def query(payload):
    endpoint = 'generate'
    url = f'{API_URL}{endpoint}'
    return post(url, json=payload).json()

```

Now go through the rest of the installation process as normal, you may need to rebuild your docker image if you used
one.

And you're good to go!

## Authors

- [@Shachar Ron Zohar](https://github.com/shacharRonZohar)

## Feedback

If you have any feedback, please reach out to me @ rz_shachar@gmail.com, or feel free to open up a github issue /
discussion for the repo!
