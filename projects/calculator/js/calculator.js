/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

var screen;


function enterDigit(val) {
    document.querySelector("#result").append(val) 
}


function clear_screen() {
    document.querySelector("#result").innerText=`${0}`;
}

function eval_expr() {

}

function enterOp(operation) {
    document.querySelector("#result").append(operation);
}

window.onload = function () {
    screen = document.querySelector("#result");
    screen.innerHTML = "0";
    
};