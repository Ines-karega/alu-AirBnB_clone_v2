#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.static_folder = 'static'


@app.teardown_appcontext
def close_storage(error):
    """Close storage after each request."""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Render HBnB filters page."""
    states = sorted(storage.all('State').values(), key=lambda x: x.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
