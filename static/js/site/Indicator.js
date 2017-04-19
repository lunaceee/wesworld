/* Â© 2015 NauStud.io
 * @author Tran Trong Thanh Tung
 */
var nau = nau || {};

(function() {
    'use strict';

    var Indicator = {
        $el: null,
        timeline: null,
        labelList: [],

        init: function(tl) {
            var $el = this.$el = $('.js-indicator');
            this.timeline = tl;
            if (this.$el === null) {
                return;
            }
            var labelList = tl.getLabelsArray();
            this.labelList = labelList;
            // console.log('labelList', labelList);
            labelList.forEach(function(element) {
                $el.innerHTML += '<li class="indicator__item"><a href="javascript:void(0)" title="' + element.name + '" data-label="' + element.name + '"></a></li>';


            });

            $$('.indicator__item').forEach(function(element, index) {
                element.querySelector('a').addEventListener('click', function() {
                    var scrollTop = (labelList[index].time + 0.25) / tl.duration() * (11000 + (1000 - window.innerHeight));
                    TweenLite.to(window, 2, {scrollTo: {y: scrollTop}, ease:Power2.easeOut});
                });
            });
        },

        updateIndicator: function(progress) {
            var time = this.timeline.duration() * progress;
            var $el = this.$el;
            for (var i = 0; i < this.labelList.length; i++) {
                if (this.labelList[i].time > time) {
                    $$('.indicator__item').forEach(function(element) {
                        Vanilla.removeClass(element, 'active');

                    });
                    Vanilla.addClass($el.querySelector('li:nth-child(' + i + ')'), 'active');
                    return;
                }
                $$('.indicator__item').forEach(function(element) {
                    Vanilla.removeClass(element, 'active');
                });
                Vanilla.addClass($el.querySelector('li:last-child'), 'active');
            }
        }

    };
    //export
    nau.Indicator = Indicator;

}());