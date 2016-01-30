(function() {

    angular
        .module('app.dashboard')
        .controller('ScreenToggleCtrl', ScreenToggleCtrl);

    ScreenToggleCtrl.$inject = ['ScreenService'];

    function ScreenToggleCtrl(screenService) {
        this.screenService = screenService;
        this.screenStatus = true;

        var vm = this;

        this.toggleScreen = function() {

            var action = vm.screenStatus ? 'on' : 'off';

            vm.screenService = screenService.setScreen(action);
        }
    }

})();