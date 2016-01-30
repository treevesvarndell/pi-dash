(function() {

    angular
        .module('app.dashboard')
        .service('ScreenService', ScreenService);

    ScreenService.$inject = ['$http', 'rx'];

    function ScreenService($http, rx) {
        var vm = this;

        var service = {
//            getScreenStatus: ,
            setScreen: setScreen
        };

        return service;

        function getApiUrl() {
            return tflApiConfig.apiUrl + '&app_id=' + tflApiConfig.appId + '&app_key=' + tflApiConfig.appKey;
        }

        function setScreen(action) {
            return rx.Observable.fromPromise($http.post(
                '/api/screen',
                {'action': action}
            ));
        }
    }


})();