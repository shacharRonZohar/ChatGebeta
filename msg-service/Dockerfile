FROM python:3.7-alpine

RUN apk add --no-cache gcc musl-dev linux-headers mariadb-dev mariadb-client

WORKDIR /app

ENV FLASK_APP=ChatGebetaMsg
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=5000

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . .

RUN python setup.py bdist_wheel
RUN pip install ./dist/ChatGebetaMsg-2.0.0-py3-none-any.whl

CMD waitress-serve --port $PORT --call ChatGebetaMsg:create_app 
