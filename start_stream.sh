#!/usr/bin/env bash
# https://stackoverflow.com/questions/71861295/using-ffmpeg-jpg-to-mp4-to-mpegts-play-with-hls-m3u8-only-first-ts-file-plays/71885708#71885708
RTMP_URL='rtmp://localhost/live/streamkey'

ffmpeg -re -f image2  -loop 1 -fflags +genpts -i output/screenshot.jpg -f fifo -attempt_recovery 1 -recovery_wait_time 1  -f flv $RTMP_URL