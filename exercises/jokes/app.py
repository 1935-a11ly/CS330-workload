#!/usr/bin/env python3
"""Flask application to use pyjokes"""

import random
from typing import List

import pyjokes
from flask import Flask, render_template, request, make_response, url_for, redirect

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    jokeCategory=request.cookies.get("jokeCategory")
    numberSelection=request.cookies.get("numberSelection")
    languageSelection=request.cookies.get("languageSelection")
    if languageSelection and numberSelection and jokeCategory:
        return render_template("base.html", alljokes=send_joke(languageSelection, jokeCategory, numberSelection))
    else:
        return render_template("base.html")
    raise NotImplementedError

@app.route("/", methods=["POST"])
def index_jokes():
    Data=make_response(redirect(url_for("index"), code=303))
    Data.set_cookie("jokeCategory", request.form.get("category"))
    Data.set_cookie("languageSelection", request.form.get("language"))
    Data.set_cookie("numberSelection", request.form.get("number"))
    return Data
    raise NotImplementedError


def send_joke(
    language: str = "en", category: str = "all", number: int = 1
) -> List[str]:
    if language == "es" and category=="chuck":
        return(["Zero jokes found on Chuck Norris in Spanish. Please try a different language."])
    
    elif number == 1:
        jokes = pyjokes.get_joke(language=language, category=category)
        fetchedJoke = []
        fetchedJoke.append(jokes[1])
        return fetchedJoke
    
    elif number == 5:
        jokes = pyjokes.get_joke(language=language, category=category)
        fetchedJoke = []
        fetchedJoke.append(jokes[5])
        return fetchedJoke
    else:
        jokes=pyjokes.get_jokes(language=language, category=category)
        fetchedJokes = []
        for numberOptions in range(int(number)):
            fetchedJokes.append(jokes[numberOptions])
    return fetchedJokes
    raise NotImplementedError