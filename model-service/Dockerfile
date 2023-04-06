FROM python:3.7

WORKDIR /app

ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0

ENV VIRTUAL_ENV=/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --upgrade wheel
RUN pip install -r requirements.txt
RUN pip install waitress

COPY . .

RUN python setup.py bdist_wheel
RUN pip install dist/api-2.0.0-py3-none-any.whl

CMD waitress-serve --port=$PORT --call api:create_app

