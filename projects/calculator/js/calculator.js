/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

var screen;


function enterDigit(val) {
    document.querySelector("#result").innerText=`${val}`;
}


function clear_screen() {

}

function eval_expr() {
}

function enterOp(operation) {
    document.querySelector("#result").innerText=`${operation}`;
}

window.onload = function () {
    screen = document.querySelector("#result");
    screen.innerHTML = "0";
    
};