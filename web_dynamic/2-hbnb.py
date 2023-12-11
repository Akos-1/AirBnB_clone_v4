#!/usr/bin/python3
"""Starts a Flask Web Application for an AirBnB clone"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template
import uuid


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session upon application context teardown"""
    storage.close()

@app.route('/2-hbnb/', strict_slashes=False)
def hbnb():
    """
    Renders the main page of the AirBnB clone application.

    Returns:
        HTML template rendering the AirBnB clone main page with states,
        amenities, places, and a cache_id for asset caching.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())

if __name__ == "__main__":
    """Main function to run the Flask application"""
    app.run(host='0.0.0.0', port=5001)
