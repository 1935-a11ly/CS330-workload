/* jshint esversion: 6 */
/* jshint browser: true */
"use strict;";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];

function addTask() {
    if (!document.querySelector("#newTask").checkValidity()) {
        let inputWarning = document.createElement("p");
        inputWarning.setAttribute("class", "alert alert-warning");
        inputWarning.innerText = "All options must be filled";
        document.querySelector("body").appendChild(inputWarning);
        return;
    }
    else{

        let vals = [];
        let rowcolids = ["title", "assignedTo", "priority", "dueDate"];
    
        addRow(vals, document.getElementById("taskList"));

    }

}

function addRow(valueList, parent) {
    let row = document.createElement("tr");
    let td = document.createElement("td");
    let cb = document.createElement("input");



    parent.appendChild(row);
}

function removeRow() {
    // https://stackoverflow.com/questions/26512386/remove-current-row-tr-when-checkbox-is-checked
}


function populateSelect(selectId, sList) {
    let selections = document.getElementById(selectId)
    for (let dropDown of sList) {
        let eachOption = document.createElement("option");
        eachOption.setAttribute("value", dropDown);
        eachOption.innerHTML = dropDown;
        selections.appendChild(eachOption);
        }
    
    }

//}
//function populateSelect(selectId, sList) {
    //let sel = document.getElementById(selectId, sList);

    // Implement
//}

window.onload = function() {
    populateSelect("assignedTo", team);
    populateSelect("priority", priority);
};
