FROM python:3.12

RUN pip install poetry==1.8.3
RUN poetry config virtualenvs.create false

WORKDIR /server

COPY ./server/pyproject.toml ./
RUN poetry install --no-interaction --no-ansi --no-root

COPY ./server /server

EXPOSE 8085

CMD uvicorn main:app --host 0.0.0.0 --port 8085 --reload
