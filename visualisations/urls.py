from rest_framework import routers
from django.conf.urls import url, include,patterns
import views





urlpatterns = patterns('',
            url(r'api/offices/$',views.OfficesList.as_view()),
            url(r'api/offices/(?P<officeId>[0-9]+)$', views.SubOfficesList.as_view()),
            url(r'api/offices/(?P<officeId>[0-9]+)/(?P<year>[0-9]+)$', views.office_suboffices),
            url(r'index/', views.index),
        )