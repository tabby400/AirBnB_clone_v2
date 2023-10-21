#!/usr/bin/python3
"""The flask framework is being utilized"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this brings back hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """this brings HBNB"""
    return "HBNB"


if __name__ == '__main__':  # run directly
    app.run(host='0.0.0.0', port=5000)
