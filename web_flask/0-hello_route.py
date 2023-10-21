#!/usr/bin/python3

""" The flask framework is to be used here"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
# This fuction is able to return hello hbnb#


if __name__ == '__main__':  # executed directly#
    app.run(host='0.0.0.0', port=5000)
