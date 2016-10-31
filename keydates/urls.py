from django.conf.urls import url
from keydates import views

urlpatterns = [
    url(r'^keydates/$', views.KeydatesList.as_view()),
    url(r'^keydates/version/$', views.KeydatesVersion.as_view())
]