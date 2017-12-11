from .models import NmapRaw ,ReqestHistory
from .serializer import ReqNmapSerializer, NmapRawDataSerializer
from rest_framework import generics

class ReqestHistoryList(generics.ListCreateAPIView):
    queryset = ReqestHistory.objects.all()
    serializer_class = ReqNmapSerializer

class NmapRawDataList(generics.ListCreateAPIView):
    queryset = NmapRaw.objects.all()
    serializer_class = NmapRawDataSerializer



# class NmapList(generics.ListCreateAPIView):
#     queryset = NmapList.objects.all()
#     serializer_class = NmapListScrapable



