from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from news import views

urlpatterns = [
    url(r'^news/$', views.NewsViewSet.as_view()),
    url(r'^news/zsxw/$', views.NewsZSXWList.as_view()),
    url(r'^news/zsxw/(?P<pk>[0-9]+)/$', views.NewsZSXWDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
