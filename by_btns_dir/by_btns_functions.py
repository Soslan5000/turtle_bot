from telebot.types import InputMediaPhoto
import os
from by_btns_dir.by_btns_messages import by_btns_start_msg, start_msg, back_to_menu_msg, choice_comm_msg, \
    choice_num_msg, load_msg, except_msg
from by_btns_dir.by_btns_inline_kbs import kb_for_orientation, create_choice_command_kb, create_nums_list, \
    create_nums_for_R_list, create_nums_for_a_list, create_nums_for_b_list, create_nums_for_alf_list, \
    create_nums_for_repeat
from by_btns_dir.by_btns_classic_kbs import start_kb
from by_btns_dir.by_btns_clbs import right_clb, left_clb, forward_clb, circle_clb, up_clb, down_clb, repeat_clb
from by_btns_dir.by_btns_additional_funcs import is_valid_instruction_string
from turtle_funcs import do_turtle_picture_screen
from turtle_settings import png_dir, svg_dir


def by_btns_start_func(bot, message, user):
    chat_id = message.chat.id
    if user.in_hands_branch or user.in_btns_branch:
        msg = bot.send_message(chat_id=chat_id,
                               text=except_msg,
                               parse_mode="Markdown")
    else:
        msg = bot.send_message(chat_id=chat_id,
                               text=by_btns_start_msg,
                               reply_markup=kb_for_orientation,
                               parse_mode="Markdown")
        user.msg_id = message.message_id + 1
        user.in_btns_branch = True
    return msg


def back_to_menu_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    user.commands_list.clear()
    user.commands_list_index = -1
    user.num_index = 0
    user.in_cicle = False
    user.in_btns_branch = False
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=back_to_menu_msg)
    bot.send_message(chat_id=chat_id,
                     text=start_msg,
                     reply_markup=start_kb,
                     parse_mode="Markdown")


def choice_command_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    orient = call.data
    user.orientation = orient
    kb = create_choice_command_kb(user)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_comm_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def choice_one_number_func(bot, call, user, plus_ind):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data

    if plus_ind == 0:
        user.num_index = 0
        user.commands_list.append(text + ' ')
        user.commands_list_index += 1
    else:
        user.num_index += plus_ind

    ind = user.num_index
    kb = create_nums_list(ind)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_num_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def number_choiced_for_left_right_or_forward(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data.split('_')[0]
    user.commands_list.append(text + ' ')
    user.commands_list_index += 1
    kb = create_choice_command_kb(user)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_comm_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def up_and_down_comm_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data
    user.commands_list.append(text + ' ')
    user.commands_list_index += 1
    kb = create_choice_command_kb(user)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_comm_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def choice_R_num_for_circle_func(bot, call, user, plus_ind):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data

    if plus_ind == 0:
        user.num_index = 0
        user.commands_list.append(text + ' ')
        user.commands_list_index += 1
    else:
        user.num_index += plus_ind

    ind = user.num_index
    kb = create_nums_for_R_list(ind)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_num_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def choice_a_num_for_circle_func(bot, call, user, plus_ind):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data.split('_')[0]

    if plus_ind == 0:
        user.num_index = 0
        user.commands_list.append(text + ', ')
        user.commands_list_index += 1
    else:
        user.num_index += plus_ind

    ind = user.num_index
    kb = create_nums_for_a_list(ind)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_num_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def choice_b_num_for_circle_func(bot, call, user, plus_ind):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data.split('_')[0]

    if plus_ind == 0:
        user.num_index = 0
        user.commands_list.append(text + ', ')
        user.commands_list_index += 1
    else:
        user.num_index += plus_ind

    ind = user.num_index
    kb = create_nums_for_b_list(ind)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_num_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def choice_alf_num_for_circle_func(bot, call, user, plus_ind):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data.split('_')[0]

    if plus_ind == 0:
        user.num_index = 0
        user.commands_list.append(text + ', ')
        user.commands_list_index += 1
    else:
        user.num_index += plus_ind

    ind = user.num_index
    kb = create_nums_for_alf_list(ind)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_num_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def end_circle_nums_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data.split('_')[0]
    user.commands_list.append(text + ' ')
    user.commands_list_index += 1
    kb = create_choice_command_kb(user)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_comm_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def repeat_func(bot, call, user, plus_ind):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data

    if plus_ind == 0:
        user.num_index = 0
        user.commands_list.append(text + ' ')
        user.commands_list_index += 1
    else:
        user.num_index += plus_ind

    user.commands_list_index += 1
    ind = user.num_index
    kb = create_nums_for_repeat(ind)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_comm_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def end_cicle_nums_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = call.data.split('_')[0]
    user.commands_list.append(text + ' ')
    user.commands_list.append('[')
    user.commands_list_index += 1
    user.in_cicle = True
    kb = create_choice_command_kb(user)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_comm_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def end_cicle_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    user.commands_list[-1] = user.commands_list[-1][:-1]
    user.commands_list.append('] ')
    user.commands_list_index += 1
    user.in_cicle = False
    kb = create_choice_command_kb(user)
    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{choice_comm_msg}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")


def the_end_picture_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    text = user.build_instruction_string()
    instruction_string = text
    valid, msg = is_valid_instruction_string(instruction_string, bot, chat_id)
    user.commands_list.clear()
    user.commands_list_index = -1
    user.num_index = 0
    user.in_cicle = False
    if valid:
        bot.edit_message_text(chat_id=chat_id,
                              message_id=msg_id,
                              text=load_msg)
        svg_path = str(chat_id) + '.svg'
        png_path = str(chat_id) + '.png'
        orient = user.orientation
        do_turtle_picture_screen(text, svg_path, orient)
        bot.send_media_group(chat_id=chat_id,
                             media=[InputMediaPhoto(open(png_dir + png_path, 'rb'))])
        os.remove(svg_dir + svg_path)
        os.remove(png_dir + png_path)
        bot.send_message(chat_id=chat_id,
                         text="`" + instruction_string + "`",
                         parse_mode="Markdown")
        bot.send_message(chat_id=chat_id,
                         text=start_msg,
                         reply_markup=start_kb,
                         parse_mode="Markdown")
    else:
        bot.edit_message_text(chat_id=chat_id,
                              message_id=msg_id,
                              text='Ошибка!')
        bot.send_message(chat_id=chat_id,
                         text="`" + instruction_string + "`",
                         parse_mode="Markdown")
        bot.send_message(chat_id=chat_id,
                         text=start_msg,
                         reply_markup=start_kb,
                         parse_mode="Markdown")
    user.in_btns_branch = False


def return_to_back_comm_func(bot, call, user):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    command_list = user.commands_list
    user.num_index = 0
    ind = user.num_index
    user.commands_list_index -= 1
    del_com = command_list.pop()

    if del_com.replace(' ', '').isdigit():
        print('digit')
        if command_list[-1].replace(' ', '') in [right_clb, left_clb, forward_clb, repeat_clb]:
            kb = create_nums_list(ind)
        elif command_list[-1].replace(' ', '') == circle_clb:
            kb = create_nums_for_R_list(ind)
        elif command_list[-2].replace(' ', '') == circle_clb:
            kb = create_nums_for_a_list(ind)
        elif command_list[-3].replace(' ', '') == circle_clb:
            kb = create_nums_for_b_list(ind)
        elif command_list[-4].replace(' ', '') == circle_clb:
            kb = create_nums_for_alf_list(ind)
        text = choice_num_msg
    elif del_com.replace(' ', '') == ']':
        print(']')
        user.in_cicle = True
        kb = create_choice_command_kb(user)
        text = choice_comm_msg
    elif del_com.replace(' ', '') == '[':
        print('[')
        command_list.pop()
        user.in_cicle = False
        kb = create_nums_for_repeat(user)
        text = choice_num_msg
    elif del_com.replace(' ', '') in [up_clb, down_clb]:
        print('up_clb, down_clb')
        kb = create_choice_command_kb(user)
        text = choice_comm_msg

    elif del_com.replace(' ', '') in [right_clb, left_clb, forward_clb, repeat_clb, circle_clb]:
        print('right_clb, left_clb, forward_clb, repeat_clb, circle_clb')
        if command_list[-1].replace(' ', '') in [up_clb, down_clb, '[', ']']:
            kb = create_choice_command_kb(user)
            text = choice_comm_msg
        elif command_list[-2].replace(' ', '') in [right_clb, left_clb, forward_clb, repeat_clb]:
            kb = create_nums_list(ind)
            text = choice_num_msg
        elif command_list[-2].replace(' ', '') == circle_clb:
            kb = create_nums_for_R_list(ind)
            text = choice_num_msg
        elif command_list[-3].replace(' ', '') == circle_clb:
            kb = create_nums_for_a_list(ind)
            text = choice_num_msg
        elif command_list[-4].replace(' ', '') == circle_clb:
            kb = create_nums_for_b_list(ind)
            text = choice_num_msg
        elif command_list[-5].replace(' ', '') == circle_clb:
            kb = create_nums_for_alf_list(ind)
            text = choice_num_msg


    instruction_string = user.build_instruction_string()
    bot.edit_message_text(chat_id=chat_id,
                          message_id=msg_id,
                          text=f'{text}\n{"`" + instruction_string + "`" if len(instruction_string) > 0 else ""}',
                          reply_markup=kb,
                          parse_mode="Markdown")
