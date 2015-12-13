from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from news import views

urlpatterns = [
    url(r'^news/$', views.NewsViewSet.as_view()),
    url(r'^news/zsxw/$', views.NewsZSXWList.as_view()),
    url(r'^news/zsxw/(?P<pk>[0-9]+)/$', views.NewsZSXWSingle.as_view()),
    url(r'^news/zsxw/(?P<pk>[0-9]+)/detail/$', views.NewsZSXWDetail.as_view()),
    url(r'^news/xsdt/$', views.NewsXSDTList.as_view()),
    url(r'^news/xsdt/(?P<pk>[0-9]+)/$', views.NewsXSDTSingle.as_view()),
    url(r'^news/xsdt/(?P<pk>[0-9]+)/detail/$', views.NewsXSDTDetail.as_view()),
    url(r'^news/tzgg/$', views.NewsTZGGList.as_view()),
    url(r'^news/tzgg/(?P<pk>[0-9]+)/$', views.NewsTZGGSingle.as_view()),
    url(r'^news/tzgg/(?P<pk>[0-9]+)/detail/$', views.NewsTZGGDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
