/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

var urlParams = new URLSearchParams(window.location.search);

function greet() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const name_Info=urlParams.get('name')||'Student';
    let welcome_Greeting = document.querySelector("h1");
    welcome_Greeting.innerText = `Hello ${name_Info}`;
}

function isPrime(n) {
    for (var z=2; z<n; z++) 
        if ( n % z === 0) {
            return false;
        }
    return n>1;
}

function printPrimeNumber() {
    const queryString=window.location.search;
    const urlParams=new URLSearchParams(queryString);
    const n=urlParams.get('n')||330;
    if(isPrime(n)){
        document.querySelector("#primeInfo").innerText=`${n} is a prime number`;
    }
    else{
        document.querySelector("#primeInfo").innerText=`${n} is not a prime number`;
    }
    }


function getNPrimes(n) {
    var list_primes = [];
    var y=2;
    for (var z=0; z<n; z++){
        while(list_primes.length<n){
            if(isPrime(y)) list_primes.push(y);
            y++;
        }
    }
    return list_primes
}


function printNPrimes() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const n=urlParams.get('n')||330;
    let thead= document.querySelector("thead");
    thead.innerHTML= `First ${n} primes`;
        for (var x of getNPrimes(n)) {
            var tableData=document.querySelector("tbody");
            var nextRow=tableData.insertRow();
            nextRow.innerText=`${x}`;
            }

}

window.onload = function() {
    greet();
    printPrimeNumber();
    printNPrimes();
};