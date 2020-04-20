$(document).ready(function () {(function ($) {
    "use strict";
    // ------------------------------------------------------------------------------ //
    // carousel  1
    // ------------------------------------------------------------------------------ //
  
  
    $("#info-carusel").owlCarousel({
      items: 1,
        margin: 0,
        loop: true,
        nav: true,
        navText: ['',''],
        dots: false,
        autoplay: true,
        autoplaySpeed: 500,
        autoplayTimeout:8000
    });
    $("#empresas-carusel").owlCarousel({
      loop: true,
      dotsEach: true,
        autoplay: true,
        items : 1,
        nav: false,
        dots: false,
        autoplaySpeed: 500,
        responsive : {
          480 : { items : 1  }, // from zero to 480 screen width 4 items
          768 : { items : 2  }, // from 480 screen widthto 768 6 items
          1024 : { items : 3 },  // from 768 screen width to 1024 8 items
          2048 : { items : 4 }  // from 1024 screen width to 2048 8 items
          }
    });
    $("#theme-carusel").owlCarousel({
      items: 1,
        margin: 0,
        loop: true,
        nav: true,
        navText: ['',''],
        dots: false,
        autoplay: true,
        autoplaySpeed: 500,
        autoplayTimeout:15000
    });
  
  })(jQuery);});