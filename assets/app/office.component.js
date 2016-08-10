angular.
  module('officeDetail').
  component('officeDetail', {
    templateUrl: '/assets/app/components/offices.template.html',
    controller: ['$scope','$http',
      function PhoneListController($scope, $http) {
            $http.get('/api/offices/').then(function(response) {
            $scope.offices = response.data.results;
      });
}
    ]
  });
