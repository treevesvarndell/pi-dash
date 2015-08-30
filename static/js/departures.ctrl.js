(function() {

    angular
        .module('app.dashboard')
        .controller('DeparturesController', DeparturesController);

    DeparturesController.$inject = ['DeparturesService', '$timeout', 'usSpinnerService'];

    function DeparturesController(departuresService, $timeout, usSpinnerService) {

        var vm = this;
        vm.people = [
            532170073, //'mrman2289',
            641356236, //'Costelad',
            663655424 //'treevesvarndell'
        ];

        vm.willHeMakeIt = {
            532170073: { //mrman2289
                y: 300,
                m: 210,
                n: 180
            },
            641356236: { //Costelad
                y: 600,
                m: 480,
                n: 360
            },
            663655424: { //treevesvarndell
                y: 300,
                m: 210,
                n: 150
            }
        };

        (function getDepartures() {
            usSpinnerService.spin('departuresSpinner');

            function calculateWillHeMakeIt(trains) {

                var now = moment();
                for (i = 0; i < trains.length; i++) {

                    var currDeparture = trains[i];
                    currDeparture.willHeMakeIt = {};
                    currDeparture.secondsUntil = moment(currDeparture.eta).diff(now, 'seconds');

                    _.each(vm.willHeMakeIt, function(value, key) {
                        var codedReturn = _.findKey(value, function(value) {
                            return currDeparture.secondsUntil > value;
                        });

                        currDeparture.willHeMakeIt[key] = codedReturn ? codedReturn : 'n';

                    });

                    console.log(trains[i]);
                }

                return trains;
            }

            return departuresService.getDepartures().then(function(data) {

                var eastBoundTrains = _.filter(data, function(train) { return train.direction === 'east' });
                vm.departuresEast = calculateWillHeMakeIt(eastBoundTrains);
                console.log(vm.departuresEast);

                var westBoundTrains = _.filter(data, function(train) { return train.direction === 'west' });
                vm.departuresWest = calculateWillHeMakeIt(westBoundTrains);

                $timeout(getDepartures, 15000);
                usSpinnerService.stop('departuresSpinner');
                return vm.departures;
            });
        })();

        vm.getFacebookProfileImageUrl = function(userId) {
            return '//graph.facebook.com/' + userId + '/picture?width=200';
        };

        vm.willMakeIt = function(code) {
            return code === 'y';
        };

        vm.mightMakeIt = function(code) {
            return code === 'm';
        };

        vm.wontMakeIt = function(code) {
            return code === 'n';
        };

    }




})();

