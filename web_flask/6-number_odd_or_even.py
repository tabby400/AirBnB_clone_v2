#!/usr/bin/python3

"""This uses the flask framework"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """ shows number(n) only if integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ rendering a html page"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """ this shows if num is odd or even"""
    if n % 2 == 0:
        output = '{} is even'.format(n)
    else:
        output = '{} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', output=output)


if __name__ == '__main__':  # executed directly
    app.run(host='0.0.0.0', port=5000)
