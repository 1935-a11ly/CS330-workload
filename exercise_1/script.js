/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

var urlParams = new URLSearchParams(window.location.search);

function greet() {
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const nameInfo=urlParams.get('name')||'student';
let greetElement = document.querySelector("h1");
greetElement.innerText = `Hello, ${nameInfo}`;
}

function isPrime(n) {
    let number = params.get('n')
        for (var n = 2; n < number;n++) {
            if ( number % n === 0 ) {
                return false;
            }
        }
        return true;
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
    var list_Primes = [];
    var k=2;
    for (var i=0; i<n; i++){
        while(list_Primes.length<n){
            if(isPrime(k)) list_Primes.push(k);
            k++;
        }
    }
    return list_Primes
}


function printNPrimes() {
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const n=urlParams.get('n')||330;
let thead= document.querySelector("thead");
thead.innerHTML= `First ${n} primes`;
for (var x of getNPrimes(n)) {
    var tableData=document.querySelector("tbody");
    var newRow=tableData.firstChild.insertRow();
    newRow.innerText=`${x}`;
}

}

window.onload = function() {
    greet();
    printPrimeNumber();
    printNPrimes();
};