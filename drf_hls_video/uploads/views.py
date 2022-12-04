from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UploadSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from accounts.models import User
from .models import Upload


class UploadView(generics.ListCreateAPIView):
    """
    Create and list uplaods
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UploadSerializer
    parser_classes = (FormParser, MultiPartParser)  # to support file uploads
    queryset = Upload.objects.all()

    def post(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            uploaded_by = User.objects.get(id=request.user.id)  # override uploaded user here
            serializer.validated_data['uploaded_by'] = uploaded_by
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class UploadDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update and destroy view
    """
    lookup_field = "id"
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()
    # TODO create custom perms to only allow editing by owners
    permission_classes = [IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
