FROM python:3.10.7 as builder

WORKDIR /app

COPY . . 

# ENV VIRTUAL_ENV=/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade wheel & \
    pip install --upgrade setuptools 
#& \
# pip install -r requirements.txt & \
# pip install -e .

RUN pip install waitress

EXPOSE 8080

# CMD ["waitress-serve",  "--call 'model-service-api:create_app"]

