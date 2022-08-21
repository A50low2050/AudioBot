from aiogram import types, Dispatcher
from create_bot import bot
from KeyBoardsBot.Keyboard import menu_markup


async def send_welcome(message: types.Message):

    chat_id = message.chat.id
    full_name_user = message.from_user.full_name
    await bot.send_message(chat_id, f'Привет,{full_name_user}✋\n'
                           'Выбери, что тебе нужно👇', reply_markup=menu_markup())


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])

