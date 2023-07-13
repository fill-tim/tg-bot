from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(disp: Dispatcher):
    disp.register_message_handler(echo_send)
