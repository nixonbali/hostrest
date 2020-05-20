## Host Rest
Basic REST API enabling CRUD operations with respect to basic information about the host system.

- Django App
- native auth system to secure all routes
- SQLite DB
  - requests table
    - id (viz. autoincrementing int)
    - type of request (e.g. GET, POST, PUT, DELETE)
    - time of request (datetime)
    - comment (text, NULL by default)
- Routes
  - '/' index page, which upon a GET request
    - creates new entry in the `requests` table logging the request.
    - displays:
      - A table listing the last 10 times the page was loaded.
      - Results of running the shell commands `date` and `cat /proc/cpuinfo`

  - '/api/:id'
    - GET: displays the info for the request with ID=:id, returning a 404 if the entry is not found.
    - POST: sets the `comment` for the request with ID=:id with the submitted payload, returning a 200 if successful, else a 400.
    - PUT: return a 405.
    - DELETE: removes the entry with ID=:id, returning a 200 if successful and a 400 if not.

## Build Plan
- Host and test with Docker
- django-rest-framework to build all routes
- superuser can write, else all pages read-only
- sqlite db saved in directory for ease of sharing (will need superuser, minimal requests while building/testing may be committed)
- unittest all routes

## Build Log

### Initial Setup
`docker-compose run web django-admin startproject hostrest .`
`docker-compose run web python manage.py startapp requestlog`

Note: using 'requestlog' as app and class name to avoid confusion with django request object

## Upon Requestlog Model Definition
`docker-compose run web python manage.py makemigrations requestlog`
`docker-compose run web python manage.py migrate`

## To Run
`docker-compose up`

### Testing
`docker-compose run web python manage.py test`
