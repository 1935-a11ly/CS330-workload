/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
'use strict';
class Stock {
    constructor(sName, cps, moneyI, chartPattern,iTerm) {
        this._stockName = sName;
        this._costPerShare  = cps;
        this._moneyInvested = moneyI;
        this._CurrentChart = chartPattern;
        this._InvestmentTerm = iTerm;
    }

    get stockName() {
        return this._stockName;
    }

    get cost() {
        return this._costPerShare;
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

    removeStock(stock) {
        if (this._port.length < this._maxSize) {
            this._port.pop(stock);
             this.publish(" Stock has been removed", this);
    }
    }
    
    [Symbol.iterator]() {
       let idx = -1;
        return {
            next: () => ({value: this._port[++idx], done: !(idx in this._port)})
        };
    }
}
