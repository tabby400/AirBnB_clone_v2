#!/usr/bin/python3
""" Using flask framework """

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """ list of states html page showm"""
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def states_id(state_id):
    """ html page with states list"""
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    state_found = False
    for state in states:
        if state.id == state_id:
            state_found = True
            return render_template(
                '9-states.html',
                states=states,
                cities=state.cities,
                id=state_id)
    if not state_found:
        return render_template(
            '9-states.html',
            states=states,
            id=None)


@app.teardown_appcontext
def close_session(exception):
    """ Closing session after  request """
    storage.close()


if __name__ == '__main__':  # execute directly
    app.run(host='0.0.0.0', port=5000)
