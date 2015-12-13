# Create your views here.
from rest_framework import generics
from speech.models import Speech, SpeechDetail
from speech.serializers import SpeechSerializer, SpeechDetailSerializer


class SpeechList(generics.ListAPIView):
    queryset = Speech.objects.all()
    serializer_class = SpeechSerializer


class SpeechSingle(generics.RetrieveAPIView):
    queryset = Speech.objects.all()
    serializer_class = SpeechSerializer


class SpeechDetailInfo(generics.RetrieveAPIView):
    queryset = SpeechDetail.objects.all()
    serializer_class = SpeechDetailSerializer
