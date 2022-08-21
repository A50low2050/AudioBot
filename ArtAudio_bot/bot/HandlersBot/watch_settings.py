from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from Dbase import select_path_videos, select_exit_path
from KeyBoardsBot.Keyboard import watch_my_settings, menu_markup


async def watch_settings(msg: types.Message):
    chat_id = msg.chat.id
    await bot.send_message(chat_id, '💠 В этом разделе ты можешь просмотреть свои настройки\n'
                                    '\n'
                                    'Нажми на кнопку "Просмотеть 👁" и ты увидишь какие настройки у тебя установлены',
                           reply_markup=watch_my_settings())


async def my_settings(msg: types.Message):
    chat_id = msg.chat.id

    path = select_path_videos()
    exit_path = select_exit_path()

    if path and exit_path:

        await bot.send_message(chat_id, f'🎞 Место сохранения ваших видео:\n'
                                        f'{path}\n'
                                        f'\n'
                                        f'💿 Путь сохранения ваших аудио:\n'
                                        f'{exit_path}', reply_markup=menu_markup())
    else:
        await bot.send_message(chat_id, 'У вас нет никаких настроек ❗', reply_markup=menu_markup())


async def cancel(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Отмена операции', reply_markup=menu_markup())


def register_handlers_watch_settings(dp: Dispatcher):
    dp.register_message_handler(watch_settings, Text(equals='Просмотреть настройки 👁‍'))
    dp.register_message_handler(my_settings, Text(equals='Просмотреть 👁'))
    dp.register_message_handler(cancel, Text(equals='Отмена ❌'))
