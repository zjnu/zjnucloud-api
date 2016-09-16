# Create your views here.
from django.db.models.base import Model

from rest_framework import generics

from banner.models import Banner
from banner.serializers import BannerSerializer


class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerSingle(generics.RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
