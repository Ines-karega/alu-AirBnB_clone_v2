#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(error):
    """Close storage after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with list of states"""
    states = storage.all('State').values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
