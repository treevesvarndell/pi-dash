(function () {

    angular
        .module('app.dashboard')
        .controller('WeatherCtrl', WeatherCtrl);

    WeatherCtrl.$inject = ['$http', '$interval'];

    function WeatherCtrl($http, $interval) {
        var vm = this;

        function getWeather() {
            $http.get("http://api.openweathermap.org/data/2.5/weather?lat=51.508&lon=0&appid=44db6a862fba0b067b1930da0d769e98")
                .success(function (data) {
                    vm.temp = _.floor(data.main.temp - 273.15);
                    vm.weather = data.weather[0].description;
                    vm.humidity = data.main.humidity;
                    vm.wind = _.floor(data.wind.speed);
                })
        }

        getWeather();
        $interval(getWeather, 1800000, 0);
    }
})();
