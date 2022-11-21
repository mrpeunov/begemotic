FROM python:3.9.10-slim

RUN mkdir /apps/

COPY . /apps/

WORKDIR /apps/

RUN pip install pip==21.3.1
RUN pip install poetry
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt