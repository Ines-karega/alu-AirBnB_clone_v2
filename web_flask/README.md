# AirBnB Clone - Web Flask

This directory contains the Flask web application for the AirBnB Clone v2 project.

## Description

A Flask web application that serves dynamic HTML pages using data from either FileStorage (JSON) or DBStorage (MySQL via SQLAlchemy), depending on the `HBNB_TYPE_STORAGE` environment variable.

## Files

| File | Description |
|------|-------------|
| `0-hello_route.py` | Simple Flask app with `/` route returning "Hello HBNB!" |
| `1-hbnb_route.py` | Adds `/hbnb` route |
| `2-c_route.py` | Adds `/c/<text>` dynamic route |
| `3-python_route.py` | Adds `/python/<text>` with default value |
| `4-number_route.py` | Adds `/number/<n>` integer-only route |
| `5-number_template.py` | Renders HTML template for number route |
| `6-number_odd_or_even.py` | Renders odd/even HTML template |
| `7-states_list.py` | Lists all State objects from storage |
| `8-cities_by_states.py` | Lists all States with their Cities |
| `9-states.py` | States list and State detail with Cities |
| `10-hbnb_filters.py` | Full filter page with States and Amenities |

## Usage

```bash
# Run any script as a module from the repo root
python3 -m web_flask.0-hello_route

# With DBStorage
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
```

## Requirements

- Python 3.8+
- Flask
- All routes use `strict_slashes=False`
- Storage is closed after each request via `@app.teardown_appcontext`
