/**
* DOM utilities without jQuery
* Refer to http://youmightnotneedjquery.com
*/

var nau = nau || {};

(function() {
    'use strict';

    /**
    * Replace jQuery's document ready $(fn)
    * @param  {Function} fn [description]
    * @return {void}
    */
    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    /**
    * Shorthand for document.querySelector()
    * @param  {string} selector [description]
    * @return {HTMLElement}          [description]
    */
    function $(selector) {
        return document.querySelector(selector);
    }

    /**
    * Shorthand for document.querySelectorAll()
    *
    * @param  {string} selector [description]
    * @return {Array} Real Array of elements for easy traversial and
    */
    function $$(selector) {
        return Array.prototype.slice.call(document.querySelectorAll(selector));
    }

    var Vanilla = {

        toggleClass: function(el, className) {
            if (el.classList) {
                el.classList.toggle(className);
            } else {
                var classes = el.className.split(' ');
                var existingIndex = classes.indexOf(className);

                if (existingIndex >= 0) {
                    classes.splice(existingIndex, 1);
                } else {
                    classes.push(className);
                }

                el.className = classes.join(' ');
            }
        },

        addClass: function(el, className) {
            if (el.classList) {
                el.classList.add(className);
            } else {
                el.className += ' ' + className;
            }
        },

        removeClass: function(el, className) {
            if (el.classList) {
                el.classList.remove(className);
            } else {
                el.className = el.className.replace(new RegExp('(^|\\b)' + className.split(' ').join('|') + '(\\b|$)', 'gi'), ' ');
            }
        },

        hasClass: function(el, className) {
            if (el.classList) {
                return el.classList.contains(className);
            } else {
                return new RegExp('(^| )' + className + '( |$)', 'gi').test(el.className);
            }
        },

        getClosest: function (elem, selector) {

            var firstChar = selector.charAt(0);

            // Get closest match
            for ( ; elem && elem !== document; elem = elem.parentNode ) {

                // If selector is a class
                if ( firstChar === '.' ) {
                    if ( elem.classList.contains( selector.substr(1) ) ) {
                        return elem;
                    }
                }

                // If selector is an ID
                if ( firstChar === '#' ) {
                    if ( elem.id === selector.substr(1) ) {
                        return elem;
                    }
                }

                // If selector is a data attribute
                if ( firstChar === '[' ) {
                    if ( elem.hasAttribute( selector.substr(1, selector.length - 2) ) ) {
                        return elem;
                    }
                }

                // If selector is a tag
                if ( elem.tagName.toLowerCase() === selector ) {
                    return elem;
                }

            }

            return false;
        }
    };

    // exports:
    nau.ready = ready;

    window.$ = $;
    window.$$ = $$;
    window.Vanilla = Vanilla;
}());