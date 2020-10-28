# REST API using Flask

## Tech used
* Python 3
* Flask
* SqlAlchemy
* Asyncio
* Celery
* Redis
* Sqlite
 

## Api Endpoints
* http://127.0.0.1:8000/api/submit
* http://127.0.0.1:8000/api/status
* http://127.0.0.1:8000/api/visits

## Installing
```bash
pip install -r requirements.txt
```

## Init database and load initial data
```bash
python manage.py initdb
```

## Run dev server
```bash
python server.py
```

## Run Test
```bash
python -m unittest tests/*.py
```

## Run celery worker
```bash
celery -A app.celery worker
```

## Improvements

* More unit test cases. At the moment test coverage is not enough.
* Better Design architecture
* Better management of dependency injection
* Documentation and code comments.
* Better database schema design
* Code quality

## Tools
* OS - Mac/Ubuntu
* IDE - Pycharm
