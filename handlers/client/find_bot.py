import asyncio
from datetime import datetime, timedelta

from aiogram import Dispatcher, types

from pyrogram.errors import FloodWait

from create_bot import bot, app
from data_base import sql_find_bot


async def get_chat_members(chat_id):
    """ Получение списка пользователей часа """
    try:
        response = app.get_chat_members(chat_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        response = 'Жди'
    return response


async def add_user(first_name, user_id, chat_id):
    """ Добавление пользователя в список для участия """
    dct = {}
    dct['chat_id'] = chat_id
    dct['first_name'] = first_name
    dct['user_id'] = user_id
    dct['num'] = 0

    await sql_find_bot.sql_add_participant(dct)


async def checking_for_bot(users, chat_id):
    """ Проверка на ботов """
    async for user in users:
        if 'bot' not in user.user.first_name:
            await add_user(user.user.first_name, user.user.id, chat_id)


async def response_choose_user(response):
    """ Возвращает ответ команды 'choose_bot' """
    if response is not None:
        return f'{response} - реально жидкий бот'
    else:
        return 'Список участников пуст'


async def command_implementation(usage_time, chat_id, date_now):
    """ Выполнение основных действий команды 'choose_bot' """
    if usage_time is not None:
        await sql_find_bot.sql_del_last_usage_time(chat_id)
    await sql_find_bot.sql_set_usage_time(chat_id, date_now)
    users = await get_chat_members(chat_id)
    await checking_for_bot(users, chat_id)
    obj = await sql_find_bot.sql_choose_user_command(chat_id)
    return obj


async def choose_user(message: types.Message):
    """ Запуск выполнения команды 'choose_bot' """
    usage_time = await sql_find_bot.sql_check_usage_time(message.chat.id)
    if usage_time is not None:
        usage_time = datetime.strptime(*usage_time, '%Y-%m-%d %H:%M:%S.%f')
    date_now = datetime.now()
    date_24_hours = timedelta(hours=24, minutes=0, seconds=0, microseconds=0)

    if usage_time is None or date_now - usage_time > date_24_hours:
        obj = await command_implementation(usage_time, message.chat.id, date_now)
        return response_choose_user(obj)
    else:
        waiting_time = date_24_hours - (datetime.now() - usage_time)
        await message.answer(f'Команда будет доступна через - {waiting_time}')


async def top_users(message: types.Message):
    """ Вывод топа """
    top = await sql_find_bot.sql_output_top(message.chat.id)
    response = ''
    for index, item in enumerate(top):
        st = f'{index + 1}. {item[0]} - {item[2]} раз(а)'
        response += st + '\n'

    await message.answer(f'Топ {len(top)} ботов: \n' + response)


def register_handlers_find_bot(disp: Dispatcher):
    disp.register_message_handler(choose_user, commands='choose_bot')
    disp.register_message_handler(top_users, commands='top')
