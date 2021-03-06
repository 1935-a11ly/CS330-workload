/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';

const allStockOptions = ["Apple (AAPL)", "Amazon (AMZN)", "Facebook (FB)", "AMC", "Advanced Micro Devices (AMD)", "Tesla (TSLA)", "Twilio (TWLO)", "Draft Kings (DKNG)", "Nike (NKE)", "Netflix (NFLX)", "Walmart (WMT)", "Starbucks (SBUX)", "GameStop (GME)", "Rocket Companies (RKT)", "Sundial Growers (SNDL)", "Riot BlockChain (RIOT)", "Nokia (NOK)", "Blackberry(BB)", "Microsoft (MSFT)", "Alibaba Group (BABA)", "Walt Disney Company (DIS)", "Nvidia Corporation (NVDA)", "Bank of America (BAC)", "Coca-Cola Company (KO)", "Verizon Communications (VZ)"];
const allPossibleChartPatterns= ["Symmetrical Triangle", "Head and Shoulders", "Double top", "Double bottom", "Rounding bottom", "Cup and Handle", "Wedges", "Pennant or flags", "Ascending Triangle", "Descending Triangle"]
const allInvestmentTerms= ["Long Term", "Short Term"]

var myPortfolioModel = new Portfolio(500);
var myPortfolioView = new PortfolioView(myPortfolioModel);

function populateSelect(selectElement, options) {
    for (let opt of options) {
        let anOption = document.createElement("option");
        anOption.setAttribute("value", opt);
        anOption.innerHTML = opt;
        selectElement.appendChild(anOption);
    }

}

function addStock() {
    if (!document.querySelector("#newStock").checkValidity()) {
        let warning = document.createElement("p");
        warning.setAttribute("class", "alert alert-warning");
        warning.innerText = "Money Invested and Cost per Share are required fields. Please enter these values";
        document.querySelector("body").appendChild(warning);
        return;
    }
    let stockName = document.querySelector("#stockOptions").selectedOptions[0].value;
    let cost = document.querySelector("#costPS").value;
    let cashInvested = document.querySelector("#moneyI").value;
    let CurrentChartPattern = document.querySelector("#CurrentChartPattern").selectedOptions[0].value;
    let InvestmentDuration = document.querySelector("#InvestmentTerm").selectedOptions[0].value;
 
    let newStock = new Stock(stockName,cost,cashInvested,CurrentChartPattern,InvestmentDuration );
    myPortfolioModel.add(newStock);

}

function removeStock(){
    $("#tblAllStocks input[type='checkbox']:checked").closest("tr").remove()
}


function removeAllStocks(){
    $("#tblAllStocks tbody tr").remove();
    localStorage.removeItem("currentStocks_local");
}

function saveStock(){
    let stocks = localStorage.getItem("currentStocks_local");
    stocks = stocks ? JSON.parse(stocks) : [];
    $("#tblAllStocks").find('tbody tr').each(function(index,stock){
        var sName=$(stock).find('td').eq(0).text();
        var cps=$(stock).find('td').eq(1).text();
        var moneyI=$(stock).find('td').eq(2).text();
        var chartPattern=$(stock).find('td').eq(3).text();
        var iTerm=$(stock).find('td').eq(4).text();
        stocks.push(new Stock(sName,cps,moneyI,chartPattern,iTerm))
    });
    localStorage.setItem("currentStocks_local", JSON.stringify(stocks));
}

function loadStock(){
    let restoreStocks = localStorage.getItem("currentStocks_local");
    if (restoreStocks) {
        restoreStocks = JSON.parse(restoreStocks);
        let tableBody = document.querySelector("#tblAllStocks > tbody");
        tableBody.innerHTML = "";

        for (let stock of restoreStocks){
            let row = document.createElement("tr");
            let checkbox = document.createElement("input");
            checkbox.setAttribute("type", "checkbox");
            checkbox.setAttribute("class", "strike");
            checkbox.setAttribute("onclick", "strike()");
            let tdRestore = document.createElement("td");
            tdRestore.appendChild(checkbox);
            row.appendChild(tdRestore);
            for(let stockItems in stock){
                let tdNew = document.createElement("td");
                tdNew.innerHTML = stock[stockItems];
                row.appendChild(tdNew);
            }
            tableBody.appendChild(row);
            document.querySelector("#tblAllStocks").appendChild(tableBody)
        }
    }
}

function strike() {
    $("input[type='checkbox']").on('change', function() {
        if ($(this).is(":checked")) {
         $(this).parent().css({
            'text-decoration': 'line-through',
            'color': 'red'
          })
        } else {
          $(this).parent().css({
            'text-decoration': 'none',
            'color': '#000'
          })
        }
      });
}

window.onload = function() {
    populateSelect(document.querySelector("#stockOptions"), allStockOptions);
    populateSelect(document.querySelector("#CurrentChartPattern"), allPossibleChartPatterns);
    populateSelect(document.querySelector("#InvestmentTerm"), allInvestmentTerms);
    loadStock();
};
