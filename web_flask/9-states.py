#!/usr/bin/python3
"""fetches data from storage engine"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_state():
    """fetches states from storage engine"""
    states = list(storage.all("State").values())

    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_state_id(id):
    """list states found by an id"""
    states = storage.all("State")
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_context():
    """removes current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
