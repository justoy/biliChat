import os
import ffmpeg
from dotenv import load_dotenv

load_dotenv()

FONT_FILE = 'NotoSansMonoCJKtc-Regular.otf'

rtm_url = os.environ.get("RTMP_BASE") + os.environ.get("RTMP_SUFFIX")


def stream_video(message_queue, rtmp_url):
    while True:
        # Block until a message is available
        text = message_queue.get()

        # Setup FFmpeg stream using the text
        background_input = ffmpeg.input('color=s=1280x720:d=3600:r=30:color=black', f='lavfi')
        video = ffmpeg.filter(background_input, 'drawtext', text=text, fontfile=FONT_FILE, fontsize=24,
                              fontcolor='white', x='(w-text_w)/2', y='h-100-t*30')
        stream = ffmpeg.output(video, rtmp_url, vcodec='libx264', pix_fmt='yuv420p', format='flv')

        # Execute streaming
        ffmpeg.run(stream)

        # Mark the message as processed
        message_queue.task_done()
