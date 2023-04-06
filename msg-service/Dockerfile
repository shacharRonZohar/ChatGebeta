FROM python:3.7-alpine

WORKDIR /app

ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install waitress

COPY . .
RUN pip install -e .

CMD waitress-serve --port=$PORT api:app