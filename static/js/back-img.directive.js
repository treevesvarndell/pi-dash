(function() {

    angular
        .module('app.dashboard')
        .directive('backgroundImage', BackgroundImage);

        function BackgroundImage() {
            return function(scope, element, attrs) {
                var url = attrs.backgroundImage;
                element.css({
                    'background-image': 'url(' + url +')',
                    'background-size' : 'cover'
                });
            };
        }
})();