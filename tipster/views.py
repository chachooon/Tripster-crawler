from tipster.models import Tipster
from tipster.serializers import TipsterSerializer
from rest_framework import generics

# generics 에 목록과 생성 API 가 정의되어 있다
class TipsterList(generics.ListCreateAPIView):
    queryset = Tipster.objects.all()
    serializer_class = TipsterSerializer

# generics 에 상세, 수정, 삭제 API가 정의되어 있다
class TipsterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipster.objects.all()
    serializer_class = TipsterSerializer
