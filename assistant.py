# 设置 OpenAI API 密钥
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url=os.environ.get("OPENAI_PROXY_URL"),
)

# 队列用于存储用户弹幕和 OpenAI 回复
conversation_history = [
    {"role": "system",
     "content": "你是一个ai主播。你正在b站直播间和b友们对话。你的设定是一个古灵精怪的美少女魔法师，喜欢对人冷嘲热讽，但是内心善良。不要使用emoji，但可以使用颜文字"}
]


def generate_reply(user_name, user_message):
    # Append the user's message to the conversation history
    conversation_history.append({"role": "user", "content": f"{user_name}: {user_message}"})

    # Generate the reply from OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o",  # Change to the appropriate model you have access to
        messages=conversation_history
    )

    # Extract the reply message
    ai_reply = completion.choices[0].message  # Adjust according to actual API response structure

    # Append AI's reply to the conversation
    if ai_reply.content is not None:
        conversation_history.append({"role": "assistant", "content": ai_reply.content})

    return ai_reply.content
