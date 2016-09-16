from django.conf.urls import url
from banner import views

urlpatterns = [
    url(r'^banner/$', views.BannerList.as_view()),
    url(r'^banner/(?P<pk>[0-9]+)/$', views.BannerSingle.as_view())
]