#!/usr/bin/python3
"""Starts a web flask application"""
import os
import shutil
import uuid
from flask import Flask, render_template

app = Flask(__name__)

# Set up cache_id with a random UUID
cache_id = str(uuid.uuid4())


@app.route('/0-hbnb/')
def hbnb():
    # Render the template with cache_id as a query string
    return render_template('0-hbnb.html', cache_id=cache_id)


if __name__ == "__main__":
    # Run the application
    app.run(host='0.0.0.0', port=5000)
