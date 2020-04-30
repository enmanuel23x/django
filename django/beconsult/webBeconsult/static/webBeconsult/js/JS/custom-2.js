var mi_track_user = true;
var disableStr = 'ga-disable-UA-110957189-1';

/* Function to detect opted out users */
function __gaTrackerIsOptedOut() {
    return document.cookie.indexOf(disableStr + '=true') > -1;
}

/* Disable tracking if the opt-out cookie exists. */
if (__gaTrackerIsOptedOut()) {
    window[disableStr] = true;
}

/* Opt-out function */
function __gaTrackerOptout() {
    document.cookie = disableStr + '=true; expires=Thu, 31 Dec 2099 23:59:59 UTC; path=/';
    window[disableStr] = true;
}

if (mi_track_user) {
    (function(i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function() {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o),
            m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', '__gaTracker');

    __gaTracker('create', 'UA-110957189-1', 'auto');
    __gaTracker('set', 'forceSSL', true);
    __gaTracker('require', 'displayfeatures');
    __gaTracker('require', 'linkid', 'linkid.js');
    __gaTracker('send', 'pageview');
} else {
    console.log("");
    (function() {
        /* https://developers.google.com/analytics/devguides/collection/analyticsjs/ */
        var noopfn = function() {
            return null;
        };
        var noopnullfn = function() {
            return null;
        };
        var Tracker = function() {
            return null;
        };
        var p = Tracker.prototype;
        p.get = noopfn;
        p.set = noopfn;
        p.send = noopfn;
        var __gaTracker = function() {
            var len = arguments.length;
            if (len === 0) {
                return;
            }
            var f = arguments[len - 1];
            if (typeof f !== 'object' || f === null || typeof f.hitCallback !== 'function') {
                console.log('Not running function __gaTracker(' + arguments[0] + " ....) because you\'re not being tracked. ");
                return;
            }
            try {
                f.hitCallback();
            } catch (ex) {

            }
        };
        __gaTracker.create = function() {
            return new Tracker();
        };
        __gaTracker.getByName = noopnullfn;
        __gaTracker.getAll = function() {
            return [];
        };
        __gaTracker.remove = noopfn;
        window['__gaTracker'] = __gaTracker;
    })();
}

window._wpemojiSettings = { "baseUrl": "https:\/\/s.w.org\/images\/core\/emoji\/2.3\/72x72\/", "ext": ".png", "svgUrl": "https:\/\/s.w.org\/images\/core\/emoji\/2.3\/svg\/", "svgExt": ".svg", "source": { "concatemoji": "http:\/\/www.beconsult.com\/beconsult_wp\/wp-includes\/js\/wp-emoji-release.min.js?ver=4.8.9" } };
! function(a, b, c) {
    function d(a) {
        var b, c, d, e, f = String.fromCharCode;
        if (!k || !k.fillText) return !1;
        switch (k.clearRect(0, 0, j.width, j.height), k.textBaseline = "top", k.font = "600 32px Arial", a) {
            case "flag":
                return k.fillText(f(55356, 56826, 55356, 56819), 0, 0), b = j.toDataURL(), k.clearRect(0, 0, j.width, j.height), k.fillText(f(55356, 56826, 8203, 55356, 56819), 0, 0), c = j.toDataURL(), b !== c && (k.clearRect(0, 0, j.width, j.height), k.fillText(f(55356, 57332, 56128, 56423, 56128, 56418, 56128, 56421, 56128, 56430, 56128, 56423, 56128, 56447), 0, 0), b = j.toDataURL(), k.clearRect(0, 0, j.width, j.height), k.fillText(f(55356, 57332, 8203, 56128, 56423, 8203, 56128, 56418, 8203, 56128, 56421, 8203, 56128, 56430, 8203, 56128, 56423, 8203, 56128, 56447), 0, 0), c = j.toDataURL(), b !== c);
            case "emoji4":
                return k.fillText(f(55358, 56794, 8205, 9794, 65039), 0, 0), d = j.toDataURL(), k.clearRect(0, 0, j.width, j.height), k.fillText(f(55358, 56794, 8203, 9794, 65039), 0, 0), e = j.toDataURL(), d !== e
        }
        return !1
    }

    function e(a) {
        var c = b.createElement("script");
        c.src = a, c.defer = c.type = "text/javascript", b.getElementsByTagName("head")[0].appendChild(c)
    }
    var f, g, h, i, j = b.createElement("canvas"),
        k = j.getContext && j.getContext("2d");
    for (i = Array("flag", "emoji4"), c.supports = { everything: !0, everythingExceptFlag: !0 }, h = 0; h < i.length; h++) c.supports[i[h]] = d(i[h]), c.supports.everything = c.supports.everything && c.supports[i[h]], "flag" !== i[h] && (c.supports.everythingExceptFlag = c.supports.everythingExceptFlag && c.supports[i[h]]);
    c.supports.everythingExceptFlag = c.supports.everythingExceptFlag && !c.supports.flag, c.DOMReady = !1, c.readyCallback = function() { c.DOMReady = !0 }, c.supports.everything || (g = function() { c.readyCallback() }, b.addEventListener ? (b.addEventListener("DOMContentLoaded", g, !1), a.addEventListener("load", g, !1)) : (a.attachEvent("onload", g), b.attachEvent("onreadystatechange", function() { "complete" === b.readyState && c.readyCallback() })), f = c.source || {}, f.concatemoji ? e(f.concatemoji) : f.wpemoji && f.twemoji && (e(f.twemoji), e(f.wpemoji)))
}(window, document, window._wpemojiSettings);