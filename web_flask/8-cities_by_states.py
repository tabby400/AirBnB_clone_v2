#!/usr/bin/python3

""" Flask web framework being started """

from flask import Flask, render_template
from models.city import City
from models.state import State
from models import storage

app = Flask(__name__)  # flask application instance


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ list of states in a html page is shown"""
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    city = sorted(list(storage.all(City).values()),
                  key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states, city=city)


@app.teardown_appcontext
def teardown(exception):
    """ Closing the session after a request """
    storage.close()


if __name__ == '__main__':  # executed directly
    app.run(host='0.0.0.0', port=5000)
