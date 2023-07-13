$(document).ready(function() {
    $('.slider').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: false,
        speed: 800,
        arrows: false,
        centerMode: true,
        variableWidth: true,
    });
});