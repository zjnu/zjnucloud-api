from django.db import models

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=32, default='')
    link = models.CharField(max_length=255, default='')


class ZSXW(models.Model):
    articleId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, default='')
    date = models.CharField(max_length=255, default='')
    overview = models.CharField(max_length=2048, blank=True, default='')
    author = models.CharField(max_length=255, default='')
    hits = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ('-articleId',)


class ZSXWDetail(models.Model):
    articleId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, default='')
    date = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=255, default='')
    deptname = models.CharField(max_length=255, default='')
    videolink = models.CharField(max_length=255, default='')
    videocover = models.CharField(max_length=255, default='')
    content = models.TextField(default='')

    class Meta:
        ordering = ('-articleId',)
        db_table = 'news_zsxw_detail'


class XSDT(models.Model):
    articleId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, default='')
    date = models.CharField(max_length=255, default='')
    overview = models.CharField(max_length=2048, blank=True, default='')
    author = models.CharField(max_length=255, default='')
    hits = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ('-articleId',)


class XSDTDetail(models.Model):
    articleId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, default='')
    date = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=255, default='')
    deptname = models.CharField(max_length=255, default='')
    videolink = models.CharField(max_length=255, default='')
    videocover = models.CharField(max_length=255, default='')
    content = models.TextField(default='')

    class Meta:
        ordering = ('-articleId',)
        db_table = 'news_xsdt_detail'


class TZGG(models.Model):
    articleId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, default='')
    date = models.CharField(max_length=255, default='')
    overview = models.CharField(max_length=2048, blank=True, default='')
    author = models.CharField(max_length=255, default='')
    hits = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ('-articleId',)
        db_table = 'news_tzgg'


class TZGGDetail(models.Model):
    articleId = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, default='')
    date = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=255, default='')
    deptname = models.CharField(max_length=255, default='')
    content = models.TextField(default='')

    class Meta:
        ordering = ('-articleId',)
        db_table = 'news_tzgg_detail'
