import queue
import threading

from bilibili_api import sync

from biliclient import get_monitor
from imageutil import add_message_to_html, capture_html_to_image
from qwen_assistant import generate_reply

# Create a global queue
message_queue = queue.Queue()

# 初始化监听直播间弹幕
monitor = get_monitor()


# 推流到 Bilibili 直播间
def push_stream(user_name, user_message, reply):
    # 构建推流内容
    content = f"{user_name}：{user_message}\nAI：{reply}"
    print("Streaming content: ", content)
    html = add_message_to_html(user_name, user_message, reply)
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
    push_stream(user_name, user_message, reply)

if __name__ == "__main__":
    sync(monitor.connect())

