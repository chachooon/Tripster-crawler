from rest_framework import serializers
from .models import ReqestHistory, NmapRaw
from .spider import NmapRawScrapable

class ReqNmapSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReqestHistory
        fields = ('x', 'y')

    def create(self, validated_data):
        Nmap = NmapRawScrapable()
        Nmap.create(**validated_data)
        return ReqestHistory.objects.create(**validated_data)


class NmapRawDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = NmapRaw
        fields =('category', 'list', 'contents')

    def create(self, validated_date):
        return NmapRaw.objects.create(**validated_date)