$(window).load(function() {
    $(".main-loader").fadeOut("slow");
    $('body').ripples({
        resolution: 512,
        dropRadius: 30,
        perturbance: 0.02,
    });
});
