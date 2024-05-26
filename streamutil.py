import os
import time

import cv2
import subprocess
import queue
import threading

from dotenv import load_dotenv

load_dotenv()
rtmp_url = os.environ.get("RTMP_URL")


# Function to produce images
def produce_frame(image_queue: queue):
    while True:
        # Generate or capture an image
        img = cv2.imread('output/screenshot.jpg')
        if img is not None:
            image_queue.put(img)
        time.sleep(0.033)  # 30 fps


def consume_frame(image_queue):
    # Consume remaining images from the queue and write to ffmpeg's stdin
    # Wait for the first image to get its size
    frame = image_queue.get(block=True)
    # Define the command to pipe frames to ffmpeg with the actual image size
    height, width, _ = frame.shape
    ffmpeg_command = [
        'ffmpeg',
        '-y',  # overwrite output files
        '-f', 'rawvideo',  # input format
        '-vcodec', 'rawvideo',  # input codec
        '-pix_fmt', 'bgr24',  # input pixel format
        '-s', f'{width}x{height}',  # input size
        '-r', '30',  # 30fps
        '-i', '-',  # input from stdin
        '-c:v', 'libx264',  # output codec
        '-pix_fmt', 'yuv420p',  # output pixel format
        '-preset', 'veryfast',  # output preset
        '-f', 'flv',  # output format
        rtmp_url
    ]
    process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)
    while True:
        # Write the frame to ffmpeg's stdin
        process.stdin.write(frame.tobytes())
        frame = image_queue.get(block=True)


def start():
    image_queue = queue.Queue()
    # Start the image producer in a separate thread
    producer_thread = threading.Thread(target=produce_frame, args=(image_queue,))
    producer_thread.daemon = True
    producer_thread.start()
    consume_frame(image_queue)


if __name__ == "__main__":
    start()
