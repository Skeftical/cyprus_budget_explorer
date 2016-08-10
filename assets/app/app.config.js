angular.
  module('phonecatApp').
  config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/offices/:officeId', {
          template: '<sub-office-detail></sub-office-detail>'
        }).
      when('/offices/', {
          template: '<office-detail></office-detail>'
        }).
          when('/#myModal', {
        template:'<modal></modal>'
      }).
        otherwise('/offices');
    }
  ]);