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
    if  (language == "es" or language == "gl") and category == "chuck" :
        errorMessage = {"error":"Zero jokes found on Chuck Norris in this language. Please try a different language."}
        error = jsonify(errorMessage)
        error.headers["Access-Control-Allow-Origin"] = "*"
        error.headers["Content-Type"] = "application/json"
        return error
    else:
        allFetchedJokes = pyjokes.get_jokes(language=language, category=category)
        emptyDictionary={}
        for completeJokeList in range(len(allFetchedJokes)):
            emptyDictionary[completeJokeList]=allFetchedJokes[completeJokeList]
        for individualJokeList in range(number):
            jokes[individualJokeList]=emptyDictionary[individualJokeList]
        joke = jsonify(jokes)
        joke.headers["Access-Control-Allow-Origin"] = "*"
        joke.headers["Content-Type"] = "application/json"
        return joke

@app.route("/api/v1/jokes/<language>/<category>/<int:number>/<int:id>")
def index_jokes(number,language,category, id):
    if  (language == "es" or language == "gl") and category == "chuck" :
        errorMessage = {"error":"Zero jokes found on Chuck Norris in this language. Please try a different language."}
        error = jsonify(errorMessage)
        error.headers["Access-Control-Allow-Origin"] = "*"
        error.headers["Content-Type"] = "application/json"
        return error
    else:
        allFetchedJokes = pyjokes.get_jokes(language=language, category=category)
        emptyDictionary={}
        for completeJokeList in range(len(allFetchedJokes)):
            emptyDictionary[completeJokeList]=allFetchedJokes[completeJokeList]   
        jokes={id:emptyDictionary[id]}
        joke = jsonify(jokes)
        joke.headers["Access-Control-Allow-Origin"] = "*"
        joke.headers["Content-Type"] = "application/json"
        return joke
        
