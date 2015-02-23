(function() {

    angular
        .module('app.dashboard')
        .controller('DeparturesController', DeparturesController);

    DeparturesController.$inject = ['DeparturesService'];

    function DeparturesController(departuresService) {


        var vm = this;
//        vm.departuresService = DeparturesService;

        getDepartures();

        function getDepartures() {
            console.log(departuresService.getDepartures);
            return departuresService.getDepartures().then(function(data) {
                vm.departures = data;
                return vm.departures;
            })

        }

    }




})();

