from aiogram import types, Dispatcher

from create_bot import bot
from key_boards import kb_client


async def output_all_command(message: types.Message):
    with open('all_bot_command', encoding='utf-8') as file:
        content = file.read()
    await message.reply(content)
    # await bot.send_message(chat_id=message.chat.id, text=content, reply_markup=kb_client)


def register_handlers_command(disp: Dispatcher):
    disp.register_message_handler(output_all_command, commands='help')
