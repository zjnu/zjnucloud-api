from rest_framework import serializers
from speech.models import Speech, SpeechDetail

__author__ = 'ddMax'


class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech
        fields = (
            'id',
            'title',
            'date',
            'href',
            'pic',
            'overview',
        )


class SpeechDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechDetail
        fields = (
            'id',
            'title',
            'date',
            'content',
        )
