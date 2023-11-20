from start_dir.start_messages import start_msg
from start_dir.start_classic_kbs import start_kb


def start_func(bot, message):
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id,
                     text=start_msg,
                     reply_markup=start_kb,
                     parse_mode="Markdown")
