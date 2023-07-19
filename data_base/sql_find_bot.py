import random

from create_bot import bot
from data_base.sqlite_db import cur, base


async def sql_add_participant(dct):
    """ Добавление участника """
    user = cur.execute(
        "SELECT first_name FROM participant WHERE (first_name = ? and chat_id = ?)", (dct['first_name'], dct['chat_id'])
    )

    if user.fetchone() is None:
        cur.execute(
            "INSERT INTO participant (chat_id,first_name, user_id, num) VALUES (?, ?, ?, ?)", (tuple(dct.values()))
        )
        base.commit()


async def sql_all_participant_command(chat_id):
    """ Все участники определенного чата"""
    mass = []
    for ret in cur.execute('SELECT first_name, user_id, num FROM participant WHERE chat_id = ? ',
                           (chat_id,)).fetchall():
        mass.append(ret)
    return mass


async def sql_insert_num_command(chat_id, user_id, num):
    """ Изменение счета пользователя """
    cur.execute("UPDATE participant SET num = ? WHERE user_id = ? and chat_id = ?", (num + 1, user_id, chat_id))
    base.commit()


async def sql_choose_user_command(chat_id):
    """ Выбор 'бота' """
    users = await sql_all_participant_command(chat_id)
    if len(users) != 0:
        response = []
        for item in users:
            response.append(item)

        user = random.choice(response)
        await sql_insert_num_command(chat_id, user[1], user[2])
        return user[0]
    else:
        return None


async def sql_output_top(chat_id):
    """ Вывод топа """
    users = await sql_all_participant_command(chat_id)
    mass = sorted(users, key=lambda num: num[2], reverse=True)
    return mass


async def sql_check_usage_time(chat_id):
    """ Проверка когда последний раз была использована команда 'choose_bot' """
    usage_time = cur.execute("SELECT usage_time FROM usage_record WHERE chat_id = ?", (chat_id,))
    return usage_time.fetchone()


async def sql_set_usage_time(chat_id, usage_time):
    """ Запись времени последнего использования команды 'choose_bot' """
    cur.execute("INSERT INTO usage_record(chat_id, usage_time) VALUES (?, ?)", (chat_id, usage_time))


async def sql_del_last_usage_time(chat_id):
    """ Удаление последней записи времени использования команды 'choose_bot' """
    cur.execute("DELETE FROM usage_record WHERE chat_id = ?", (chat_id,))
