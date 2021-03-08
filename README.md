# LineUp Exercise

I've given myself a few hours to build this out -- there's a lot of things I would change if I were to spend a bit more time on it, especially on the backend:

- Unit tests! The app is sorely missing unit tests, it would make me nervous to push something to production without a safety net of unit tests.

- A quick integration with an ORM - I'd be interested to see how well (or not) it integrates with something like SQLAlchemy.

- A better docker compose setup, with nginx as our frontend static server and proper volumes and such.

- Moving some bits in the frontend into their own components, such as extracting a re-usable "Table" component, instead of having all the fields and such hardcoded.

- Pagination on the frontend. As the user table wasn't necessarily part of the exercise, I've left out table pagination so I don't waste too much time going on tangents.

# Requirements

- Docker
- Docker Compose

## For Development

- Node
- Yarn
- Python >~3.8
- Pipenv

# Running

```
docker-compose up -d
```

The frontend will be accessible on `http://localhost:5000` and the backend on `http://localhost:8000`.

# Setup

## Frontend

```
cd frontend
yarn install

yarn start
```

## Backend

```
cd backend
pipenv install

pipenv run python -m lineup.main
```
