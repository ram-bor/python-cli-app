# Bookmarker Collector App

# Description

This Bookmarker has full CRUD (Create, Read, Update, Delete) capability. Users can add bookmarks by including webpage title, url and details. Users can search by title, url, and database ID.

# Technologies

- Python3
- PostgreSQL
- PeeWee

# Installation

Install dependencies:
`pipenv install peewee psycopg2-binary autopep8`

Initialize virtual environment:
`pipenv shell`

Create and seed database:

`psql < seed.sql`

Start the application:

`python3 app.py`
