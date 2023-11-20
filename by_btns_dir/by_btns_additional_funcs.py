from turtle_settings import right_act, left_act, forward_act, up_act, down_act, circle_act, repeat_act, \
    num_error, com_error


def print_error(commands, ind, string, message, dind, type_error, bot, chat_id):
    if type_error == num_error:
        print(f'\n{message}')
        bot.send_message(chat_id, f'!!!ОШИБКА!!!\n{message}')

        commands[ind] = f'👉{commands[ind]}'
        commands[ind + dind] = f'{commands[ind + dind]}👈'

        print(f'Место ошибки: {" ".join(commands)}')
        msg = bot.send_message(chat_id, f'Место ошибки:\n{" ".join(commands)}')

    elif type_error == com_error:
        print(f'\n{message}')
        bot.send_message(chat_id, f'!!!ОШИБКА!!!\n{message}')

        print(f'!!!<<<{commands[ind]}>>>')
        commands[ind] = f'👉{commands[ind]}👈'
        msg = bot.send_message(chat_id, f'Место ошибки:\n{" ".join(commands)}')

    return msg


def check_command(commands, ind, begin_itters, end_itters, bot, chat_id):
    string = commands[ind].title()
    if '[' in string:
        if begin_itters:
            string = string[1:]
        else:
            message = 'Открывающаяся скобка "[" допустима только сразу после команды "Повтори n"'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=0, type_error=num_error,
                              bot=bot, chat_id=chat_id)
            return False, ind, False, msg

    if string in [right_act, left_act, forward_act]:
        if ind + 1 >= len(commands):
            message = f'Неверный формат числа или числового выражения после команды {string}'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=0, type_error=num_error,
                              bot=bot, chat_id=chat_id)
            return False, ind, False, msg
        try:
            num = commands[ind + 1]
            if num[-1] == ']':
                if not end_itters:
                    message = 'Закрывающаяся скобка "]" допустима только сразу после команды "Повтори n"'
                    msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=1,
                                      type_error=num_error, bot=bot, chat_id=chat_id)
                    return False, ind, False, msg
                num = num[:-1]
                num = eval(num)
                print(string, num)
                return True, ind + 2, False, None
            else:
                num = eval(num)
                print(string, num, end=' ')
                return True, ind + 2, True, None
        except:
            message = 'Неверный формат числа или числового выражения'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=1, type_error=num_error,
                              bot=bot, chat_id=chat_id)
            return False, ind, False, msg

    elif string in [up_act, down_act]:
        if ind + 1 >= len(commands):
            message = f'После команды "{string}" должно идти слово "хвост"'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=0, type_error=num_error,
                              bot=bot, chat_id=chat_id)
            return False, ind, False, msg

        if commands[ind + 1].lower() in ['хвост', 'хвост]']:
            if commands[ind + 1][-1] == ']':
                if not end_itters:
                    message = 'Закрывающаяся скобка "]" допустима только сразу после команды "Повтори n"'
                    msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=1,
                                      type_error=num_error, bot=bot, chat_id=chat_id)
                    return False, ind, False, msg
                print(string, commands[ind + 1][-1])
                return True, ind + 2, False, None
            else:
                print(string, commands[ind + 1], end=' ')
                return True, ind + 2, True, None
        else:
            message = f'После команды "{string}" должно идти слово "хвост"'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=1, type_error=num_error,
                              bot=bot, chat_id=chat_id)
            return False, ind, False, msg

    elif string == circle_act:
        if ind + 4 >= len(commands):
            message = 'Неверный формат чисел или числовых выражений или их количество (необходимо 4 для команды "Дуга")'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=len(commands) - ind - 1,
                              type_error=num_error, bot=bot, chat_id=chat_id)
            return False, ind, False, msg
        try:
            num1 = eval(commands[ind + 1])
            num2 = eval(commands[ind + 2])
            num3 = eval(commands[ind + 3])
            num4 = commands[ind + 4]
            if num4[-1] == ']':
                num4 = num4[:-1]
                num4 = eval(num4)
                if not end_itters:
                    message = 'Закрывающаяся скобка "]" допустима только сразу после команды "Повтори n"'
                    msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=4,
                                      type_error=num_error, bot=bot, chat_id=chat_id)
                    return False, ind, False, msg
                print(string, num1, num2, num3, num4)
                return True, ind + 5, False, None
            else:
                num4 = eval(num4)
                print(string, num1, num2, num3, num4, end=' ')
                return True, ind + 5, True, None
        except:
            message = 'Неверный формат чисел или числовых выражений или их количество (необходимо 4 для команды "Дуга")'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=4, type_error=num_error,
                              bot=bot, chat_id=chat_id)
            return False, ind, False, msg

    else:
        if string == repeat_act:
            message = '\nКоманда "Повтори n" не должна встречаться внутри другой команды "Повтори n"'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=1, type_error=num_error,
                              bot=bot, chat_id=chat_id)
        else:
            message = '\nНедопустимая команда'
            msg = print_error(commands=commands, ind=ind, string=string, message=message, dind=0, type_error=com_error,
                              bot=bot, chat_id=chat_id)
        return False, ind, False, msg


def is_valid_instruction_string(instruction_string, bot, chat_id):
    commands = []
    for i in instruction_string.split(','):
        L = i.split()
        for j in L:
            commands.append(j)

    i = 0
    while True:
        if i >= len(commands):
            return True, msg

        if commands[i].title() == repeat_act:
            print()
            print(commands[i], commands[i + 1])
            if commands[i + 1].isdigit():
                if commands[i + 2][0] == '[':
                    begin_ind = i
                    i += 2
                    begin_itters = True
                    while True:
                        end_itters = True
                        flag, i, end_itters, msg = check_command(commands, i, begin_itters, end_itters, bot, chat_id)
                        begin_itters = False
                        if not flag:
                            return False, msg
                        if i >= len(commands):
                            if end_itters:
                                message = '\nВ цикле "Повтори n" не была закрыта скобка "]"'
                                msg = print_error(commands=commands, ind=begin_ind,
                                                  string=' '.join(commands[begin_ind:]),
                                                  message=message, dind=len(commands) - begin_ind - 1,
                                                  type_error=num_error, bot=bot, chat_id=chat_id)
                                return False, msg
                            else:
                                return True, msg
                        if not end_itters:
                            break
                else:
                    message = '\nОтсутствует скобка "[" после команды Повтори n'
                    msg = print_error(commands=commands, ind=i, string=commands[i], message=message, dind=2,
                                      type_error=num_error, bot=bot, chat_id=chat_id)
                    return False, msg
            else:
                message = '\nНеверный формат числа после команды Повтори. Необходимо целое число'
                msg = print_error(commands=commands, ind=i, string=commands[i], message=message, dind=1,
                                  type_error=num_error, bot=bot, chat_id=chat_id)
                return False, msg
        else:
            begin_itters = False
            end_itters = False
            flag, i, end_itters, msg = check_command(commands, i, begin_itters, end_itters, bot, chat_id)
            if not flag:
                if commands[-1] in [right_act, left_act, forward_act, up_act, down_act, circle_act, repeat_act]:
                    message = '\nНеверный формат команды'
                    msg = print_error(commands=commands, ind=i, string=commands[i], message=message, dind=0,
                                      type_error=num_error, bot=bot, chat_id=chat_id)
                return False, msg