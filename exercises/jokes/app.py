#!/usr/bin/env python3
"""Flask application to use `pyjokes`"""

import random
from typing import List

import pyjokes
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Render the template with form"""
    raise NotImplementedError


@app.route("/", methods=["POST"])
def index_jokes():
    return render_template("/index.html")
    raise NotImplementedError


def send_joke(
    language: str = "en", category: str = "all", number: int = 1
) -> List[str]:

    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "OK"}), 200)

    return res
    """Return a list of jokes"""
    raise NotImplementedError
