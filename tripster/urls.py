from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from tripster import views

urlpatterns = [
    # 클래스를 호출하고 해당클래스의 as_view() 함수를 호출
    url(r'^$', views.TripsterList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.TripsterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)