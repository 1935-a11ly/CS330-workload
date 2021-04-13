#!/usr/bin/env python3

#!/usr/bin/env python3
"""Flask application to use pyjokes"""

import random
from typing import List

import pyjokes
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/jokes/<language>/<category>/<int:number>")
def index(number,language,category):
    jokes={}
    if  language == "es" and language == "gl" and category == "chuck" :
        return "No kidding"
    else:
        alljokes = pyjokes.get_jokes(language=language, category=category)
        dictionary={}
        for i in range(len(alljokes)):
            dictionary[i]=alljokes[i]
        for k in range(number):
            jokes[k]=dictionary[k]
        joke = jsonify(jokes)
        joke.headers["Access-Control-Allow-Origin"] = "*"
        joke.headers["Content-Type"] = "application/json"
        return joke

@app.route("/api/v1/jokes/<language>/<category>/<int:number>/<int:id>")
def index_jokes(number,language,category, id):
    if  language == "es" and language == "gl" and category == "chuck" :
        return "No kidding"
    else:
        alljokes = pyjokes.get_jokes(language=language, category=category)
        dictionary={}
        for i in range(len(alljokes)):
            dictionary[i]=alljokes[i]   
        jokes={id:dictionary[id]}
        joke = jsonify(jokes)
        return joke
        
