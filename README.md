# AirBnB Clone - v2

A full-stack clone of the AirBnB website built progressively in Python.

## Description

This project is the second version of the AirBnB clone. It extends the original console-based storage with MySQL database support via SQLAlchemy, and introduces a Flask web application to serve dynamic HTML pages.

## Features

- **Console**: command interpreter to manage AirBnB objects
- **Models**: BaseModel, User, State, City, Place, Amenity, Review
- **Storage engines**:
  - `FileStorage` – serializes/deserializes objects to a JSON file
  - `DBStorage` – stores objects in a MySQL database using SQLAlchemy ORM
- **Web Flask**: dynamic web pages served via Flask routes

## Web Flask routes

| Route | Description |
|-------|-------------|
| `/` | Hello HBNB! |
| `/hbnb` | HBNB |
| `/c/<text>` | C \<text\> |
| `/python/(<text>)` | Python \<text\> (default: "is cool") |
| `/number/<n>` | \<n\> is a number |
| `/number_template/<n>` | HTML page with number |
| `/number_odd_or_even/<n>` | HTML page with odd/even result |
| `/states_list` | List of all states |
| `/cities_by_states` | States with their cities |
| `/states` | All states |
| `/states/<id>` | Cities of a specific state |
| `/hbnb_filters` | Filters page (states + amenities) |

## Requirements

- Python 3.8+
- Flask
- SQLAlchemy
- MySQLdb or PyMySQL (for DBStorage)

## Usage

```bash
# FileStorage
python3 -m web_flask.0-hello_route

# DBStorage
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
```

## Authors

See [AUTHORS](AUTHORS)
