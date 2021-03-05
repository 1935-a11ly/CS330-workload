/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';
class Stock {
    constructor(cps, sName, moneyI, chartPattern,iTerm) {
        this._costPerShare  = cps;
        this._stockName = sName;
        this._moneyInvested = moneyI;
        this._CurrentChart = chartPattern;
        this._InvestmentTerm = iTerm;
    }

    get cost() {
        return this._costPerShare;
    }

    get stockName() {
        return this._stockName;
    }

    get cashInvested() {
        return this._moneyInvested;
    }

    get CurrentChartPattern() {
        return this._CurrentChart;
    }

    get InvestmentDuration() {
        return this._InvestmentTerm;
    }



}

class Subject {
    constructor() {
        this.handlers = [];
    }
    subscribe(func) {
        this.handlers.push(func);
    }

    unsubscribe(func) {
        this.handlers = this.handlers.filter(item => item !== func);
    }

    publish(msg, obj) {
        let scope = obj || window;
        for (let func of this.handlers) {
            func(scope, msg);
        }
    }
}

class Portfolio extends Subject {
    constructor(portSize) {
        super();
        this._maxSize = portSize;
        this._port = []; 
    }

    add(stock) {
        if (this._port.length < this._maxSize) {
           this._port.push(stock);
            this.publish("New stock has been added", this);
        }
    }

    removeStock() {
        $("#tblAllStocks tbody tr").remove();
    }

    [Symbol.iterator]() {
       let idx = -1;
        return {
            next: () => ({value: this._port[++idx], done: !(idx in this._port)})
        };
    }
}