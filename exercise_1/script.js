/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

var urlParams = new URLSearchParams(window.location.search);

function greet() {
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
let greetElement = document.querySelector("h1");
greetElement.innerHTML = `Hello ${urlParams.get('name')}`;
}

function isPrime(n) {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    let number = params.get('n')
        for (var n = 2; n < number;n++) {
            if ( number % n === 0 ) {
                return false;
            }
        }
        return true;
    }

function printPrimeNumber() {
    let primeElement = document.querySelector("h3");
}

function getNPrimes(n) {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    let number = params.get('n')
    var arr = [2];
    for ( var n = 3; n < number; n+=2 ) {
        if ( isPrime(n) ) {
            arr.push(n);
        }
    }

}


function printNPrimes() {
    getNPrimes()
    console.log(arr)
}

window.onload = function() {
    greet();
    printPrimeNumber();
    printNPrimes();
};