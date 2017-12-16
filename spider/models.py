from django.db import models
from django.contrib.postgres.fields import JSONField

class Timestampable(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ReqestData(Timestampable, models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    max = models.IntegerField()

class NmapList(Timestampable, models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    x = models.DecimalField(max_digits=10, decimal_places=7)
    y = models.DecimalField(max_digits=10, decimal_places=7)
    contents = JSONField(null=True)

class NmapBoundaryList(Timestampable, models.Model):
    boundary = models.CharField(max_length=100)

# class NmapContents(Timestampable, models.Model):
#     cid = models.ForeignKey(NmapList, on_delete=models.CASCADE)
#     contents = JSONField()
