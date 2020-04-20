$(document).ready(function () {(function ($) {
  "use strict";


  var window_width = $(window).width(),
    window_height = window.innerHeight,
    header_height = $(".default-header").height(),
    header_height_static = $(".site-header.static").outerHeight(),
    fitscreen = window_height - header_height;

  $(".fullscreen").css("height", window_height)
  $(".fitscreen").css("height", fitscreen);


  $(window).on('scroll', function () {
    if ($(this).scrollTop() > 600) {
      $('.scroll-top').fadeIn(600);
    } else {
      $('.scroll-top').fadeOut(600);
    }
  });
  $('.scroll-top').on("click", function () {
    $("html,body").animate({
      scrollTop: 0
    }, 500);
    return false;
  });


  // ------------------------------------------------------------------------------ //
  // Active Menu 
  // ------------------------------------------------------------------------------ //


  $('#dopeNav').dopeNav({
    stickyNav: true,
  });

  //Smooth Scrolling Using Navigation Menu
  $('a[href*="#"]').on('click', function (e) {
    $('html,body').animate({
      scrollTop: $($(this).attr('href')).offset().top - 70
    }, 500);
    e.preventDefault();
  });
})(jQuery);});