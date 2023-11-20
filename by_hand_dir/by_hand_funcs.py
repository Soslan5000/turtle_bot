from by_hand_dir.by_hand_messages import write_commands_msg, by_hand_start_msg, write_commands_repeat_msg, load_msg, \
    except_msg
from by_hand_dir.by_hand_classic_kb import kb_for_back, kb_for_orientation
from by_hand_dir.by_hand_btns import back_btn, east_btn, west_btn, south_btn, north_btn
from turtle_settings import next_step_back, next_step_repeat, next_step_continue, png_dir, svg_dir, next_step_menu
from by_hand_dir.additional_funcs import is_valid_instruction_string
from turtle_funcs import do_turtle_picture_screen
from telebot.types import InputMediaPhoto
import os


def by_hand_start_func(bot, message, user):
    chat_id = message.chat.id
    if user.in_hands_branch or user.in_btns_branch:
        msg = bot.send_message(chat_id=chat_id,
                               text=except_msg,
                               parse_mode="Markdown")
        next_step = next_step_menu
    else:
        msg = bot.send_message(chat_id=chat_id,
                               text=by_hand_start_msg,
                               reply_markup=kb_for_orientation,
                               parse_mode="Markdown")
        user.in_hands_branch = True
        next_step = None
    return msg, next_step


def write_commands_func(bot, message, user):
    chat_id = message.chat.id
    text = message.text
    if text in [back_btn, '/start']:
        msg = None
        next_step = next_step_back
        user.in_hands_branch = False
    elif text in [north_btn, south_btn, west_btn, east_btn]:
        user.orientation = text
        msg = bot.send_message(chat_id=chat_id,
                               text=write_commands_msg,
                               reply_markup=kb_for_back,
                               parse_mode="Markdown")
        next_step = next_step_continue
    else:
        bot.send_message(chat_id=chat_id,
                         text=write_commands_repeat_msg,
                         reply_markup=kb_for_back,
                         parse_mode="Markdown")
        msg = bot.send_message(chat_id=chat_id,
                               text=by_hand_start_msg,
                               reply_markup=kb_for_orientation,
                               parse_mode="Markdown")
        next_step = next_step_repeat
    return msg, next_step


def draw_turtle_func(bot, message, user):
    chat_id = message.chat.id
    text = message.text
    instruction_string = message.text
    if text == back_btn:
        msg = bot.send_message(chat_id=chat_id,
                               text=by_hand_start_msg,
                               reply_markup=kb_for_orientation,
                               parse_mode="Markdown")
        next_step = next_step_back
    elif text == '/start':
        msg = None
        next_step = next_step_menu
        user.in_hands_branch = False
    else:
        valid, msg = is_valid_instruction_string(instruction_string, bot, chat_id)
        if valid:
            msg = bot.send_message(chat_id=chat_id, text=load_msg)
            svg_path = str(chat_id) + '.svg'
            png_path = str(chat_id) + '.png'
            orient = user.orientation
            do_turtle_picture_screen(text, svg_path, orient)
            bot.send_media_group(chat_id=chat_id,
                                 media=[InputMediaPhoto(open(png_dir + png_path, 'rb'))])
            os.remove(svg_dir + svg_path)
            os.remove(png_dir + png_path)
            next_step = next_step_continue
            user.in_hands_branch = False
        else:
            next_step = next_step_repeat
    return msg, next_step
