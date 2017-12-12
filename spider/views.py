from .models import ReqestData, NmapList#, NmapContents
from .serializer import ReqNmapSerializer,NmapListSerializer#, NmapContentsSerializer
from rest_framework import generics

class ReqestDataView(generics.ListCreateAPIView):
    queryset = ReqestData.objects.all()
    serializer_class = ReqNmapSerializer

class NmapListView(generics.ListCreateAPIView):
    queryset = NmapList.objects.all()
    serializer_class = NmapListSerializer

# class NmapContentsView(generics.ListCreateAPIView):
#     queryset = NmapContents.objects.all()
#     serializer_class = NmapContentsSerializer


