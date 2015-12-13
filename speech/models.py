from django.db import models

# Create your models here.


class Speech(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, default='')
    date = models.CharField(max_length=16, default='')
    href = models.CharField(max_length=255, default='')
    pic = models.CharField(max_length=255, default='')
    overview = models.CharField(max_length=2048, default='')

    class Meta:
        ordering = ('-id',)
        db_table = 'speech'


class SpeechDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, default='')
    date = models.CharField(max_length=16, default='')
    content = models.TextField(default='')

    class Meta:
        ordering = ('-id', )
        db_table = 'speech_detail'
