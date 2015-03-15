(function() {

    angular.module('app.dashboard', ['angularMoment', 'angularSpinner'])

    angular.module('app.dashboard').constant('angularMomentConfig', {
        timezone: 'Europe/London',
        withoutSuffix: true
    });

    angular.module('app.dashboard').constant('amTimeAgoConfig', {
        withoutSuffix: true
    });

})();
