#!/usr/bin/python3
"""fetches data from storage engine"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """fetches states from storage engine"""
    states = storage.all("State")

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_context():
    """removes current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
