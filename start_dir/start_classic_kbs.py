from telebot.types import ReplyKeyboardMarkup
from start_dir.start_btns import by_btns_btn, by_hand_btn

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.row(by_hand_btn, by_btns_btn)