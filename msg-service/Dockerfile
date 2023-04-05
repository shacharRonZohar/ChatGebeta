FROM python:3.7-alpine

WORKDIR /app

ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0
# This will not be set here in a real app
ENV API_TOKEN = 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

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install waitress

# EXPOSE 5000

COPY . .
RUN pip install -e .

CMD ["waitress-serve" ,"--port",$port, "--call","api:create_app"]