from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # 클래스를 호출하고 해당클래스의 as_view() 함수를 호출
    url(r'^$', views.NmapRawDataList.as_view()),
    url(r'^req', views.ReqestHistoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)