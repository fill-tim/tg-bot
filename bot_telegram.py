from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Работает')
    sqlite_db.start_db()


from handlers.client import repeat_text, send_voice_message
from handlers.admin import read_file_with_command
from handlers import other

repeat_text.register_handlers_repeat_text(dp)
send_voice_message.register_handlers_voice_message(dp)
read_file_with_command.register_handlers_command(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
