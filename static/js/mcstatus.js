$(document).ready(function() {
    $('.mcstatus').load('http://voltaire.sh/mcstatus');
    var refreshId = setInterval(function() {
        $('.mcstatus').load('http://voltaire.sh/mcstatus');
    }, 15000);
    $.ajaxSetup({ cache: false });
});
