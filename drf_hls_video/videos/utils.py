from moviepy.editor import VideoFileClip
import ffmpeg_streaming
from ffmpeg_streaming import Formats
from .models import HlsVideo
from uploads.models import Upload


def convert_to_hls(video):
    hls_video = HlsVideo.objects.create(
        status="inpr"
    )  # create an object with 'in progress' status
    video = Upload.objects.get(id=video)
    temp_clip = VideoFileClip("{}".format(video.video.path))
    if temp_clip.rotation == 90:
        temp_clip = temp_clip.resize(temp_clip.size[::-1])
        temp_clip.rotation = 0
    #  convert any video format to mp4
    temp_clip.write_videofile("{}final.mp4".format(video.id), codec="libx264", audio_codec="libmp3lame")
    temp_clip.close()
    temp_video = "{}final.mp4".format(video.id)
    stream_video = ffmpeg_streaming.input(temp_video)
    hls = stream_video.hls(Formats.h264())
    hls.auto_generate_representations()
    hls.output(f"/media/videos/hls/{video.id}/{video.id}.m3u8")
    local = f"/videos/hls/{video.id}/{video.id}.m3u8"
    hls_video.hls_video = local
    hls_video.uploaded_video = video
    hls_video.status = "done"
    hls_video.save()
