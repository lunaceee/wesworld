var nau = nau || {};

(function() {
    'use strict';

    var HeroBannerAnimation = {
        timeline: null,

        addHeroBannerComponent: function(timeline) {
            var $el = $('.js-header-global');
            // var  $rectLine1 = $('#header-rect-line-1');
            // var  $rectLine2 = $('#header-rect-line-2');
            // var  $rectLine3 = $('#header-rect-line-3');
            // var  $rectLine4 = $('#header-rect-line-4');
            // var $text = $('.js-header-global__text');
            // var $scroll = $('.js-header-global__scroll');
            var $navBar = $('.js-nav-bar-desktop');
            this.timeline = timeline;

            // this.timeline.set($rectLine1, {'stroke-dashoffset': 170}, 0);
            // this.timeline.set($rectLine4, {'stroke-dashoffset': 170}, 0);
            // this.timeline.set($rectLine2, {'stroke-dashoffset': 270}, 0);
            // this.timeline.set($rectLine3, {'stroke-dashoffset': 270}, 0);
            // this.timeline.set($text, {opacity: 0}, 0);
            // this.timeline.set($navBar, {pointerEvents: 'none'}, 0);

            // this.timeline.to($rectLine1, 0.5, {'stroke-dashoffset': 0}, 0);
            // this.timeline.to($rectLine2, 0.5, {'stroke-dashoffset': 0}, 0);
            // this.timeline.to($text, 0, {'opacity': 1}, 0.25);
            // this.timeline.to($rectLine3, 0.5, {'stroke-dashoffset': 0}, 0.5);
            // this.timeline.to($rectLine4, 0.5, {'stroke-dashoffset': 0}, 0.5);
            // this.timeline.to($el, 2.5, {'top' : '-200%'}, 1);
            // this.timeline.to($text, 1.35, {'margin-top' : '-30rem'}, 1);
            // this.timeline.to($scroll, 1.5, {'bottom' : '15rem'}, 1);
            this.timeline.set($navBar, {className: '+=fixed'}, 0.25);
            // this.timeline.set($navBar, {pointerEvents: 'all'}, 0.25);

            // auto animate
            setTimeout(function() {
                Vanilla.addClass($el, 'showed');
            }, 1100);

            this.timeline.set($el, {'top' : '0'}, 0);
            this.timeline.to($el, 0.5, {'top' : '-200%'}, 0);
            return 0.25;
        }
    };

    nau.HeroBannerAnimation = HeroBannerAnimation;
}());