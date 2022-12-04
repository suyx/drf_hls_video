from .utils import convert_to_hls


def task_convert_to_hls_video(upload):
    """
    Turn this into a celery task
    """
    convert_to_hls(upload)
