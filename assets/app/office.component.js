angular.
  module('officeDetail').
  component('officeDetail', {
    templateUrl: '/assets/app/components/offices.template.html',
    controller: ['$scope','$http',
      function PhoneListController($scope, $http) {
          var self = this;
            $http.get('/api/offices/').then(function(response) {
            $scope.offices = response.data;
            self.year=2014
      });
}
    ]
  });
