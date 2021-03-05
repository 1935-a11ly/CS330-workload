/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';

class PortfolioView {
    constructor(model) {
        // Connect to the model and redraw the table on change
        model.subscribe(this.redrawTable.bind(this));
    }

    redrawTable(listOfStocks, msg) {
        let tblBody = document.querySelector("#tblAllStocks > tbody");
        tblBody.innerHTML = "";

        for (let stock of listOfStocks) {
            let row = document.createElement("tr");
            let cb = document.createElement("input");
            cb.setAttribute("type", "checkbox");
            cb.setAttribute("id", "remove");
            cb.setAttribute("onclick", "removeStock()");
            row.appendChild(cb);
            
            let tdName = document.createElement("td");
            tdName.innerText = stock.stockName;
            row.appendChild(tdName);
            let tdCost = document.createElement("td");
            tdCost.innerText = stock.cost;
            row.appendChild(tdCost);
            let tdMoneyInvested = document.createElement("td");
            tdMoneyInvested.innerText = stock.cashInvested;
            row.appendChild(tdMoneyInvested);
            let tdChart = document.createElement("td");
            tdChart.innerText = stock.CurrentChartPattern;
            row.appendChild(tdChart);
            let tdTerm = document.createElement("td");
            tdTerm.innerText = stock.InvestmentDuration;
            
            row.appendChild(tdTerm);

            tblBody.appendChild(row);
        }
    }
}