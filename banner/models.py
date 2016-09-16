from django.db import models

# Create your models here.


class Banner(models.Model):
    id = models.IntegerField(primary_key=True,)
    image = models.CharField(max_length=255,)
    href = models.CharField(max_length=255,)

    class Meta:
        ordering = ('id', )
        db_table = 'banner'
