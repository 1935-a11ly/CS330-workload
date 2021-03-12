/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';

async function get_individual(num, all_numbers) {
    all_numbers.innerHTML="";
    
    let numberFirst = await fetch(`http://numbersapi.com/${num-1}?json`)
    .then(response => response.json());
    let row1=document.createElement("div");
    let div1=document.createElement("div");
    let div2=document.createElement("div");
    row1.classList.add("numberAndDataContainer");
    div1.classList.add("numberInputByUser");
    div2.classList.add("factAboutNumber");
    div1.innerHTML=num-1;
    div2.innerHTML=numberFirst.text;
    row1.appendChild(div1);
    row1.appendChild(div2);
    all_numbers.appendChild(row1)  

    let numberSecond = await fetch(`http://numbersapi.com/${num}?json`)
    .then(response => response.json());
    let row2=document.createElement("div");
    let div3=document.createElement("div");
    let div4=document.createElement("div");
    row2.classList.add("numberAndDataContainer");
    div3.classList.add("numberInputByUser");
    div4.classList.add("factAboutNumber");
    div3.innerHTML= num;
    div4.innerHTML=numberSecond.text;
    row2.appendChild(div3);
    row2.appendChild(div4);
    all_numbers.appendChild(row2)  

    let numberThird = await fetch(`http://numbersapi.com/${num+1}?json`)
    .then(response => response.json());
    let row3=document.createElement("div");
    let div5=document.createElement("div");
    let div6=document.createElement("div");
    row3.classList.add("numberAndDataContainer");
    div5.classList.add("numberInputByUser");
    div6.classList.add("factAboutNumber");
    div5.innerHTML=num+1;
    div6.innerHTML=numberThird.text;
    row3.appendChild(div5);
    row3.appendChild(div6);
    all_numbers.appendChild(row3);
}

    
async function get_batch(num, all_numbers) {
    all_numbers.innerHTML="";
    let number = await fetch(`http://numbersapi.com/${num-1}..${num+1}?json`)
     .then(response => response.json());
    for (let item in number){
        let row=document.createElement("div");
        let firstDiv=document.createElement("div");
        let secondDiv=document.createElement("div");
        row.classList.add("numberAndDataContainer");
        firstDiv.classList.add("numberInputByUser");
        secondDiv.classList.add("factAboutNumber");
        firstDiv.innerHTML=item;
        secondDiv.innerHTML=number[item];
        row.appendChild(firstDiv);
        row.appendChild(secondDiv);
        all_numbers.appendChild(row);
    }
}

async function clickedon() {
    let num = parseInt(document.querySelector('#number').value);
    let all_numbers = document.querySelector('#number_info');
    if (document.querySelector('#batch').checked) {
        get_batch(num, all_numbers);
    } else {
        get_individual(num, all_numbers);
    }
}