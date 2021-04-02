#!/usr/bin/env python3
"""Flask application to use pyjokes"""

import random
from typing import List

import pyjokes
from flask import Flask, render_template, request, make_response, url_for, redirect

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    if request.method == "GET":

        jokeCategory=request.cookies.get("jokeCategory")

        # Uses request.cookies.get() as illustrated in HTTP methods lecture on youtube to get category

        numberSelection=request.cookies.get("numberSelection")

        # Uses request.cookies.get() as illustrated in HTTP methods lecture on youtube to get number

        languageSelection=request.cookies.get("languageSelection")

        # Uses request.cookies.get() as illustrated in HTTP methods lecture on youtube to get language

        if languageSelection  is not None and numberSelection is not None and jokeCategory is not None:

            # Attributes language, category and number cannot be NoneTypes for request to go through

            return render_template("base.html", alljokes=send_joke(languageSelection, jokeCategory, numberSelection))

        else:

            return render_template("base.html")

        raise NotImplementedError

@app.route("/", methods=["POST"])
def index_jokes():

    if request.method == "POST":

        Data = make_response(redirect(url_for("index"), code=303))
    
        # Syntax from HTTP methods lecture on youtube 
    
        Data.set_cookie("jokeCategory", request.form.get("category"))
    
        # Syntax for setting cookies for category from HTTP methods lecture on youtube
    
        Data.set_cookie("languageSelection", request.form.get("language"))
    
        # Syntax for setting cookies for language from HTTP methods lecture on youtube
    
        Data.set_cookie("numberSelection", request.form.get("number"))
    
        # Syntax for setting cookies for number from HTTP methods lecture on youtube
    
        return Data
    
        raise NotImplementedError


def send_joke(
    language: str = "en", category: str = "all", number: int = 1
) -> List[str]:

    if (language == "es" or language == "gl") and category=="chuck":

        # There are no jokes for Chuck Norris in Spanish and Galician so we inform the user and have them try a different language

        errorMessage = ["Zero jokes found on Chuck Norris in this language. Please try a different language."]

        # Return error message

        return(errorMessage)
    
    elif number == 1:

        allJokesFound = pyjokes.get_joke(language=language, category=category)

        fetchedJoke = []

        fetchedJoke.append(allJokesFound[1])

        return fetchedJoke
    
    elif number == 5:

        allJokesFound = pyjokes.get_joke(language=language, category=category)

        fetchedJoke = []

        fetchedJoke.append(allJokesFound[5])

        return fetchedJoke

    else:

        allJokesFound=pyjokes.get_jokes(language=language, category=category)

        fetchedJokes = []

        for allNumberOptions in range(int(number)):

            fetchedJokes.append(allJokesFound[allNumberOptions])

    return fetchedJokes

    raise NotImplementedError