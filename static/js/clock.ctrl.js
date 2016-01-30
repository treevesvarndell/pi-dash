(function() {

    angular
        .module('app.dashboard')
        .controller('ClockCtrl', ClockCtrl);

    ClockCtrl.$inject = ['$timeout'];

    function ClockCtrl($timeout) {
        this.clock = ""; // initialise the time variable
        this.tickInterval = 1000 //ms

        var vm = this;

        var tick = function() {
            vm.clock = Date.now() // get the current time
            $timeout(tick, vm.tickInterval); // reset the timer
        }

        // Start the timer
        $timeout(tick, vm.tickInterval);
    }

})();