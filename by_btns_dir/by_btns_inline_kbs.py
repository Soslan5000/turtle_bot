from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from by_btns_dir.by_btns_btns import back_btn, north_btn, east_btn, west_btn, south_btn, \
    right_btn, up_btn, left_btn, back_to_menu_btn, down_btn, circle_btn, repeat_btn, forward_btn, return_to_back_btn, \
    back_row_btn, next_row_btn, the_end_btn, end_cicle_btn
from by_btns_dir.by_btns_clbs import back_clb, east_clb, west_clb, north_clb, south_clb, \
    circle_clb, up_clb, down_clb, left_clb, right_clb, repeat_clb, forward_clb, back_to_menu_clb, num_clb, \
    back_row_clb, next_row_clb, return_to_back_clb, next_row_for_R_clb, back_row_for_R_clb, num_R_clb, \
    next_row_for_a_clb, back_row_for_a_clb, num_a_clb, back_row_for_b_clb, next_row_for_b_clb, num_b_clb, \
    num_alf_clb, back_row_for_alf_clb, next_row_for_alf_clb, next_row_for_repeat_clb, num_repeat_clb, \
    back_row_for_repeat_clb, the_end_clb, end_cicle_clb

kb_for_orientation = InlineKeyboardMarkup(row_width=1)
kb_for_orientation.row(
    InlineKeyboardButton(text=north_btn, callback_data=north_clb),
    InlineKeyboardButton(text=south_btn, callback_data=south_clb),
                       )
kb_for_orientation.row(
    InlineKeyboardButton(text=west_btn, callback_data=west_clb),
    InlineKeyboardButton(text=east_btn, callback_data=east_clb),
                       )
kb_for_orientation.row(
    InlineKeyboardButton(text=back_btn, callback_data=back_clb)
                       )

def create_choice_command_kb(user):
    kb_for_choice_command = InlineKeyboardMarkup(row_width=1)
    kb_for_choice_command.row(
        InlineKeyboardButton(text=right_btn, callback_data=right_clb),
        InlineKeyboardButton(text=left_btn, callback_data=left_clb),
                           )
    kb_for_choice_command.row(
        InlineKeyboardButton(text=forward_btn, callback_data=forward_clb),
        InlineKeyboardButton(text=circle_btn, callback_data=circle_clb),
                           )
    kb_for_choice_command.row(
        InlineKeyboardButton(text=up_btn, callback_data=up_clb),
        InlineKeyboardButton(text=down_btn, callback_data=down_clb),
                           )
    if user.in_cicle:
        if user.commands_list[-1] != '[':
            kb_for_choice_command.row(
                InlineKeyboardButton(text=end_cicle_btn, callback_data=end_cicle_btn),
            )
    else:
        if len(user.commands_list) == 0:
            kb_for_choice_command.row(
                InlineKeyboardButton(text=repeat_btn, callback_data=repeat_clb),
            )
        else:
            if user.commands_list[-1] != '[':
                kb_for_choice_command.row(
                    InlineKeyboardButton(text=repeat_btn, callback_data=repeat_clb),
                )

    if len(user.commands_list) > 0:
        kb_for_choice_command.row(
            InlineKeyboardButton(text=return_to_back_btn, callback_data=return_to_back_clb),
                              )
        if not user.in_cicle:
            kb_for_choice_command.row(
                InlineKeyboardButton(text=the_end_btn, callback_data=the_end_clb),
            )
    kb_for_choice_command.row(
        InlineKeyboardButton(text=back_to_menu_btn, callback_data=back_to_menu_clb),
                          )
    return kb_for_choice_command

def create_nums_list(ind):
    nums_kb = InlineKeyboardMarkup(row_width=1)
    k = 50
    if ind >= 0:
        begin_ind = k*ind
        end_ind = begin_ind + k
        d_ind = 5
        d_i = 1
    else:
        begin_ind = k * (ind + 1)
        end_ind = begin_ind - k
        d_ind = -5
        d_i = -1
    for i in range(begin_ind, end_ind, d_ind):
        btns = [InlineKeyboardButton(text=str(j), callback_data=str(j) + '_' + num_clb) for j in range(i, i + d_ind, d_i)]
        nums_kb.row(*btns)
    nums_kb.row(
        InlineKeyboardButton(text=back_row_clb, callback_data=back_row_clb),
        InlineKeyboardButton(text=next_row_clb, callback_data=next_row_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=return_to_back_btn, callback_data=return_to_back_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=back_to_menu_btn, callback_data=back_to_menu_clb)
    )
    return nums_kb


def create_nums_for_R_list(ind):
    nums_kb = InlineKeyboardMarkup(row_width=1)
    k = 50
    if ind >= 0:
        begin_ind = k*ind
        end_ind = begin_ind + k
        d_ind = 5
        d_i = 1
    else:
        begin_ind = k * (ind + 1)
        end_ind = begin_ind - k
        d_ind = -5
        d_i = -1
    for i in range(begin_ind, end_ind, d_ind):
        btns = [InlineKeyboardButton(text=str(j), callback_data=str(j) + '_' + num_R_clb) for j in range(i, i + d_ind, d_i)]
        nums_kb.row(*btns)
    nums_kb.row(
        InlineKeyboardButton(text=back_row_btn, callback_data=back_row_for_R_clb),
        InlineKeyboardButton(text=next_row_btn, callback_data=next_row_for_R_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=return_to_back_btn, callback_data=return_to_back_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=back_to_menu_btn, callback_data=back_to_menu_clb)
    )
    return nums_kb


def create_nums_for_a_list(ind):
    nums_kb = InlineKeyboardMarkup(row_width=1)
    k = 50
    if ind >= 0:
        begin_ind = k*ind
        end_ind = begin_ind + k
        d_ind = 5
        d_i = 1
    else:
        begin_ind = k * (ind + 1)
        end_ind = begin_ind - k
        d_ind = -5
        d_i = -1
    for i in range(begin_ind, end_ind, d_ind):
        btns = [InlineKeyboardButton(text=str(j), callback_data=str(j) + '_' + num_a_clb) for j in range(i, i + d_ind, d_i)]
        nums_kb.row(*btns)
    nums_kb.row(
        InlineKeyboardButton(text=back_row_btn, callback_data=back_row_for_a_clb),
        InlineKeyboardButton(text=next_row_btn, callback_data=next_row_for_a_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=return_to_back_btn, callback_data=return_to_back_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=back_to_menu_btn, callback_data=back_to_menu_clb)
    )
    return nums_kb


def create_nums_for_b_list(ind):
    nums_kb = InlineKeyboardMarkup(row_width=1)
    k = 50
    if ind >= 0:
        begin_ind = k*ind
        end_ind = begin_ind + k
        d_ind = 5
        d_i = 1
    else:
        begin_ind = k * (ind + 1)
        end_ind = begin_ind - k
        d_ind = -5
        d_i = -1
    for i in range(begin_ind, end_ind, d_ind):
        btns = [InlineKeyboardButton(text=str(j), callback_data=str(j) + '_' + num_b_clb) for j in range(i, i + d_ind, d_i)]
        nums_kb.row(*btns)
    nums_kb.row(
        InlineKeyboardButton(text=back_row_btn, callback_data=back_row_for_b_clb),
        InlineKeyboardButton(text=next_row_btn, callback_data=next_row_for_b_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=return_to_back_btn, callback_data=return_to_back_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=back_to_menu_btn, callback_data=back_to_menu_clb)
    )
    return nums_kb


def create_nums_for_alf_list(ind):
    nums_kb = InlineKeyboardMarkup(row_width=1)
    k = 50
    if ind >= 0:
        begin_ind = k*ind
        end_ind = begin_ind + k
        d_ind = 5
        d_i = 1
    else:
        begin_ind = k * (ind + 1)
        end_ind = begin_ind - k
        d_ind = -5
        d_i = -1
    for i in range(begin_ind, end_ind, d_ind):
        btns = [InlineKeyboardButton(text=str(j), callback_data=str(j) + '_' + num_alf_clb) for j in range(i, i + d_ind, d_i)]
        nums_kb.row(*btns)
    nums_kb.row(
        InlineKeyboardButton(text=back_row_btn, callback_data=back_row_for_alf_clb),
        InlineKeyboardButton(text=next_row_btn, callback_data=next_row_for_alf_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=return_to_back_btn, callback_data=return_to_back_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=back_to_menu_btn, callback_data=back_to_menu_clb)
    )
    return nums_kb


def create_nums_for_repeat(ind):
    nums_kb = InlineKeyboardMarkup(row_width=1)
    k = 50
    if ind >= 0:
        begin_ind = k*ind
        end_ind = begin_ind + k
        d_ind = 5
        d_i = 1
    else:
        begin_ind = k * (ind + 1)
        end_ind = begin_ind - k
        d_ind = -5
        d_i = -1
    for i in range(begin_ind, end_ind, d_ind):
        btns = [InlineKeyboardButton(text=str(j), callback_data=str(j) + '_' + num_repeat_clb) for j in range(i, i + d_ind, d_i)]
        nums_kb.row(*btns)
    nums_kb.row(
        InlineKeyboardButton(text=back_row_btn, callback_data=back_row_for_repeat_clb),
        InlineKeyboardButton(text=next_row_btn, callback_data=next_row_for_repeat_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=return_to_back_btn, callback_data=return_to_back_clb)
    )
    nums_kb.row(
        InlineKeyboardButton(text=back_to_menu_btn, callback_data=back_to_menu_clb)
    )
    return nums_kb