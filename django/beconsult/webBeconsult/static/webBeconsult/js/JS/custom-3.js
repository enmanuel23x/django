(function(url) {
    if (/(?:Chrome\/26\.0\.1410\.63 Safari\/537\.31|WordfenceTestMonBot)/.test(navigator.userAgent)) { return; }
    var addEvent = function(evt, handler) {
        if (window.addEventListener) {
            document.addEventListener(evt, handler, false);
        } else if (window.attachEvent) {
            document.attachEvent('on' + evt, handler);
        }
    };
    var removeEvent = function(evt, handler) {
        if (window.removeEventListener) {
            document.removeEventListener(evt, handler, false);
        } else if (window.detachEvent) {
            document.detachEvent('on' + evt, handler);
        }
    };
    var evts = 'contextmenu dblclick drag dragend dragenter dragleave dragover dragstart drop keydown keypress keyup mousedown mousemove mouseout mouseover mouseup mousewheel scroll'.split(' ');
    var logHuman = function() {
        var wfscr = document.createElement('script');
        wfscr.type = 'text/javascript';
        wfscr.async = true;
        wfscr.src = url + '&r=' + Math.random();
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(wfscr);
        for (var i = 0; i < evts.length; i++) {
            removeEvent(evts[i], logHuman);
        }
    };
    for (var i = 0; i < evts.length; i++) {
        addEvent(evts[i], logHuman);
    }
})('//www.beconsult.com/beconsult_wp/?wordfence_lh=1&hid=9A165CE2ED7F02CAF29C882FA8ACFFA7');

jQuery(document).ready(function() {
    jQuery("article.et_pb_post").each(function() {
        jQuery(">a:first-child, .post-meta", this).insertAfter(jQuery(".post-content", this));
    });
    jQuery(".more-link").text("LEER MÁS");
});