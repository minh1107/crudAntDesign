FROM python:3.8 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /capp

COPY --from=requirements-stage /tmp/requirements.txt /capp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /capp/requirements.txt

COPY . /capp
