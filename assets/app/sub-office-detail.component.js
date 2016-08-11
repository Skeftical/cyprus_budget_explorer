angular.module('subOfficeDetail').component('subOfficeDetail', {
    templateUrl: '/assets/app/components/suboffices.template.html',
    controller: ['$scope', '$http', '$routeParams',
        function PhoneDetailController($scope, $http, $routeParams) {
            var self = this;

            $http.get('/api/offices/' + $routeParams.officeId).then(function (response) {
                self.offices = response.data;
                self.year = 2014;
                self.setData = function setData(index) {
                    subOffice = self.offices[index];
                    self.pagio = subOffice.pagio;
                    self.taktikes = subOffice.taktikes;
                    self.anaptuksiakes = subOffice.anaptuksiakes;
                };

            });


        }
    ]
});