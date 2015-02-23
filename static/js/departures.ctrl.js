(function() {

    angular
        .module('app.dashboard')
        .controller('DeparturesController', DeparturesController);

    DeparturesController.$inject = ['DeparturesService', '$timeout', 'usSpinnerService'];

    function DeparturesController(departuresService, $timeout, usSpinnerService) {

        var vm = this;

        (function getDepartures() {
            usSpinnerService.spin('departuresSpinner');
            return departuresService.getDepartures().then(function(data) {
                console.log(data);
                vm.departures = data;
                $timeout(getDepartures, 15000);
                usSpinnerService.stop('departuresSpinner');
                return vm.departures;
            });
        })();

    }




})();

