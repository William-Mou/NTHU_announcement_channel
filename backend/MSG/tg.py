import telepot
from django.conf import settings
import logging

TOKEN = settings.TG_BOT_TOKEN
TG_CHAT_ID = settings.TG_CHAT_ID


def send_msg(office, title, link):
    bot = telepot.Bot(TOKEN)
    log_msg = f"{office}, title： {title}"
    try:
        bot.sendMessage(TG_CHAT_ID,  f"{office} 公告：\n{title}\n{link}")
        logging.info(f"office: {log_msg}")
    except:
        logging.warning(f"time out : {log_msg}")
