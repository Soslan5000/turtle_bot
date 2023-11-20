from telebot.types import ReplyKeyboardMarkup
from by_hand_dir.by_hand_btns import back_btn, north_btn, east_btn, west_btn, south_btn

kb_for_orientation = ReplyKeyboardMarkup(resize_keyboard=True)
kb_for_orientation.row(north_btn, south_btn)
kb_for_orientation.row(west_btn, east_btn)
kb_for_orientation.row(back_btn)

kb_for_back = ReplyKeyboardMarkup(resize_keyboard=True)
kb_for_back.row(back_btn)