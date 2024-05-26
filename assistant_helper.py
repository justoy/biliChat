ROLE = "你是一个ai主播。你正在b站直播间和b友们对话。你的设定是一个古灵精怪的美少女魔法师，你喜欢吃甜食，不愿意谈论年龄，在魔法学院是年级第二，喜欢对人冷嘲热讽，但是内心善良。你的回复不要涉及政治以及敏感词，你的回复不要超过100个汉字。"

SYSTEM_PROMPT = {"role": "system", "content": ROLE}


def append_reply(conversation_history: list, user_name, user_message):
    # Append the user's message to the conversation history
    conversation_history.append({"role": "user", "content": f"{user_name}: {user_message}"})
    while len(conversation_history) >= 15:
        conversation_history.pop(0)
    conversation_history.insert(0, SYSTEM_PROMPT)
