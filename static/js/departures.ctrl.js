(function () {

    angular
        .module('app.dashboard')
        .controller('DeparturesController', DeparturesController);

    DeparturesController.$inject = ['DeparturesService', 'rx'];

    function DeparturesController(departuresService, rx) {

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

        var trainsObservable = rx.Observable.interval(15000).startWith('testing').map(function() {
            vm.loading = true;
            return departuresService.getDepartures();
        });

        trainsObservable.forEach(function(ajaxObservable){

            ajaxObservable.subscribe(
                function(trains) {
                    var now = moment();

                    vm.departuresWest = [];
                    vm.departuresEast = [];

                    rx.Observable.from(trains.data).map(function(train) {

                        var secondsUntil = moment(train.expectedArrival).diff(now, 'seconds');

                        return {
                            direction: train.direction,
                            destination: train.destinationName.replace('DLR Station', ''),
                            secondsUntil: secondsUntil,
                            eta: train.expectedArrival,
                            willHeMakeIt: vm.generateWillHeMakeIt(secondsUntil)
                        };

                    }).forEach(function(train) {
//                        console.log(train);
                        train.direction === 'inbound' ? vm.departuresWest.push(train) : vm.departuresEast.push(train);
                    });

                },
                function(err) {
                    console.log('error:' + error)
                },
                function() {
                    vm.departuresWest = _.sortBy(vm.departuresWest, function(t) {
                        t.secondsUntil
                    });
                    vm.departuresEast = _.sortBy(vm.departuresEast, function(t) {
                        t.secondsUntil
                    });
                    vm.loading = false;
                }
            );
        });

        vm.generateWillHeMakeIt = function(secondsUntilTrain) {
            var willHeMakeIt = {};
            _.each(vm.willHeMakeIt, function (value, key) {
                var codedReturn = _.findKey(value, function (value) {
                    return secondsUntilTrain > value;
                });

                willHeMakeIt[key] = codedReturn ? codedReturn : 'n';
            });
            return willHeMakeIt;
        };

        vm.getFacebookProfileImageUrl = function (userId) {
            return '//graph.facebook.com/' + userId + '/picture?width=200';
        };

        vm.willMakeIt = function (code) {
            return code === 'y';
        };

        vm.mightMakeIt = function (code) {
            return code === 'm';
        };

        vm.wontMakeIt = function (code) {
            return code === 'n';
        };

    }


})();

