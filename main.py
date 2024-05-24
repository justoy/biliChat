import os
import queue

from bilibili_api import Credential, sync
from bilibili_api.live import LiveDanmaku

from openai import OpenAI
from dotenv import load_dotenv

from assistant import generate_reply
from biliclient import get_monitor
from streamutil import stream_video


# Create a global queue
message_queue = queue.Queue()

# 初始化监听直播间弹幕
monitor = get_monitor()


# 推流到 Bilibili 直播间
def push_stream(user_name, user_message, reply):
    # 构建推流内容
    content = f"{user_name}：{user_message}\nAI：{reply}"
    print("content is ", content)
    stream_video(content)


@monitor.on("DANMU_MSG")
async def recv(event):
    # 弹幕文本
    user_message = event["data"]["info"][1]
    user_name = event["data"]["info"][2][1]
    print("event is ", event)
    print("msg is ", user_message)
    print("user is ", user_name)

    # 调用 OpenAI API 生成回复
    reply = generate_reply(user_name, user_message)
    print(f"生成回复：{reply}")

    # 将对话内容推流到 Bilibili 直播间
    push_stream(user_name, user_message, reply)


# 启动监听
sync(monitor.connect())
