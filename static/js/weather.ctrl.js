(function () {

    angular
        .module('app.dashboard')
        .controller('WeatherCtrl', WeatherCtrl);

    WeatherCtrl.$inject = ['$http', '$interval'];

    function WeatherCtrl($http, $interval) {
        var vm = this;

        var weatherTypes = {
            0: "Clear night",
            1: "Sunny day",
            2: "Partly cloudy",
            3: "Partly cloudy",
            4: "Not used",
            5: "Mist",
            6: "Fog",
            7: "Cloudy",
            8: "Overcast",
            9: "Light rain shower",
            10: "Light rain shower",
            11: "Drizzle",
            12: "Light rain",
            13: "Heavy rain shower",
            14: "Heavy rain shower",
            15: "Heavy rain",
            16: "Sleet shower",
            17: "Sleet shower",
            18: "Sleet",
            19: "Hail shower",
            20: "Hail shower",
            21: "Hail",
            22: "Light snow shower",
            23: "Light snow shower",
            24: "Light snow",
            25: "Heavy snow shower",
            26: "Heavy snow shower",
            27: "Heavy snow",
            28: "Thunder shower",
            29: "Thunder shower",
            30: "Thunder"
        };

        function getForecastForDay() {
            $http.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354377?res=daily&key=9e3d027e-1771-42cf-bf59-4dce5989f4e3")
                .success(function (data) {
                    var forecast = data.SiteRep.DV.Location.Period[0].Rep[0];

                    vm._feelsLikeMax = forecast.FDm;
                    vm._dayMax = forecast.Dm;
                    vm._gustSpeed = forecast.Gn;

                    vm._windSpeed = forecast.S;
                    vm._precProb = forecast.PPd;
                    vm._weatherType = weatherTypes[forecast.W];
                });
        }

        function getWeatherNow() {
            $http.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/354377?res=3hourly&key=9e3d027e-1771-42cf-bf59-4dce5989f4e3")
                .success(function (data) {
                    var forecast = data.SiteRep.DV.Location.Period[0].Rep[0];
                    vm._temperature = forecast.T;
                    vm._feelsLike = forecast.F;
                });
        }

        getForecastForDay();
        getWeatherNow();
        $interval(getWeatherNow, 1800000, 0);
        $interval(getForecastForDay, 3600000, 0);
    }
})();
