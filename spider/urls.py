from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # 클래스를 호출하고 해당클래스의 as_view() 함수를 호출
    url(r'^request', views.ReqestDataView.as_view()),
    url(r'^list', views.NmapListView.as_view()),
   # url(r'^contents', views.NmapContentsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)