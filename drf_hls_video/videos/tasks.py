from .utils import convert_to_hls
from drf_hls_video.celery import app


@app.task(ignore_result=True)
def task_convert_to_hls_video(upload):
    convert_to_hls(upload)
