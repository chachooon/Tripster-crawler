from rest_framework import serializers
from .models import ReqestData, NmapList#, NmapContents
from . import spider

class ReqNmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReqestData
        fields = ('x', 'y','max')

    def create(self, validated_data):
        spider.start()
        return ReqestData.objects.create(**validated_data)


class NmapListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NmapList
        fields = ('id', 'name', 'category', 'x', 'y','contents')

    def create(self,validated_date):
        return NmapList.objects.create(**validated_date)

    def update(self, instance, validated_date):
        instance.id = validated_date.get('id', instance.id)
        instance.name = validated_date.get('name', instance.name)
        instance.category = validated_date.get('category', instance.category)
        instance.x = validated_date.get('x', instance.x)
        instance.y = validated_date.get('y', instance.y)
        instance.save()
        return instance


# class NmapContentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NmapContents
#         fields = ('cid', 'contents')
#
#     def create(self,validated_date):
#         return NmapContents.objects.create(**validated_date)
#
#     def update(self, instance, validated_date):
#         instance.cid = validated_date.get('cid', instance.cid)
#         instance.contents = validated_date.get('contents', instance.contents)
#         instance.save()
#         return instance