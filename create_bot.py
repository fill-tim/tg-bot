from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# PROXY_URL = 'http://proxy.server:3128'
# bot = Bot(token=TOKEN, proxy=PROXY_URL)

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
