from django.db import models as db


class Visitor(db.Model):
    ip = db.CharField(max_length=100, verbose_name='Ip')

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = verbose_name
