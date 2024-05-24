import os

from bilibili_api import Credential, Danmaku, sync
from bilibili_api.live import LiveDanmaku, LiveRoom
from dotenv import load_dotenv

load_dotenv()
# 设置 Bilibili 房间 ID 和凭证
ROOM_ID = int(os.environ.get("ROOM_ID"))

credential = Credential(
    sessdata=os.environ.get("SESS_DATA"),
    bili_jct=os.environ.get("BILI_JCT"),
    buvid3=os.environ.get("BUVID3"),
)

# 监听直播间弹幕
monitor = LiveDanmaku(ROOM_ID, credential=credential)


@monitor.on("DANMU_MSG")
async def recv(event):
    # 弹幕文本
    msg = event["data"]["info"][1]
    print("event is ", event)
    print("msg is ", msg)
    print("user is ", event["data"]["info"][2][1])


# 启动监听
sync(monitor.connect())
