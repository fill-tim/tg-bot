from aiogram import types, Dispatcher


# @dp.message_handler()
async def error_command(message: types.Message):
    if message.text[0] == '/':
        await message.reply('Такой команды не существует! Для просмотра команд введите /help.')


def register_handlers_other(disp: Dispatcher):
    disp.register_message_handler(error_command)
