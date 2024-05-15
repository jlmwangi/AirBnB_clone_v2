#!/usr/bin/python3
"""fetches data from storage engine"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_state_id(state_id=None):
    """list states found by an id"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' +state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_context(exception):
    """removes current sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
