# 设置 OpenAI API 密钥
import os

from dotenv import load_dotenv
from openai import OpenAI

from assistant_helper import SYSTEM_PROMPT, append_reply

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url=os.environ.get("OPENAI_PROXY_URL"),
)

# 队列用于存储用户弹幕和 OpenAI 回复
conversation_history = [SYSTEM_PROMPT]


def generate_reply(user_name, user_message):
    # Append the user's message to the conversation history
    append_reply(conversation_history, user_name, user_message)

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


if __name__ == '__main__':
    # Example usage
    user_name = "User1"
    user_message = "你好呀，主播！"
    print(generate_reply(user_name, user_message))
