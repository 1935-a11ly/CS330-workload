/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';

const allStockOptions = ["Apple (AAPL)", "Amazon (AMZN)", "Facebook (FB)", "AMC", "Advanced Micro Devices (AMD)", "Tesla (TSLA)", "Twilio (TWLO)", "Draft Kings (DKNG)", "Nike (NKE)", "Netflix (NFLX)", "Walmart (WMT)", "Starbucks (SBUX)", "GameStop (GME)", "Rocket Companies (RKT)", "Sundial Growers (SNDL)", "Riot BlockChain (RIOT)", "Nokia (NOK)", "Blackberry(BB)", "Microsoft (MSFT)", "Alibaba Group (BABA)", "Walt Disney Company (DIS)", "Nvidia Corporation (NVDA)", "Bank of America (BAC)", "Coca-Cola Company (KO)", "Verizon Communications (VZ)"];
const allPossibleChartPatterns= ["Symmetrical Triangle", "Head and Shoulders", "Double top", "Double bottom", "Rounding bottom", "Cup and Handle", "Wedges", "Pennant or flags", "Ascending Triangle", "Descending Triangle"]
const allInvestmentTerms= ["Long Term", "Short Term"]

var myPortfolioModel = new Portfolio(200);
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
    let currentStocks_local = localStorage.getItem("currentStocks_local");
    currentStocks_local = currentStocks_local ? JSON.parse(currentStocks_local) : [];
    let cost = document.querySelector("#costPS").value;
    let stockName = document.querySelector("#stockOptions").selectedOptions[0].value;
    let cashInvested = document.querySelector("#moneyI").value;
    let CurrentChartPattern = document.querySelector("#CurrentChartPattern").selectedOptions[0].value;
    let InvestmentDuration = document.querySelector("#InvestmentTerm").selectedOptions[0].value;
 
    let newStock = new Stock(cost, stockName, cashInvested,CurrentChartPattern,InvestmentDuration );
    myPortfolioModel.add(newStock);
    currentStocks_local.push(newStock);
    localStorage.setItem("currentStocks_local" , JSON.stringify(currentStocks_local));
}
function removeAllStocks(){
        $("#tblAllStocks tbody tr").remove();
        localStorage.removeItem("currentStocks_local");
}

function removeStock(){
    $("#tblAllStocks tr").remove();
}
function loadStock(){

}
function strike(){

}

window.onload = function() {
    populateSelect(document.querySelector("#stockOptions"), allStockOptions);
    populateSelect(document.querySelector("#CurrentChartPattern"), allPossibleChartPatterns);
    populateSelect(document.querySelector("#InvestmentTerm"), allInvestmentTerms);
};