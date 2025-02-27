FROM python:3.10-alpine

WORKDIR /usr/src/app

EXPOSE 5001

RUN pip install poetry

COPY pyproject.toml .

COPY poetry.lock .

RUN poetry install --no-root

COPY . .

CMD poetry run python3 src/index.py
