from django.db import models
from uploads.models import Upload
from shared.models import UUIDModel


CONV_STATUS = [
        ('pend', 'Pending'),
        ('inpr', 'In Progress'),
        ('undf', 'Undefined'),
        ('done', 'Done')
]


class HlsVideo(UUIDModel):
    hls_video = models.FileField(upload_to="videos/tls/", null=True, blank=True)
    uploaded_video = models.ForeignKey(Upload, related_name="uploaded_video", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=4, default='ud', choices=CONV_STATUS)
