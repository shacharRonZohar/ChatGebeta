FROM python:3.7-alpine

WORKDIR /app

ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN python setup.py bdist_wheel
RUN pip install ./dist/api-2.0.0-py3-none-any.whl

RUN flask init-db

CMD waitress-serve --port $PORT --call api:create_app 
# RUN pip install -e .


# ENTRYPOINT [ "./dist/msg_service_api-2.0.0-py3-none-any.whl" ]