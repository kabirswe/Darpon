$(document).ready(function(){

});

function showinfo(e) {
    if (e == true) {
        $('.contact-info').hide();
        $('.contact-form-block').show();
    } else {
        $('.contact-form-block').hide();
        $('.contact-info').show();
    }
}
