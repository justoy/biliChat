# biliChat

## Dependencies
1. Chrome
2. ffmpeg

## Env Variables
1. SESS_DATA - b站的cookie SESS_DATA
2. BILI_JCT - b站的cookie BILI_JCT
3. BUVID3 - b站的cookie BUVID3
4. ROOM_ID - b站的直播间号
5. DASHSCOPE_API_KEY - 通义千问的api key
6. RTMP_URL - b站直播间推流地址

## Run
`pip install -r requirements.txt`

`python main.py`

## Test with local live stream
1. start a local live stream server `docker run -d -p 1935:1935 -p 8080:80 --name nginx-rtmp tiangolo/nginx-rtmp`
2. open `rtmp://localhost/live/test`
3. `python main.py`