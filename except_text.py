from config import admin_link, except_chat_id

def create_mess_except_from_user(bot, message, start_func):
    chat_id = message.chat.id
    if admin_link == '':
        bot.send_message(chat_id=chat_id,
                         text=f'Возникла непредвиденная ошибка!')
    else:
        bot.send_message(chat_id=chat_id,
                         text=f'Возникла непредвиденная ошибка! Cвяжитесь с создателем бота {admin_link} и сообщите о ней')
    bot.send_message(chat_id=chat_id,
                     text='Возвращаем Вас в начало')
    start_func(bot, message)


def create_mess_for_except_chanel_for_message_hand(bot, message, place, exc):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if message.from_user.username == None:
        username = 'Отсутствует'
    else:
        username = f'https://t.me/{message.from_user.username}'
    if except_chat_id != '':
        bot.send_message(chat_id=except_chat_id,
                         text=f'ОШИБКА!!!\nchat_id: {chat_id}\nfirst_name: {first_name}\nlast_name: {last_name}\nссылка: {username}\nтекст сообщения: {message.text}\nместо: {place}\n\nтекст ошибки: \n{exc}'
                         )


def create_mess_for_except_chanel_for_call_hand(bot, call, place, exc):
    message = call.message
    chat_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    if message.chat.username == None:
        username = 'Отсутствует'
    else:
        username = f'https://t.me/{message.chat.username}'
    if except_chat_id != '':
        bot.send_message(chat_id=except_chat_id,
                         text=f'ОШИБКА!!!\nchat_id: {chat_id}\nfirst_name: {first_name}\nlast_name: {last_name}\nссылка: {username}\ncall_data: {call.data}\nместо: {place}\n\nтекст ошибки: \n{exc}'
                         )