from rest_framework import routers
from django.conf.urls import url, include,patterns
import views



router = routers.DefaultRouter()
router.register(r'api/offices', views.OfficeViewSet)


urlpatterns = patterns('',
            url(r'^', include(router.urls)),
            url(r'api/offices/(?P<officeId>[0-9]+)$', views.office_detail),
            url(r'api/offices/(?P<officeId>[0-9]+)/(?P<year>[0-9]+)$', views.office_suboffices),
            url(r'index/', views.index),
        )