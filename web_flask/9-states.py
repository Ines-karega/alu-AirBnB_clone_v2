#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(error):
    """Close storage after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Render HTML page with list of states."""
    states_list = sorted(storage.all('State').values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states_list, state=None,
                           show_list=True)


@app.route('/states/<id>', strict_slashes=False)
def state_details(id):
    """Render HTML page with state details."""
    state = storage.all('State').get('State.{}'.format(id))
    return render_template('9-states.html', states=[], state=state,
                           show_list=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
