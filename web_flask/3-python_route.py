#!/usr/bin/python3

"""This uses the flask framework"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """btings hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """brings  HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """brings back  the specific text given"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_text(text):
    """this shows python the the text value"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':  # executed directly
    app.run(host='0.0.0.0', port=5000)
