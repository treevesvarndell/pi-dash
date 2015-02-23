(function() {

    angular
        .module('app.dashboard')
        .service('DeparturesService', DeparturesService);

    DeparturesService.$inject = ['$http'];

    function DeparturesService($http) {
        var vm = this;

        var service = {
            getDepartures: getDepartures
        };

        return service;

        function getDepartures() {
            return $http.get('/api/departures')
                .then(getDeparturesComplete)
                .catch(function(message) {
                    console.log(message);
                }
            );

            function getDeparturesComplete(data, status, headers, config) {
                return data.data;
            }

        }
    }


})();