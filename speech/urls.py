from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from speech import views

urlpatterns = [
    url(r'^speech/$', views.SpeechList.as_view()),
    url(r'^speech/(?P<pk>[0-9]+)/$', views.SpeechSingle.as_view()),
    url(r'^speech/(?P<pk>[0-9]+)/detail/$', views.SpeechDetailInfo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
