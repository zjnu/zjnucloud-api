from rest_framework import generics
from news.models import Type, ZSXW
from news.serializers import NewsTypeSerializer, NewsZSXWSerializer

# Create your views here.


class NewsViewSet(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = NewsTypeSerializer


class NewsZSXWList(generics.ListAPIView):
    """

    """
    queryset = ZSXW.objects.all()
    serializer_class = NewsZSXWSerializer


class NewsZSXWDetail(generics.RetrieveAPIView):
    """

    """
    queryset = ZSXW.objects.all()
    serializer_class = NewsZSXWSerializer
