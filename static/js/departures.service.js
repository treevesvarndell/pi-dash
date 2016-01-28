(function() {

    angular
        .module('app.dashboard')
        .service('DeparturesService', DeparturesService);

    DeparturesService.$inject = ['$http', 'tflApiConfig', 'rx'];

    function DeparturesService($http, tflApiConfig, rx) {
        var vm = this;

        var service = {
            getDepartures: getDepartures
        };

        return service;

        function getApiUrl() {
            return tflApiConfig.apiUrl + '&app_id=' + tflApiConfig.appId + '&app_key=' + tflApiConfig.appKey;
        }

        function getDepartures(direction) {
            return rx.Observable.fromPromise($http.get(getApiUrl()));
        }
    }


})();