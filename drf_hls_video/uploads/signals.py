from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from videos.tasks import task_convert_to_hls_video
from .models import Upload


@receiver(post_save, sender=Upload)
def create_hls(sender, created, instance, **kwargs):
    if instance.video:
        if (created and instance.enable_hls) or (instance.enable_hls and not instance.uploaded_video.all()):
            task_convert_to_hls_video.delay(instance.id)
