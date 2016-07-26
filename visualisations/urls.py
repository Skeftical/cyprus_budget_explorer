from rest_framework import routers
from django.conf.urls import url, include,patterns

import views



router = routers.DefaultRouter()
router.register(r'offices', views.OfficeViewSet)


urlpatterns = patterns('',
            url(r'^', include(router.urls)),
            url(r'^offices/(?P<officeId>[0-9]+)$', views.office_detail),
        )