from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from videos.tasks import convert_to_hls
from .models import Upload


@receiver(post_save, sender=Upload)
def create_hls(sender, created, instance, **kwargs):
    print(created, instance.enable_hls, instance.uploaded_video.all())
    if instance.video:
        if (created and instance.enable_hls) or (instance.enable_hls and not instance.uploaded_video.all()):
            convert_to_hls(instance)
