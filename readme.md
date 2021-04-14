# Bookmark Collector 👩🏻‍💻 👨🏻‍💻

Bookmark Collector is a Python command line application designed for users to keep track of their favorite websites.

## Description

This app has full CRUD (Create, Read, Update, Delete) capability. Users can add bookmarks by including webpage title, url and details. Users can make updates to a bookmark's title, url and details field by searching for the bookmark's associated webpage title and delete bookmark records in a similar way.

![](bookmark-cli-app.gif)

## Technologies

- Python3
- PostgreSQL
- PeeWee

## Installation

Install dependencies:

`pipenv install peewee psycopg2-binary autopep8`

Initialize virtual environment:

`pipenv shell`

Create and seed database:

`psql < seed.sql`

Start the application:

`python3 app.py`
