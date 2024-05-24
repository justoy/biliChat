from streamutil import stream_video

test_text = """
b友：好看
AI：哈哈哈，你是说我好看吗？你知道什么叫“真理存在于美丽中”吗？哦，当然你不知道，因为这句话我刚刚编的～不过，既然你这么有眼光，我就大方承认啦，谢谢你的夸奖，嘻嘻~
"""

# stream_video('chat_log.txt', './Noto_Sans_TC/NotoSansTC-VariableFont_wght.ttf', 'rtmp://localhost/live/streamkey')
stream_video(test_text, '../NotoSansMonoCJKtc-Regular.otf', 'rtmp://localhost/live/streamkey')

