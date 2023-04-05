# FROM python:3.10.7 as builder

# WORKDIR /app

# COPY . . 

# ENV VIRTUAL_ENV=/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# RUN pip install --upgrade wheel & \
#     pip install --upgrade setuptools & \
#     pip install -r requirements.txt & \
#     pip install -e .

# RUN pip install waitress



# # EXPOSE 8080

# CMD ["waitress-serve",  "--call","model-service-api:create_app"]

FROM python:3.7

WORKDIR /app

ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0

ENV VIRTUAL_ENV=/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install -r requirements.txt
RUN pip install waitress

EXPOSE 5050

COPY . .
RUN pip install -e .

CMD ["waitress-serve",  "--call","api:create_app","--port","5050"]

# CMD ["flask", "run", "--port", "5050"]
