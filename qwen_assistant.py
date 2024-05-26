import os
import requests
from dotenv import load_dotenv

from assistant_helper import SYSTEM_PROMPT, append_reply

load_dotenv()

# 设置 DashScope API 密钥
api_key = os.getenv("DASHSCOPE_API_KEY")
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# 队列用于存储用户弹幕和 DashScope 回复
conversation_history = [SYSTEM_PROMPT]


def generate_reply(user_name, user_message):
    append_reply(conversation_history, user_name, user_message)

    # Prepare the request body for DashScope API
    body = {
        'model': 'qwen-turbo',
        "input": {
            "messages": conversation_history
        },
        "parameters": {
            "result_format": "message"
        }
    }

    # Generate the reply from DashScope
    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()

    # Extract the reply message
    ai_reply = response_data["output"]["choices"][0]["message"]["content"]

    # Append AI's reply to the conversation
    conversation_history.append({"role": "assistant", "content": ai_reply})

    return ai_reply


if __name__ == '__main__':
    # Example usage
    user_name = "User1"
    user_message = "你好呀，主播！"
    print(generate_reply(user_name, user_message))
