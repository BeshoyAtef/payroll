function getSalaryYearly(year){
    $.ajax({
    url: "/getSalary/",
    type: "GET",
    data: {
        "year" : year,
    }, 
    success: function(result) {
        alert(result);
    }
});
}
function getAttendanceYearly(year){
    $.ajax({
    url: "/getAttendanceYearly/",
    type: "POST",
    data: {
        "year" : year,
    }, 
    success: function(result) {
        alert(result);
    }
});
}
function getOutputYearly(year){
    $.ajax({
    url: "/getOutputYearly/",
    type: "POST",
    data: {
        "year" : year,
    }, 
    success: function(result) {
        alert(result);
    }
});
}
function getAttendanceMonthly(year, month){
    $.ajax({
    url: "/getAttendanceMonthly/",
    type: "POST",
    data: {
        "year" : year,
        "month" : month,
    }, 
    success: function(result) {
        alert(result);
    }
});
}
function getOutputMonthly(year, month){
    $.ajax({
    url: "/getOutputMonthly/",
    type: "POST",
    data: {
        "year" : year,
        "month" : month,
    }, 
    success: function(result) {
        alert(result);
    }
});
}
