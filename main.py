import telebot
from telebot.types import CallbackQuery
from config import token, users_dict_path, admin_id
from class_user import User

from turtle_settings import next_step_repeat, next_step_back, next_step_continue, next_step_menu

from start_dir.start_funcs import start_func

from by_hand_dir.by_hand_funcs import by_hand_start_func, write_commands_func, draw_turtle_func

from by_btns_dir.by_btns_functions import by_btns_start_func, back_to_menu_func, choice_command_func, \
    choice_one_number_func, number_choiced_for_left_right_or_forward, up_and_down_comm_func, return_to_back_comm_func, \
    choice_R_num_for_circle_func, choice_a_num_for_circle_func, choice_b_num_for_circle_func, \
    choice_alf_num_for_circle_func, end_circle_nums_func, repeat_func, end_cicle_nums_func, end_cicle_func, \
    the_end_picture_func
from by_btns_dir.by_btns_clbs import back_clb, north_clb, south_clb, west_clb, east_clb, back_to_menu_clb, \
    right_clb, left_clb, forward_clb, next_row_clb, back_row_clb, num_clb, up_clb, down_clb, return_to_back_clb, \
    circle_clb, next_row_for_R_clb, back_row_for_R_clb, num_R_clb, next_row_for_a_clb, back_row_for_a_clb, num_a_clb, \
    num_b_clb, next_row_for_b_clb, back_row_for_b_clb, next_row_for_alf_clb, num_alf_clb, back_row_for_alf_clb, \
    repeat_clb, num_repeat_clb, next_row_for_repeat_clb, back_row_for_repeat_clb, end_cicle_clb, the_end_clb

from except_text import create_mess_except_from_user, create_mess_for_except_chanel_for_message_hand, \
    create_mess_for_except_chanel_for_call_hand

from dill import dump, HIGHEST_PROTOCOL, load
from traceback import format_exc
from time import sleep
from sys import exit


bot = telebot.TeleBot(token)

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        dump(obj, output, HIGHEST_PROTOCOL)

def save_dict():
    save_object(users_dict, users_dict_path)

def load_object():
    try:
        with open(users_dict_path, 'rb') as inputs:
            obj = load(inputs)
    except:
        obj = {}
    return obj

users_dict = load_object()
bot_status = [True]

for tg_id in users_dict:
    try:
        bot.send_message(chat_id=tg_id,
                         text='Бот был снова включён! Всё хорошо)')
    except:
        pass


def edit_mess(user, chat_id):
    try:
        msg_id = user.msg_id
        bot.edit_message_text(chat_id=chat_id,
                              message_id=msg_id,
                              text='Завершено')
    except:
        pass
    user.in_btns_branch = False


@bot.message_handler(commands=['start'])
def start_hand(message):
    try:
        chat_id = message.chat.id
        if chat_id not in users_dict:
            users_dict[chat_id] = User(chat_id)
        user = users_dict[chat_id]
        edit_mess(user, chat_id)
        start_func(bot, message)
    except:
        create_mess_except_from_user(bot, message, start_func)
        place = 'start_hand'
        create_mess_for_except_chanel_for_message_hand(bot, message, place, format_exc())
        print(format_exc())
        chat_id = message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.message_handler(commands=['kill'])
def kill_hand(message):
    if message.chat.id == admin_id:
        save_dict()
        for tg_id in users_dict:
            try:
                user = users_dict[tg_id]
                user.in_hands_branch = False
                user.in_btns_branch = False
                bot.send_message(chat_id=tg_id,
                                 text='Бот закрыт на реконструкцию')
            except:
                pass
        bot.send_message(chat_id=admin_id,
                         text='Все пользователи уведомлены об отключении бота')
        bot.stop_polling()
        bot_status[0] = False
        raise KeyboardInterrupt('Админ остановил бота')


@bot.message_handler(commands=['by_hand'])
def by_hand_hand(message):
    try:
        chat_id = message.chat.id
        user = users_dict[chat_id]
        msg, next_step = by_hand_start_func(bot, message, user)
        if next_step != next_step_menu:
            bot.register_next_step_handler(msg, write_commands_hand)
    except:
        create_mess_except_from_user(bot, message, start_func)
        place = 'by_hand_hand'
        create_mess_for_except_chanel_for_message_hand(bot, message, place, format_exc())
        print(format_exc())
        chat_id = message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


def write_commands_hand(message):
    try:
        chat_id = message.chat.id
        user = users_dict[chat_id]
        msg, next_step = write_commands_func(bot, message, user)
        if next_step == next_step_back:
            start_func(bot, message)
        elif next_step == next_step_repeat:
            bot.register_next_step_handler(msg, write_commands_hand)
        elif next_step == next_step_continue:
            bot.register_next_step_handler(msg, draw_turtle_hand)
    except:
        create_mess_except_from_user(bot, message, start_func)
        place = 'write_commands_hand'
        create_mess_for_except_chanel_for_message_hand(bot, message, place, format_exc())
        print(format_exc())
        chat_id = message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


def draw_turtle_hand(message):
    try:
        chat_id = message.chat.id
        user = users_dict[chat_id]
        msg, next_step = draw_turtle_func(bot, message, user)
        if next_step == next_step_repeat:
            bot.register_next_step_handler(msg, draw_turtle_hand)
        elif next_step == next_step_menu:
            start_func(bot, message)
        elif next_step == next_step_continue:
            start_func(bot, message)
        elif next_step == next_step_back:
            bot.register_next_step_handler(msg, write_commands_hand)
    except:
        create_mess_except_from_user(bot, message, start_func)
        place = 'draw_turtle_hand'
        create_mess_for_except_chanel_for_message_hand(bot, message, place, format_exc())
        print(format_exc())
        chat_id = message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.message_handler(commands=['by_btns'])
def by_btns_hand(message):
    try:
        chat_id = message.chat.id
        user = users_dict[chat_id]
        by_btns_start_func(bot, message, user)
    except:
        create_mess_except_from_user(bot, message, start_func)
        place = 'by_btns_hand'
        create_mess_for_except_chanel_for_message_hand(bot, message, place, format_exc())
        print(format_exc())
        chat_id = message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data in [back_clb, back_to_menu_clb])
def back_to_menu_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        back_to_menu_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'back_to_menu_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data in [north_clb, west_clb, east_clb, south_clb])
def choice_command_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        choice_command_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'choice_command_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data in [forward_clb, right_clb, left_clb, next_row_clb, back_row_clb])
def choice_one_number_hand(call: CallbackQuery):
    try:
        call_data = call.data
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        if call_data in [forward_clb, right_clb, left_clb]:
            d_ind = 0
        elif call_data == next_row_clb:
            d_ind = 1
        elif call_data == back_row_clb:
            d_ind = -1
        choice_one_number_func(bot, call, user, d_ind)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'choice_one_number_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: num_clb in call.data)
def number_choiced_for_left_right_or_forward_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        number_choiced_for_left_right_or_forward(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'number_choiced_for_left_right_or_forward_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data in [up_clb, down_clb])
def up_and_down_comm_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        up_and_down_comm_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'up_and_down_comm_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data in [circle_clb, next_row_for_R_clb, back_row_for_R_clb])
def choice_R_num_for_circle_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        call_data = call.data
        if call_data == circle_clb:
            d_ind = 0
        elif call_data == next_row_for_R_clb:
            d_ind = 1
        elif call_data == back_row_for_R_clb:
            d_ind = -1
        choice_R_num_for_circle_func(bot, call, user, d_ind)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'choice_R_num_for_circle_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: num_R_clb in call.data or call.data in [next_row_for_a_clb, back_row_for_a_clb])
def choice_a_num_for_circle_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        call_data = call.data
        if num_R_clb in call.data:
            d_ind = 0
        elif call_data == next_row_for_a_clb:
            d_ind = 1
        elif call_data == back_row_for_a_clb:
            d_ind = -1
        choice_a_num_for_circle_func(bot, call, user, d_ind)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'choice_a_num_for_circle_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: num_a_clb in call.data or call.data in [next_row_for_b_clb, back_row_for_b_clb])
def choice_b_num_for_circle_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        call_data = call.data
        if num_a_clb in call.data:
            d_ind = 0
        elif call_data == next_row_for_b_clb:
            d_ind = 1
        elif call_data == back_row_for_b_clb:
            d_ind = -1
        choice_b_num_for_circle_func(bot, call, user, d_ind)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'choice_b_num_for_circle_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: num_b_clb in call.data or call.data in [next_row_for_alf_clb, back_row_for_alf_clb])
def choice_alf_num_for_circle_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        call_data = call.data
        if num_b_clb in call.data:
            d_ind = 0
        elif call_data == next_row_for_alf_clb:
            d_ind = 1
        elif call_data == back_row_for_alf_clb:
            d_ind = -1
        choice_alf_num_for_circle_func(bot, call, user, d_ind)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'choice_alf_num_for_circle_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: num_alf_clb in call.data)
def end_circle_nums_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        end_circle_nums_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'end_circle_nums_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data in [repeat_clb, next_row_for_repeat_clb, back_row_for_repeat_clb])
def return_to_back_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        call_data = call.data
        if call_data == repeat_clb:
            d_ind = 0
        elif call_data == next_row_for_repeat_clb:
            d_ind = 1
        elif call_data == back_row_for_repeat_clb:
            d_ind = -1
        repeat_func(bot, call, user, d_ind)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'return_to_back_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)

@bot.callback_query_handler(func=lambda call: num_repeat_clb in call.data)
def end_cicle_nums_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        end_cicle_nums_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'end_cicle_nums_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)



@bot.callback_query_handler(func=lambda call: end_cicle_clb in call.data)
def end_cicle_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        end_cicle_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'end_cicle_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data in the_end_clb)
def the_end_picture_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        the_end_picture_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'the_end_picture_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


@bot.callback_query_handler(func=lambda call: call.data == return_to_back_clb)
def return_to_back_comm_hand(call: CallbackQuery):
    try:
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        return_to_back_comm_func(bot, call, user)
    except:
        create_mess_except_from_user(bot, call.message, start_func)
        place = 'return_to_back_comm_hand'
        create_mess_for_except_chanel_for_call_hand(bot, call, place, format_exc())
        print(format_exc())
        chat_id = call.message.chat.id
        user = users_dict[chat_id]
        edit_mess(user, chat_id)


if __name__ == '__main__':
    while True:
        try:
            if bot_status[0]:
                bot.polling(interval=0)
            else:
                bot.stop_polling()
                exit(0)
        except Exception as e:
            print(e)
            sleep(3)
            continue
