from rest_framework import serializers
from news.models import Type
from news.models import ZSXW


class NewsTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'category', 'link')
        extra_kwargs = {
            'url': {'view_name': 'url', 'lookup_field': 'link'}
        }


class NewsZSXWSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZSXW
        fields = (
            'articleId',
            'title',
            'overview',
            'date',
            'author',
            'hits'
        )

