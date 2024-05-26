import queue
import threading
import time

from bilibili_api import sync
from dotenv import load_dotenv

import streamutil
from biliclient import get_monitor
from imageutil import add_message_to_html, capture_html_to_image
from qwen_assistant import generate_reply
from validate_env import check_env_vars

load_dotenv()

# Create a global queue
message_queue = queue.Queue()

# 初始化监听直播间弹幕
monitor = get_monitor()


# 推流到 Bilibili 直播间
def push_stream():
    # 构建推流内容
    while True:
        user_name, user_message, reply = message_queue.get(block=True)
        content = f"{user_name}：{user_message}\nAI：{reply}"
        print("Streaming content: ", content)
        html = add_message_to_html(user_name, user_message, reply)
        capture_html_to_image(html)
        time.sleep(0.2)


def write_first_message():
    first_message = "你好，我是一个可爱的魔法少女。请用弹幕跟我聊天吧。"
    html = add_message_to_html(None, None, first_message)
    capture_html_to_image(html)


@monitor.on("DANMU_MSG")
async def recv(event):
    # 弹幕文本
    user_message = event["data"]["info"][1]
    user_name = event["data"]["info"][2][1]
    print("msg is ", user_message)
    print("user is ", user_name)

    # 调用 assistant 生成回复
    reply = generate_reply(user_name, user_message)
    print(f"生成回复：{reply}")

    # 将对话内容推流到 Bilibili 直播间
    message_queue.put((user_name, user_message, reply))


if __name__ == "__main__":
    check_env_vars()

    stream_thread = threading.Thread(target=streamutil.start)
    stream_thread.daemon = True
    stream_thread.start()
    message_thread = threading.Thread(target=push_stream)
    message_thread.daemon = True
    message_thread.start()
    write_first_message()
    sync(monitor.connect())
