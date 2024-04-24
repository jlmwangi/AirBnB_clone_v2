#!/usr/bin/python3
""" starts a flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """display hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def textc(text):
    """displays c followed by text"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def is_cool(text="is cool"):
    """displays python followed by is cool"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def numbern(n):
    """display n only if its an int"""
    try:
        n_int = int(n)
        return f"{n_int} is a number"
    except Exception:
        return """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.\
                If you entered the URL manually please check \
                your spelling and try again.</p>"""


@app.route('/number_template/<n>', strict_slashes=False)
def html_page(n):
    """displays html page if n is an integer"""
    try:
        n_int = int(n)
        return render_template('5-number.html', n=n_int)
    except Exception:
        return """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server.\
                If you entered the URL manually please check\
                your spelling and try again.</p>"""


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def even_odd(n):
    """displays html page only if n is an odd or even integer"""
    try:
        n = int(n)
        return render_template('6-number_odd_or_even.html', n=n)
    except Exception:
        return ("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title>404 Not Found</title>
        <h1>Not Found</h1>
        <p>The requested URL was not found on the server. If you entered the \
                URL manually please check your spelling and try again.</p>""")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
