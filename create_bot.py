from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

# PROXY_URL = 'http://proxy.server:3128'
# bot = Bot(token=TOKEN, proxy=PROXY_URL)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
