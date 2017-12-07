from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from tripster import views

urlpatterns = [
    url(r'^$', views.tripster_list),
    url(r'^(?P<pk>[0-9]+)/$', views.tripster_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)