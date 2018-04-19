from django.contrib import admin
from django.conf.urls import url
from usermodels.api.views import RudCustomUserApiView,CreateCustomUserApiView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', RudCustomUserApiView.as_view(),name='rud'),
    url(r'^$', CreateCustomUserApiView.as_view(),name='create'),
]


