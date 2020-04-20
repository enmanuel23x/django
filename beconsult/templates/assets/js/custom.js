document.documentElement.className = 'js';
var et_site_url = 'http://www.beconsult.com/beconsult_wp';
var et_post_id = '40';

function et_core_page_resource_fallback(a, b) {
    "undefined" === typeof b && (b = a.sheet.cssRules && 0 === a.sheet.cssRules.length);
    b && (a.onerror = null, a.onload = null, a.href ? a.href = et_site_url + "/?et_core_page_resource=" + a.id + et_post_id : a.src && (a.src = et_site_url + "/?et_core_page_resource=" + a.id + et_post_id))
}


//


jQuery(document).ready(function() {
    jQuery(".kiwi-logo-carousel-default").bxSlider({
        mode: "horizontal",
        speed: 500,
        slideMargin: 0,
        infiniteLoop: true,
        hideControlOnEnd: false,
        captions: false,
        ticker: false,
        tickerHover: false,
        adaptiveHeight: false,
        responsive: true,
        pager: false,
        controls: true,
        autoControls: false,
        minSlides: 1,
        maxSlides: 4,
        moveSlides: 1,
        slideWidth: 200,
        auto: true,
        pause: 4000,
        useCSS: false
    });
    jQuery(".kiwi-logo-carousel-carrusel_mobile").bxSlider({
        mode: "horizontal",
        speed: 500,
        slideMargin: 10,
        infiniteLoop: true,
        hideControlOnEnd: false,
        captions: false,
        ticker: false,
        tickerHover: false,
        adaptiveHeight: false,
        responsive: true,
        pager: false,
        controls: true,
        autoControls: false,
        minSlides: 1,
        maxSlides: 1,
        moveSlides: 1,
        slideWidth: 200,
        auto: true,
        pause: 1000,
        useCSS: false
    });
    jQuery(".kiwi-logo-carousel-carrusel_web").bxSlider({
        mode: "horizontal",
        speed: 500,
        slideMargin: 20,
        infiniteLoop: true,
        hideControlOnEnd: false,
        captions: false,
        ticker: false,
        tickerHover: false,
        adaptiveHeight: true,
        responsive: true,
        pager: false,
        controls: true,
        autoControls: false,
        minSlides: 1,
        maxSlides: 4,
        moveSlides: 1,
        slideWidth: 250,
        auto: true,
        pause: 4000,
        useCSS: false
    });
});

var et_animation_data = [{
        "class": "et_pb_image_0",
        "style": "slideLeft",
        "repeat": "once",
        "duration": "500ms",
        "delay": "0ms",
        "intensity": "10%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_18",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "100ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_19",
        "style": "slideRight",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "250ms",
        "intensity": "50%",
        "speed_curve": "ease-in-out"
    },
    {
        "class": "et_pb_text_20",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "100ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_21",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "250ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_22",
        "style": "slideRight",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "350ms",
        "intensity": "50%",
        "speed_curve": "ease-in-out"
    },
    {
        "class": "et_pb_text_23",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "250ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_24",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "400ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_25",
        "style": "slideRight",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "500ms",
        "intensity": "50%",
        "speed_curve": "ease-in-out"
    },
    {
        "class": "et_pb_text_26",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "400ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_27",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "550ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_28",
        "style": "slideRight",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "650ms",
        "intensity": "50%",
        "speed_curve": "ease-in-out"
    },
    {
        "class": "et_pb_text_29",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "550ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_30",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "700ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }, {
        "class": "et_pb_text_31",
        "style": "slideRight",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "800ms",
        "intensity": "50%",
        "speed_curve": "ease-in-out"
    },
    {
        "class": "et_pb_text_32",
        "style": "slideTop",
        "repeat": "once",
        "duration": "1000ms",
        "delay": "700ms",
        "intensity": "50%",
        "starting_opacity": "100%",
        "speed_curve": "ease-in-out"
    }
];


//




/* <![CDATA[ */
var et_shortcodes_strings = { "previous": "Anterior", "next": "Siguiente" };
var et_pb_custom = {
    "ajaxurl": "http:\/\/www.beconsult.com\/beconsult_wp\/wp-admin\/admin-ajax.php",
    "images_uri": "http:\/\/www.beconsult.com\/beconsult_wp\/wp-content\/themes\/Divi\/images",
    "builder_images_uri": "http:\/\/www.beconsult.com\/beconsult_wp\/wp-content\/themes\/Divi\/includes\/builder\/images",
    "et_frontend_nonce": "dd65156847",
    "subscription_failed": "Por favor, revise los campos a continuaci\u00f3n para asegurarse de que la informaci\u00f3n introducida es correcta.",
    "et_ab_log_nonce": "553aa720f9",
    "fill_message": "Por favor, rellene los siguientes campos:",
    "contact_error_message": "Por favor, arregle los siguientes errores:",
    "invalid": "De correo electr\u00f3nico no v\u00e1lida",
    "captcha": "Captcha",
    "prev": "Anterior",
    "previous": "Anterior",
    "next": "Siguiente",
    "wrong_captcha": "Ha introducido un n\u00famero equivocado de captcha.",
    "is_builder_plugin_used": "",
    "ignore_waypoints": "no",
    "is_divi_theme_used": "1",
    "widget_search_selector": ".widget_search",
    "is_ab_testing_active": "",
    "page_id": "40",
    "unique_test_id": "",
    "ab_bounce_rate": "5",
    "is_cache_plugin_active": "no",
    "is_shortcode_tracking": ""
};
var et_pb_box_shadow_elements = [];
/* ]]> */


//


/* <![CDATA[ */
var pum_vars = {
    "ajaxurl": "http:\/\/www.beconsult.com\/beconsult_wp\/wp-admin\/admin-ajax.php",
    "restapi": "http:\/\/www.beconsult.com\/beconsult_wp\/index.php?rest_route=\/pum\/v1",
    "rest_nonce": null,
    "default_theme": "224",
    "debug_mode": "",
    "disable_open_tracking": ""
};
var pum_debug_vars = {
    "debug_mode_enabled": "Popup Maker Debug Mode Enabled",
    "debug_started_at": "Debug started at:",
    "debug_more_info": "For more information on how to use this information visit http:\/\/docs.wppopupmaker.com\/?utm_medium=js-debug-info&utm_campaign=ContextualHelp&utm_source=browser-console&utm_content=more-info",
    "global_info": "Global Information",
    "localized_vars": "Localized variables",
    "popups_initializing": "Popups Initializing",
    "popups_initialized": "Popups Initialized",
    "single_popup_label": "Popup: #",
    "theme_id": "Theme ID: ",
    "label_method_call": "Method Call:",
    "label_method_args": "Method Arguments:",
    "label_popup_settings": "Settings",
    "label_triggers": "Triggers",
    "label_cookies": "Cookies",
    "label_delay": "Delay:",
    "label_conditions": "Conditions",
    "label_cookie": "Cookie:",
    "label_settings": "Settings:",
    "label_selector": "Selector:",
    "label_mobile_disabled": "Mobile Disabled:",
    "label_tablet_disabled": "Tablet Disabled:",
    "label_display_settings": "Display Settings:",
    "label_close_settings": "Close Settings:",
    "label_event_before_open": "Event: Before Open",
    "label_event_after_open": "Event: After Open",
    "label_event_open_prevented": "Event: Open Prevented",
    "label_event_setup_close": "Event: Setup Close",
    "label_event_close_prevented": "Event: Close Prevented",
    "label_event_before_close": "Event: Before Close",
    "label_event_after_close": "Event: After Close",
    "label_event_before_reposition": "Event: Before Reposition",
    "label_event_after_reposition": "Event: After Reposition",
    "label_event_checking_condition": "Event: Checking Condition",
    "triggers": {
        "click_open": {
            "name": "Click Open",
            "modal_title": "Click Trigger Settings",
            "settings_column": "<strong>Extra Selectors<\/strong>: {{data.extra_selectors}}"
        },
        "auto_open": {
            "name": "Auto Open",
            "modal_title": "Auto Open Settings",
            "settings_column": "<strong>Delay<\/strong>: {{data.delay}}"
        }
    },
    "cookies": {
        "on_popup_open": {
            "name": "On Popup Open",
            "modal_title": "On Popup Open Settings"
        },
        "on_popup_close": { "name": "On Popup Close", "modal_title": "On Popup Close Settings" },
        "manual": { "name": "Manual JavaScript", "modal_title": "Click Trigger Settings" }
    }
};
var ajaxurl = "http:\/\/www.beconsult.com\/beconsult_wp\/wp-admin\/admin-ajax.php";
var popmake_default_theme = "224";
/* ]]> */



// TRABAJA CON NOSOTROS


$(document).ready(function(){
    $(".accordion-title").click(function(e){
        var accordionitem = $(this).attr("data-tab");
        $("#"+accordionitem).slideToggle().parent().siblings().find(".accordion-content").slideUp();

        $(this).toggleClass("active-title");
        $("#"+accordionitem).parent().siblings().find(".accordion-title").removeClass("active-title");

        $("i.fa-chevron-down",this).toggleClass("chevron-top");
        $("#"+accordionitem).parent().siblings().find(".accordion-title i.fa-chevron-down").removeClass("chevron-top");
    });

});
//SCROLL
function scrollinfo(){
    $('html, body').animate({
        scrollTop: $("div.info-carusel").offset().top
      }, 1000)
}
function scrollservicios(){
    $('html, body').animate({
        scrollTop: $("div.servicios-div").offset().top
      }, 1000)
}
function scrollcaptacion(){
    $('html, body').animate({
        scrollTop: $("section.captacion-div").offset().top
      }, 1000)
}
function scrollbeneficios(){
    $('html, body').animate({
        scrollTop: $("h1.beneficios-div").offset().top
      }, 1000)
}
function scrollnoticias(){
    $('html, body').animate({
        scrollTop: $("section.noticias-div").offset().top
      }, 1000)
}
function scrollclientes(){
    $('html, body').animate({
        scrollTop: $("section.sectionEmpresas").offset().top
      }, 1000)
}