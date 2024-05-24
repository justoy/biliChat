import os

from bilibili_api import Credential
from bilibili_api.live import LiveDanmaku
from dotenv import load_dotenv

load_dotenv()

# 设置 Bilibili 房间 ID 和凭证
room_id = int(os.environ.get("ROOM_ID"))

rtm_url = os.environ.get("RTMP_BASE") + os.environ.get("RTMP_SUFFIX")
credential = Credential(
    sessdata=os.environ.get("SESS_DATA"),
    bili_jct=os.environ.get("BILI_JCT"),
    buvid3=os.environ.get("BUVID3"),
)


def get_monitor():
    return LiveDanmaku(room_id, credential=credential)
