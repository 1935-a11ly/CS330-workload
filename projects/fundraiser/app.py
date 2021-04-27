#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask application to use pyjokes"""

import random
from typing import List

import pyjokes
from flask import Flask, jsonify

app = Flask(__name__)

if __name__ == "__main__":
    app.run()