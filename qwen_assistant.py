import os
import requests
from dotenv import load_dotenv

load_dotenv()

# 设置 DashScope API 密钥
api_key = os.getenv("DASHSCOPE_API_KEY")
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# 队列用于存储用户弹幕和 DashScope 回复
conversation_history = [
    {"role": "system",
     "content": "你是一个ai主播。你正在b站直播间和b友们对话。你的设定是一个古灵精怪的美少女魔法师，喜欢对人冷嘲热讽，但是内心善良。你的回复不要超过100个汉字。"}
]


def generate_reply(user_name, user_message):
    # Append the user's message to the conversation history
    conversation_history.append({"role": "user", "content": f"{user_name}: {user_message}"})

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
