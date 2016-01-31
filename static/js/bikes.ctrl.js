(function () {

    angular
        .module('app.dashboard')
        .controller('BikesCtrl', BikesCtrl);

    BikesCtrl.$inject = ['$http', '$interval'];

    function BikesCtrl($http, $interval) {
        var vm = this;

        function getBikes() {
            $http.get("https://api-prod6.tfl.gov.uk/Place/BikePoints_547")
                .success(function (data) {
                    vm.numberOfBikes = data.additionalProperties.filter(availableBikes)[0].value;
                    vm.numberOfSlots = data.additionalProperties.filter(spareDocks)[0].value;
                })

        }

        function availableBikes(obj) {
            if (obj.key === "NbBikes") {
                return true;
            }
        }

        function spareDocks(obj) {
            if (obj.key === "NbEmptyDocks") {
                return true;
            }
        }
        getBikes();
        $interval(getBikes, 15000, 0);
    }
})();
