from django.db import models
from django.contrib.postgres.fields import JSONField

class Tripster(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=20, blank=True, default='')
    pw = models.CharField(max_length=12, blank=True, default='')
    content = models.TextField()

    class Meta:
        ordering = ('created',)

# 수집한 데이터 json 형태로 저장
class Rawdata(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    list = JSONField()
    detail = JSONField()