from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyrogram import Client

# PROXY_URL = 'http://proxy.server:3128'
# bot = Bot(token=TOKEN, proxy=PROXY_URL)

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
api_id = 24360033
api_hash = 'ae42a455f97b7c0221d4f91fa11fd8a2'
bot_token = os.getenv('TOKEN')
app = Client(name='GariginBot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)
