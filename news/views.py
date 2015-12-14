from rest_framework import generics

from news.serializers import *


# Create your views here.


class NewsViewSet(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = NewsTypeSerializer


class NewsZSXWList(generics.ListAPIView):
    """

    """
    queryset = ZSXW.objects.all()
    serializer_class = NewsZSXWSerializer


class NewsZSXWSingle(generics.RetrieveAPIView):
    """

    """
    queryset = ZSXW.objects.all()
    serializer_class = NewsZSXWSerializer


class NewsZSXWDetail(generics.RetrieveAPIView):
    """

    """
    queryset = ZSXWDetail.objects.all()
    serializer_class = NewsZSXWDetailSerializer


class NewsXSDTList(generics.ListAPIView):
    """

    """
    queryset = XSDT.objects.all()
    serializer_class = NewsXSDTSerializer


class NewsXSDTSingle(generics.RetrieveAPIView):
    """

    """
    queryset = XSDT.objects.all()
    serializer_class = NewsXSDTSerializer


class NewsXSDTDetail(generics.RetrieveAPIView):
    """

    """
    queryset = XSDTDetail.objects.all()
    serializer_class = NewsXSDTDetailSerializer


class NewsTZGGList(generics.ListAPIView):
    """

    """
    queryset = TZGG.objects.all()
    serializer_class = NewsTZGGSerializer


class NewsTZGGSingle(generics.RetrieveAPIView):
    """

    """
    queryset = TZGG.objects.all()
    serializer_class = NewsTZGGSerializer


class NewsTZGGDetail(generics.RetrieveAPIView):
    """

    """
    queryset = TZGGDetail.objects.all()
    serializer_class = NewsTZGGDetailSerializer


class NewsChuYangList(generics.ListAPIView):
    """

    """
    queryset = ChuYang.objects.all()
    serializer_class = NewsChuYangSerializer


class NewsChuYangSingle(generics.RetrieveAPIView):
    """

    """
    queryset = ChuYang.objects.all()
    serializers = NewsChuYangSerializer


class NewsChuYangDetail(generics.RetrieveAPIView):
    """

    """
    queryset = ChuYangDetail.objects.all()
    serializer_class = NewsChuYangDetailSerializer


