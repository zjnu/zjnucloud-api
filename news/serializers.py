from rest_framework import serializers
from news.models import Type, ZSXW, ZSXWDetail, XSDT, XSDTDetail, TZGG, TZGGDetail, ChuYang, ChuYangDetail


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


class NewsZSXWDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZSXWDetail
        fields = (
            'articleId',
            'title',
            'date',
            'author',
            'deptname',
            'videolink',
            'videocover',
            'content'
        )


class NewsXSDTSerializer(serializers.ModelSerializer):
    class Meta:
        model = XSDT
        fields = (
            'articleId',
            'title',
            'overview',
            'date',
            'author',
            'hits'
        )


class NewsXSDTDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = XSDTDetail
        fields = (
            'articleId',
            'title',
            'date',
            'author',
            'deptname',
            'videolink',
            'videocover',
            'content'
        )


class NewsTZGGSerializer(serializers.ModelSerializer):
    class Meta:
        model = TZGG
        fields = (
            'articleId',
            'title',
            'overview',
            'date',
            'author',
            'hits'
        )


class NewsTZGGDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TZGGDetail
        fields = (
            'articleId',
            'title',
            'date',
            'author',
            'deptname',
            'content'
        )

class NewsChuYangSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChuYang
        fields = (
            'articleId',
            'title',
            'date'
        )

class NewsChuYangDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChuYangDetail
        fields = (
            'articleId',
            'title',
            'date',
            'author',
            'content'
        )
