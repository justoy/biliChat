import os

from bilibili_api import Credential, sync
from bilibili_api.live import LiveDanmaku
from dotenv import load_dotenv

load_dotenv()

# 设置 Bilibili 房间 ID 和凭证
room_id = int(os.environ.get("ROOM_ID"))
credential = Credential(
    sessdata=os.environ.get("SESS_DATA"),
    bili_jct=os.environ.get("BILI_JCT"),
    buvid3=os.environ.get("BUVID3"),
)


def get_monitor():
    return LiveDanmaku(room_id, credential=credential)


if __name__ == '__main__':
    monitor = get_monitor()


    @monitor.on("DANMU_MSG")
    async def recv(event):
        # 弹幕文本
        msg = event["data"]["info"][1]
        print("event is ", event)
        print("msg is ", msg)
        print("user is ", event["data"]["info"][2][1])


    sync(monitor.connect())
