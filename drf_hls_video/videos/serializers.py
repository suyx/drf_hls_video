from rest_framework import serializers
from uploads.serializers import UploadSerializer


class HlsVideoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    uploaded_video = UploadSerializer(read_only=False)
    hls_video = serializers.FileField(read_only=True)
    status = serializers.CharField(read_only=True)
