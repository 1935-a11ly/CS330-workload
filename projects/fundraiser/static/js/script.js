/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */

'use strict';

var otherVar;
var myVar; 

function calculator(){
    $('#result1').val($('#qty1').val() * $('#sel1').val());
    $('#result2').val($('#qty2').val() * $('#sel2').val());
    $('#result3').val($('#qty3').val() * $('#sel3').val());
    $('#result4').val($('#qty4').val() * $('#sel4').val());
    $('#result5').val($('#qty5').val() * $('#sel5').val());
    $('#result6').val($('#qty6').val() * $('#sel6').val());
    $('#result7').val($('#qty7').val() * $('#sel7').val());
    $('#result8').val($('#qty8').val() * $('#sel8').val());
    $('#result9').val($('#qty9').val() * $('#sel9').val());
    $('#result10').val($('#qty10').val() * $('#sel10').val());
    $('#result11').val($('#qty11').val() * $('#sel11').val());
    $('#result12').val($('#qty12').val() * $('#sel12').val());
}
        
function getTotals() {
    var sum = 0;
    $('.qty').each(function() {
        sum += Number($(this).val());
    });
    $('#totalCards').val(sum);    
    var add = 0;
    $('.result').each(function() {
        add += Number($(this).val());
    });
    $('#totalDue').val(add); 
    $('#pd1').val(($('#totalDue').val() * 0.01).toFixed(2));
}

$(document).ready(function(){
    myVar = setInterval("getTotals()", 10);
    otherVar = setInterval("calculator()", 10);
});

