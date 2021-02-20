/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

var screen;


function enterDigit(val) {
    if (screen.innerHTML == "0" && val!= "."){
        document.querySelector("#result").innerHTML=`${val}`;
    }
    else{document.querySelector("#result").innerText=document.querySelector("#result").innerText+`${val}`;
}
}


function clear_screen() {
    document.querySelector("#result").innerText=`${0}`;
}

function eval_expr() {
    let x = screen.innerHTML
    let z = String(x)
    let y = eval(z)
    document.querySelector("#result").innerHTML=`${y}`

}

function enterOp(operation) {
    document.querySelector("#result").append(operation);
}

window.onload = function () {
    screen = document.querySelector("#result");
    screen.innerHTML = "0";
    
};