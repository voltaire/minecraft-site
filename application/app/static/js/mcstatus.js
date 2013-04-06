$(document).ready(function() {
    $('.mcstatus').load('/mcstatus');
    var refreshId = setInterval(function() {
        $('.mcstatus').load('/mcstatus');
    }, 15000);
    $.ajaxSetup({ cache: false });
});
