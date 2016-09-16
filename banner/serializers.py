from rest_framework import serializers
from banner.models import Banner


FULL_PATH = "http://api.zjnucloud.com/"


class BannerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Banner
        fields = ('id', 'image', 'href')
        extra_kwargs = {
            'url': {
                'view_name': 'image',
                'lookup_field': 'image'
            }
        }
