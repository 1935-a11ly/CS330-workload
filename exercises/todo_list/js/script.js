/* jshint esversion: 6 */
/* jshint browser: true */
"use strict;";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];
let td = document.createElement("td");

class Task {
    constructor(task, team, priority,dueDate) {
        this._task  = task;
        this._team = team;
        this._priority = priority;
        this._dueDate = dueDate;
    }

    get task() {
        return this._task;
    }

    get team() {
        return this._team;
    }

    get priority() {
        return this._priority;
    }

    get dueDate(){
        return this._dueDate;
    }
    
}



function addTask() {
    let vals = [];
    let rowcolids = ["title", "assignedTo", "priority", "dueDate"];

    if (!document.querySelector("#newTask").checkValidity()) {
        let inputWarning = document.createElement("p");
        inputWarning.setAttribute("class", "alert alert-warning");
        inputWarning.innerText = "Fill out title and due date";
        document.querySelector("body").appendChild(inputWarning);
        return;
    }
    else{

    let titleText = document.querySelector("#title").value;
    vals.push(titleText);
    let teamOptions = document.querySelector("#assignedTo").selectedOptions[0].value;
    vals.push(teamOptions);
    let priorityOptions = document.querySelector("#priority").selectedOptions[0].value;
    vals.push(priorityOptions);
    let dueDateOptions = document.querySelector("#dueDate").value;
    vals.push(dueDateOptions);

    addRow(vals, document.getElementById("taskList"));
}
}


function addRow(valueList, parent) {
    let td = document.createElement("td");
    let row = document.createElement("tr");
    let cb = document.createElement("input");
    cb.setAttribute("type", "checkbox");
    cb.setAttribute("id", "eliminate");
    cb.setAttribute("onclick", "removeRow();");
    
    let checker = document.createElement("td");
    checker.appendChild(cb);
    row.appendChild(checker);
    for (let elements of valueList){
        
        let td = document.createElement("td");
        td.innerHTML = elements;
        if (elements=="Low"){
            row.style.backgroundColor="green";
        }
        else if (elements=="Normal"){
            row.style.backgroundColor="orange";
        }
        else if (elements=="Important"){
            row.style.backgroundColor="yellow";
        }
        else if (elements=="Critical"){
            row.style.backgroundColor="red";
        }
        row.appendChild(td);
        
    }

    parent.appendChild(row);
}


function removeRow() {
    {$("#taskList input[type='checkbox']:checked").closest("tr").remove();}
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

function myFunction() {
    var element = document.getElementById("#taskList");
    element.classList.add("low");
  }


window.onload = function() {
    populateSelect("assignedTo", team);
    populateSelect("priority", priority);
    document.querySelector("#title").value = ""
    
}
