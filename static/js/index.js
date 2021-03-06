(function() {

    angular.module('app.dashboard', ['angularMoment', 'toggle-switch', 'rx']);

    angular.module('app.dashboard').constant('angularMomentConfig', {
        timezone: 'Europe/London',
        withoutSuffix: true
    });

    angular.module('app.dashboard').constant('tflApiConfig', {
        appId: '27dd0323',
        appKey: '4d68fa7d6da14a6bec23af0e5b453e5f',
        apiUrl: 'https://api.tfl.gov.uk/Line/dlr/Arrivals?stopPointId=940GZZDLEIN'
    });

    angular.module('app.dashboard').constant('amTimeAgoConfig', {
        withoutSuffix: true
    });

})();
