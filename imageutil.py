import os
import time
from collections import deque

from html2image import Html2Image

hti = Html2Image(output_path=os.path.join(os.getcwd(), 'output'), temp_path='./tmp')
msg_history = deque()

with open('chat_ui/index.html', 'r') as file:
    html_lines = file.readlines()
    # Find the position to insert the new message
    insert_position = html_lines.index('        </div>\n')


# Function to add a message to the HTML file
def add_message_to_html(user_name, user_message, reply):
    user_message_div = f'            <div class="message user">{user_message} - ({user_name})</div>\n'
    assistant_message_div = f'            <div class="message">{reply}</div>\n'
    msg_history.append(user_message_div)
    msg_history.append(assistant_message_div)

    while len(msg_history) > 10:
        msg_history.popleft()

    html_lines_copy = html_lines.copy()
    i = insert_position
    for message in msg_history:
        html_lines_copy.insert(i, message)
        i += 1
    return html_lines_copy


# Function to capture the HTML as an image
def capture_html_to_image(html):
    hti.screenshot(html_str=" ".join(html), size=(1280, 720), save_as='screenshot.jpg')


if __name__ == '__main__':
    messages = [
        ("user", "Hello!", "第一条"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "你好"),
        ("user", "how are you!", "吃了吗🐶"),
        ("user", "Hello!", "最后一条"),
    ]

    for user_name, user_message, reply in messages:
        html = add_message_to_html(user_name, user_message, reply)
        time.sleep(0.2)  # Simulate delay
        capture_html_to_image(html)
