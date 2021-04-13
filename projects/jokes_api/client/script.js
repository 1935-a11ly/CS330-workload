/* jshint esversion: 8 */
'use strict';
const BASE_URL =  "http://localhost:5000/api/v1/jokes"

async function get_joke() {
    var language = document.getElementById("selLang").value;
    var numberOfJokes = document.getElementById("selNum").value;
    var jokeCategory = document.getElementById("selCat").value;
    var jokeId = document.getElementById("jokeId").value;

    if (jokeId) {
        var jokes= fetch(`${BASE_URL}/${language}/${jokeCategory}/${numberOfJokes}/${jokeId}`)
        .then(response => response.json());
    }
    else{
        var jokes= await fetch(`${BASE_URL}/${language}/${jokeCategory}/${numberOfJokes}`)
    .then(response => response.json());  
    }
    let row=document.querySelector("#response")
    for (let index in jokes){
        let td=document.createElement("div");
        td.innerHTML=jokes[index];
        row.appendChild(td);
    }
}
async function print_joke(){
    pass
}

