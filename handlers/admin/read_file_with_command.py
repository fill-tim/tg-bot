from aiogram import types, Dispatcher


async def all_command(message: types.Message):
    with open('all_bot_command', encoding='utf-8') as file:
        content = file.read()
    await message.reply(content)


def register_handlers_command(disp: Dispatcher):
    disp.register_message_handler(all_command, commands='help')
