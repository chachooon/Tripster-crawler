from django.db import models
from django.contrib.postgres.fields import JSONField

class Timestampable(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class NmapRaw(Timestampable, models.Model):
    category = models.CharField(max_length=100)
    list = JSONField()
    contents = JSONField()

class ReqestHistory(Timestampable, models.Model):
    x = models.IntegerField()
    y = models.IntegerField()

# class NmapList(Timestampable, models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     x = models.IntegerField()
#     y = models.IntegerField()
#
#
# class NmapDetail(Timestampable, models.Model):
#     id = models.ForeignKey()
#     contents = JSONField()