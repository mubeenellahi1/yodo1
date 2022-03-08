# Yodo GeoData Application

Collects user location data and sends to backend

## Setting up backend

Backend:

```cd backend```

create python3 virtual environment
activate virtual environment

```pip install -r requirements.txt```

```python manage.py migrate```

```python manage.py runserver```

## Frontend
Front end is written in a simple html file

```cd frontend```

In index.html on line: 53 add google maps api key
open index.html file with any live server

    