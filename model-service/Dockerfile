FROM python:3.10.7-alpine as builder

WORKDIR /app

COPY . . 

# ENV VIRTUAL_ENV=/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt & \
    pip install --upgrade wheel & \
    pip install --upgrade setuptools & \
    python setup.py bdist_wheel

# CMD ["python", "setup.py", "bdist_wheel"]

FROM python:3.10.7 as runner

WORKDIR /app

RUN python -m  venv /venv
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --from=builder /app/dist /app/dist

COPY . /app/

RUN  pip install dist/*.whl

RUN pip install gunicorn

EXPOSE 8080

CMD ["waitress-serve", "--port=8080", "model-service-api:create_app"]

