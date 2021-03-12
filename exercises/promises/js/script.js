/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';

async function get_individual(num) {
    return fetch('http://numbersapi.com/' + String(num))
    .then (response => response.json())
    .then (data => console.log(data))
    .catch (error => console.log(error))
}

async function get_batch(num) {
    let result = await resolve_with_wait();
    console.log(result);
    console.log("Done");
}

async function clickedon() {
    let num = parseInt(document.querySelector('#number').value);
    let all_numbers = document.querySelector('#number_info');
    if (document.querySelector('#batch').checked) {
    //    get_batch(num, all_numbers);
    //} else {
        get_individual(num);
    }
}

window.onload = function(){
    clickedon();
}