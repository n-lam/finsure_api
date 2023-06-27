# Finsure API

## Pre-requisites

- Python 3.10 (this can be installed via pyenv)
- Poetry
- **Recommended** - use Postman for testing

## Setup

```
poetry install
```

## Basic usage

Enter virtual environment

```
poetry shell
```

Run server

```
python manage.py runserver
```

Run migration

```
python manage.py migrate
```

## API

Create a new lender

```
curl -X POST http://localhost:8000/api/lenders.json/ -d "<data>"
```

List all lenders

```
curl http://localhost:8000/api/lenders.json
```

Get a specific lender

```
curl http://localhost:8000/api/lenders/<id>.json
```

Update a specific lender

```
curl -X PUT http://localhost:8000/api/lenders/<id>.json/ -d "<data>"
```

Delete a specific lender

```
curl -X DELETE http://localhost:8000/api/lenders/<id>.json
```

Bulk upload via CSV file

```
curl -X POST http://localhost:8000/api/lenders/?filetype=csv -d "{file: \"<csv>\"}"
```

Download CSV file (I think I should have wrapped the CSV in JSON to make this OpenAPI compliant
but that would be an easy change to make if needed).

```
curl http://localhost:8000/api/lenders/?filetype=csv
```

## Future improvements

- I would probably pick another API framework which has less indirection. Using DRF was quite
  hard to debug, so I might just use something like Django TastyPie in the future.
  - This would allow me to have more fine-grain control over the API routes so it would have
    a more intuitive design
- Create a file model which can handle the CSV file uploads (which could simplify the implementation since the LenderViewSet was a bit overloaded).
- Add auto-generated API docs (using either Swagger or ReDoc - https://www.django-rest-framework.org/topics/documenting-your-api/)
- Add authentication and authorisation.
- Add test cases for the API
