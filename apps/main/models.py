from django.db import models as db


class Visitor(db.Model):
    ip = db.CharField(max_length=100, verbose_name='Ip')
    url = db.CharField(max_length=100, verbose_name='url')

    class Meta:
        verbose_name = 'Visitors'
        verbose_name_plural = verbose_name
