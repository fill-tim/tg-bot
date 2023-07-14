from aiogram import types, Dispatcher
from create_bot import bot


async def send_voice_message_pigs(message: types.Message):
    voice_file = open('voice_message/fill_pig.mp3', 'rb')
    await bot.send_voice(chat_id=message.chat.id, voice=voice_file)
    voice_file.close()


def register_handlers_voice_message(disp: Dispatcher):
    disp.register_message_handler(send_voice_message_pigs, commands='pig')
