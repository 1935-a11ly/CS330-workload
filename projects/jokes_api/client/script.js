/* jshint esversion: 8 */
'use strict';
const BASE_URL =  "http://localhost:5000/api/v1/jokes"

async function get_joke() {
    language = document.getElementById(selLang);
    numberOfJokes = document.getElementById(selNum);
    jokeCategory = document.getElementById(selCat);
    jokeId = document.getElementById(jokeId);
    if (jokeId) {
        return fetch(`${BASE_URL}/${language}/${numberOfJokes}/${jokeCategory}/${jokeId}`)
        .then(response => response.json());
    }
    else{
        return fetch(`${BASE_URL}/${language}/${numberOfJokes}/${jokeCategory}`)
    .then(response => response.json());  
    }
}
async function print_joke(){
    
}

