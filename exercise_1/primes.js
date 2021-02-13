/* Michael Musa */
/* Primes Exercise */


/* jshint esversion: 8 */
/* jshint node: true */
'use strict';


var urlParams = new URLSearchParams(window.location.search);

function greet() {
    const queryString = window.location.search;


    /* Using queryString from lecture videos
    */
    const urlParams = new URLSearchParams(queryString);


    /* Gets name form URL. Defaults to Student if the user did not input any
    */
    const name_Information=urlParams.get('name')||'Student';

   
    /* Selects h1 from html
    */
    let welcome_Greeting = document.querySelector("h1");


    /* Changes h1 to greeting based on the name input by user
    */
    welcome_Greeting.innerText = `Hello ${name_Information}`;
   
}

function isPrime(n) {


     /* z is always smaller than the parameter
    */
    /* And this condition will not allow the parameter to be divisible by itself
    */
    for (var z=2; z<n; z++) 


    /* When the parameter is divisible by z it's not a prime
    */
        if ( n % z === 0) {
            return false;
        }
    

    /* Parameter must be greater than 1 since 1 is not Prime
    */ 
    return n>1;

}

function printPrimeNumber() {
    const queryString=window.location.search;


     /* Using queryString from lecture videos
    */ 
    const urlParams=new URLSearchParams(queryString);


    /* Gets n input by user in URL. if there is none defaults to 330
    */
    const n=urlParams.get('n')||330;


    if(isPrime(n)){
        document.querySelector("#primeInfo").innerText=`${n} is a prime number`;
    }
    else{
        document.querySelector("#primeInfo").innerText=`${n} is not a prime number`;
    }
    }


function getNPrimes(n) {

    var listOfPrimes = [];

    var y=2;

    for (var z=0; z<n; z++){
        while(listOfPrimes.length<n){
            if(isPrime(y)) listOfPrimes.push(y);
            y++;
        }
    }
    return listOfPrimes
}


function printNPrimes() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const n=urlParams.get('n')||330;

    let table_Header= document.querySelector("thead");
    table_Header.innerHTML= `First ${n} primes`;

        for (var x of getNPrimes(n)) {
            var table_Information=document.querySelector("tbody");
            var next_Row=table_Information.insertRow();
            next_Row.innerText=`${x}`;
            }

}

window.onload = function() {
    greet();
    printPrimeNumber();
    printNPrimes();
};