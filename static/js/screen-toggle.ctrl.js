(function() {

    angular
        .module('app.dashboard')
        .controller('ScreenToggleCtrl', ScreenToggleCtrl);

    ScreenToggleCtrl.$inject = ['ScreenService', '$timeout'];

    function ScreenToggleCtrl(screenService, $timeout) {
        this.screenService = screenService;
        this.screenStatus = false;
        this.loading = true;
        this.error = false;

        var vm = this;

        var screenStatus = screenService.getScreenStatus();

        screenStatus.subscribe(function(status) {
            var status = status.data.status;

            vm.loading = false;

            if (status == 'on') {
                vm.screenStatus = true;

            } else if (status == 'off') {
                vm.screenStatus = false;

            } else if (status == 'error') {
                vm.error = true;
            }

        });

        this.toggleScreen = function() {

            var action = vm.screenStatus ? 'on' : 'off';

            screenService.setScreen(action).subscribe(function(response) {
                var state = response.data.success ? ' successful ' : ' failed';
                vm.message = 'Request to turn screen ' + action + state;

                $timeout(function() {
                    vm.message = false;
                }, 6000);
            });
        }
    }

})();