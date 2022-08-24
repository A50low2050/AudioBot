from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from KeyBoardsBot.Keyboard import menu_markup, back_menu
from create_bot import bot, dp


async def start_download(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, f'💠 В этом разделе ты можешь загрузить аудио и \n'
                                    f'отправить его в чат группы\n'
                                    f'\n'
                                    f'Просто отправьте сюда аудио 👇 и я его загружу', reply_markup=back_menu())

    @dp.message_handler(content_types=['audio'])
    async def download_audio(msg: types.Message):
        chat_id = msg.chat.id
        audio_id = msg.audio.file_id

        await bot.send_audio(chat_id, audio=audio_id, reply_markup=menu_markup())
        await bot.send_message(chat_id, 'Загрузка завершенна ✅')


async def back(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Возвращаюсь в меню', reply_markup=menu_markup())


def register_handlers_download_audio(dp: Dispatcher):
    dp.register_message_handler(start_download, Text(equals='Загрузить аудио в чат 📩'))
    dp.register_message_handler(back, Text(equals='Назад 🔙'))
