(function() {

    angular
        .module('app.dashboard')
        .controller('DeparturesController', DeparturesController);

    DeparturesController.$inject = ['DeparturesService', '$timeout', 'usSpinnerService'];

    function DeparturesController(departuresService, $timeout, usSpinnerService) {

        var vm = this;
        vm.people = ['mrman2289', 'Costelad', 'treevesvarndell'];


        (function getDepartures() {
            usSpinnerService.spin('departuresSpinner');
            return departuresService.getDepartures().then(function(data) {
                console.log(data);
                vm.departuresEast = _.filter(data, function(train) { return train.direction === 'east' });
                vm.departuresWest = _.filter(data, function(train) { return train.direction === 'west' });
                $timeout(getDepartures, 15000);
                usSpinnerService.stop('departuresSpinner');
                return vm.departures;
            });
        })();

        vm.getFacebookProfileImageUrl = function(username) {
            return '//graph.facebook.com/' + username + '/picture?width=200';
        }

    }




})();

