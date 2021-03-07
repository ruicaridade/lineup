FROM python:3.8-slim

RUN pip install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install

CMD ["pipenv", "run", "gunicorn", "lineup.main:app"]
