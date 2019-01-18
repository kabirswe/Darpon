$(document).ready(function(){
    // $(".mainlink").on("click", function() {
    //     $(".maincontent").fadeOut();
    //     $("#main-page").animate({
    //         width: "25px",
    //         height: "375px"
    //     }, function() {
    //         $(this).animateRotate(90);
    //     });
    //
    //     setTimeout(function() {
    //         $("#main-page").fadeOut();
    //     }, 1500);
    //
    //     setTimeout(function() {
    //         $("#next-page").animateRotate(0, 0);
    //         $("#next-page").css("height", "25px");
    //         $("#next-page").css("width", "375px");
    //         $("#next-page").fadeIn();
    //         $("#next-page").animate({
    //             backgroundColor: "#27ae60"
    //         }, function() {
    //             $(this).animate({
    //                 height: "100vh"
    //             }, function() {
    //                 $(this).animate({
    //                     width: "100%"
    //                 }, function() {
    //                     $(".nextcontent").fadeIn(300);
    //                 });
    //             });
    //         });
    //     }, 800);
    // });
});

function pageChange(e) {
    console.log('get data');
    console.log(this);
    console.log(e);
}
