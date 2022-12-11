from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import HlsVideo
from .serializers import HlsVideoSerializer


class HlsVideoList(generics.ListAPIView):
    serializer_class = HlsVideoSerializer
    queryset = HlsVideo.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class HlsVideoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HlsVideoSerializer
    queryset = HlsVideo.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "id"
