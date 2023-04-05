# FROM python:3.10.7-alpine as builder

# WORKDIR /app

# COPY . . 

# ENV VIRTUAL_ENV=/.venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# RUN pip install -r requirements.txt & \
#     pip install -e .

# CMD ["flask", "run", "--app=api","run"]


# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0
ENV API_TOKEN = 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
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install waitress
EXPOSE 5000
COPY . .
RUN pip install -e .
# CMD ["flask", "run" ,"--debug"]
CMD ["waitress-serve", "--call", "api:create_app"]