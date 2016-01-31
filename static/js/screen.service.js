(function() {

    angular
        .module('app.dashboard')
        .service('ScreenService', ScreenService);

    ScreenService.$inject = ['$http', 'rx'];

    function ScreenService($http, rx) {
        var vm = this;

        vm.screenApi = '/api/screen';

        var service = {
            getScreenStatus: getScreenStatus,
            setScreen: setScreen
        };

        return service;

        function getScreenStatus() {
            return rx.Observable.fromPromise($http.get(vm.screenApi));
        }

        function setScreen(action) {
            return rx.Observable.fromPromise($http.post(
                vm.screenApi,
                {'action': action}
            ));
        }
    }


})();