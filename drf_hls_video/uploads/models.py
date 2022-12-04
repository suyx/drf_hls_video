from django.db import models
from shared.models import UUIDModel
from django.core.validators import FileExtensionValidator
from accounts.models import User


VALID_VIDEO_EXTNS = ["mp4", "mov", "mkv", "avi", "m3u8", "webm"]  # Add additional formats here and create migration


class Upload(UUIDModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    video = models.FileField(upload_to="videos/", validators=[FileExtensionValidator(allowed_extensions=VALID_VIDEO_EXTNS)], null=True, blank=True)
    enable_hls = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, null=True, blank=True, related_name="liked_users")
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}, id: {self.id}"
