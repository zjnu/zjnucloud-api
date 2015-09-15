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
