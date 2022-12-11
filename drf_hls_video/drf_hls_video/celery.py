from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_hls_video.settings')
app = Celery("drf_hls_video")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
