/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

var urlParams = new URLSearchParams(window.location.search);

function greet() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const nameData=urlParams.get('name')||'Student';
    let greetElement = document.querySelector("h1");
    greetElement.innerText = `Hello, ${nameData}`;
}

function isPrime(n) {
    for (var i=2; i<n; i++) 
        if ( n % i === 0) {
            return false;
        }
    return n>1;
}

function printPrimeNumber() {
    const queryString=window.location.search;
    const urlParams=new URLSearchParams(queryString);
    const n=urlParams.get('n')||330;
    if(isPrime(n)){
        document.querySelector("#primeInfo").innerText= `${n} is a prime number`;
    }
    else{
        document.querySelector("#primeInfo").innerText= `${n} is not a prime number`;
    }
    }


function getNPrimes(n) {
    var list_primes = [];
    var k=2;
    for (var i=0; i<n; i++){
        while(list_primes.length<n){
            if(isPrime(k)) list_primes.push(k);
            k++;
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
            var newRow=tableData.insertRow();
            newRow.innerText=`${x}`;
            }

}

window.onload = function() {
    greet();
    printPrimeNumber();
    printNPrimes();
};