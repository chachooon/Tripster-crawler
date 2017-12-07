# 클래스 기반의 Rest CRUD 처리
from tripster.models import Tripster
from tripster.serializers import TripsterSerializer
from rest_framework import generics

# generics 에 목록과 생성 API 가 정의되어 있다
class TripsterList(generics.ListCreateAPIView):
    queryset = Tripster.objects.all()
    serializer_class = TripsterSerializer

# generics 에 상세, 수정, 삭제 API가 정의되어 있다
class TripsterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tripster.objects.all()
    serializer_class = TripsterSerializer