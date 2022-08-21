from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from create_bot import bot, dp
from KeyBoardsBot.Keyboard import menu_markup, convert_audio_settings
from Dbase import update_path, select_path, select_exit_path, insert_path
from Proccesssor.converter import DownloadAudio


class StatusBot(StatesGroup):
    link = State()
    path_videos = State()
    exit_path = State()


async def start_upload_audio(msg: types.Message):
    chat_id = msg.chat.id
    user = msg.from_user.first_name
    message = f'💠 Итак, {user}, ты выбрал данный раздел.\n' \
              f'\n' \
              f'❗ Прежде чем начать, нужно указать пути, где хранятся твои видеозаписи и куда ты собираешься сохранить аудиозаписи.\n' \
              f'\n' \
              f'Поэтому зайди в раздел "Настройки ⚙" и укажи пути\n' \
              f'Если ты уже все настроил, то нажми "Начать  ▶"'

    await bot.send_message(chat_id, message, reply_markup=convert_audio_settings())


async def upload_audio(msg: types.Message):
    chat_id = msg.chat.id

    select_answer = select_path()
    if select_answer:
        await bot.send_message(chat_id, 'Загрузите видео в чат бот\n', reply_markup=ReplyKeyboardRemove())
    else:
        await bot.send_message(chat_id, 'Мне нужно пути, где вы храните видеозаписи и куда нужно сохранять аудио ❗\n'
                                        '\n'
                                        'Пожалуйста войдите в раздел "Настройки ⚙" и укажите пути сохранения')

    @dp.message_handler(content_types=['video'])
    async def upload_video_in_chat(msg: types.Message):
        chat_id = msg.chat.id
        file_name = msg.video.file_name
        exit_path = select_exit_path()
        user = msg.from_user.first_name

        await bot.send_message(chat_id, f'📋 Файл: {file_name}\n'
                                        f'📂 Путь сохранения: {exit_path}\n'
                                        f'📩 Отправитель: {user}\n'
                                        f'\n'
                                        f'Подождите пожалуйста, это займет несколько секунд 🕞')
        answer = DownloadAudio(file_name).download_audio()

        await bot.send_message(chat_id, answer, reply_markup=menu_markup())


async def cancel(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Отмена операции', reply_markup=menu_markup())


async def settings(msg: types.Message):
    chat_id = msg.chat.id

    await bot.send_message(chat_id, 'Введите путь, где хранятся ваши видео\n'
                                    '\n'
                                    r'📌 Пример: "C:\Users\Admin\Desktop\my_video"')
    await StatusBot.path_videos.set()


async def get_save_videos(msg: types.Message, state: FSMContext):
    chat_id = msg.chat.id
    path = msg.text

    async with state.proxy() as data:
        data['path'] = path

    await bot.send_message(chat_id, 'Теперь укажи путь, куда ты будешь сохранять свои аудиозаписи\n'
                                    '\n'
                                    r'📌 Пример: "C:\Users\Admin\Desktop\save_audio"')
    await StatusBot.exit_path.set()


async def get_exit_path(msg: types.Message, state: FSMContext):
    chat_id = msg.chat.id
    exit_path = msg.text

    async with state.proxy() as data:
        data['exit_path'] = exit_path

    user_path = data['path']
    user_exit_path = data['exit_path']

    result = select_path()

    if result:
        update_path(user_path, user_exit_path)
        await bot.send_message(chat_id, 'Изменения обновлены ✅', reply_markup=menu_markup())
        await state.finish()

    else:
        insert_path(user_path, user_exit_path)
        await bot.send_message(chat_id, 'Изменения добавлены ✅', reply_markup=menu_markup())
        await state.finish()


def register_handlers_audio_ytb(dp: Dispatcher):
    dp.register_message_handler(start_upload_audio, Text(equals='Преобразовать видео в аудио 🔁'))
    dp.register_message_handler(upload_audio, Text(equals='Начать ▶'))

    dp.register_message_handler(settings, Text(equals='Настройки ⚙'))
    dp.register_message_handler(get_save_videos, state=StatusBot.path_videos)
    dp.register_message_handler(get_exit_path, state=StatusBot.exit_path)

    dp.register_message_handler(cancel, Text(equals='Отмена ❌'))
