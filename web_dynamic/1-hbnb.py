#!/usr/bin/python3
"""Replace the route 0-hbnb with 1-hbnb in the file 1-hbnb.py"""
from flask import Flask, render_template

app = Flask(__name__)

# Use a dynamic route 1-hbnb
@app.route('/1-hbnb/')
def hbnb():
    return render_template('1-hbnb.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
