#!/usr/bin/python3

""" Flask web framework being started """

from flask import Flask, render_template
from models.city import City
from models.state import State
from models import storage

app = Flask(__name__)  # flask application instance


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """showsHTML page with a list of all states with cities.
    States/cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Closing the session after a request """
    storage.close()


if __name__ == '__main__':  # executed directly
    app.run(host='0.0.0.0', port=5000)
