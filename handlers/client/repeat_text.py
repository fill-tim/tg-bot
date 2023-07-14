from aiogram import types, Dispatcher
from create_bot import bot


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здарова бандиты')


# @dp.message_handler(commands=['Напомни'])
async def remind_text(message: types.Message):
    await message.answer('Введите текст, который нужно напомнить')


def register_handlers_client(disp: Dispatcher):
    disp.register_message_handler(command_start, commands=['start', 'help'])
    disp.register_message_handler(remind_text, commands=['Напомни'])
