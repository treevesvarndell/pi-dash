(function() {

    angular
        .module('app.dashboard')
        .controller('DeparturesController', DeparturesController);


    function DeparturesController() {
        var vm = this;
        vm.departures = 'Departures from the controller...';

    }

//    DeparturesController.$inject = ['$scope'];



})();

