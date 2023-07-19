from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove

from create_bot import bot


class FSMRepeat(StatesGroup):
    """ Создаем состояния """
    text = State()  # Состояние текста
    number = State()  # Состояние числового значения


async def cancel_handler(message: types.Message, state: FSMContext):
    """ Выполняем выход с помощью команды/слова 'отмена' """
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.chat.id, 'Хорошо')


async def repeat_text_start(message: types.Message):
    await FSMRepeat.text.set()  # Ожидаем состояние 'text'
    await message.reply('Введите текст')


async def load_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text  # Заполняем состояние 'text' введенным текстом
    await FSMRepeat.next()  # Ожидаем следующее состояние 'number'
    await message.reply('Введите число повторов')


async def load_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['number'] = int(message.text)  # Проверяем, чтобы сообщение было числом
            await message.reply((data['text'] + ' ') * data['number'])  # Выводим несколько раз
            await state.finish()
        except:
            await message.reply('Введите число')


def register_handlers_repeat_text(disp: Dispatcher):
    """ Регистрируем handlers """
    disp.register_message_handler(cancel_handler, state='*', commands='cancel')
    disp.register_message_handler(repeat_text_start, commands='repeat')
    # disp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    disp.register_message_handler(load_text, content_types=['text'], state=FSMRepeat.text)
    disp.register_message_handler(load_number, state=FSMRepeat.number)
