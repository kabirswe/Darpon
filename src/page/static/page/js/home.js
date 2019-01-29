$(document).ready(function(){
    var swiper = new Swiper('.blog-slider', {
        spaceBetween: 30,
        effect: 'fade',
        loop: true,
        mousewheel: {
            invert: false,
        },
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        // autoHeight: true,
        pagination: {
            el: '.blog-slider__pagination',
            clickable: true,
        }
    });

    $("#scrollHide").overlayScrollbars({
        className       : "os-theme-dark",
        resize          : "both",
        sizeAutoCapable : true,
    });
});
