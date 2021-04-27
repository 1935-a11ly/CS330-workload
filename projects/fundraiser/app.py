#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask application for fundraiser"""


import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()