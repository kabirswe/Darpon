$(document).ready(function(){
});

function pageChange(e) {
    console.log('get data');
    console.log(this);
    console.log(e.getAttribute('data-name'));
    var page = e.getAttribute('data-name');
    console.log(window.location);
    console.log(window.location.host);
    var origin = window.location.origin;
    $('body').addClass('body-dark');
    $('.main-body').fadeOut(function(){
        window.location.href = origin + '/' + page;
    });
}
