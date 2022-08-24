from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def menu_markup():
    btn_download_video_url = KeyboardButton('Преобразовать видео в аудио 🔁')
    btn_watch_settings = KeyboardButton('Просмотреть настройки 👁‍')
    btn_download_audio_in_chat = ('Загрузить аудио в чат 📩')
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
        btn_download_video_url,
        btn_watch_settings,
        btn_download_audio_in_chat,
    )

    return menu


def back_menu():
    btn_back = KeyboardButton('Назад 🔙')
    back = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_back)

    return back


def convert_audio_settings():
    btn_settings = KeyboardButton('Настройки ⚙')
    btn_cancel = KeyboardButton('Отмена ❌')
    btn_start = KeyboardButton('Начать ▶')
    settings = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btn_settings, btn_cancel, btn_start)

    return settings


def watch_my_settings():
    btn_watch = KeyboardButton('Просмотреть 👁')
    btn_cancel = KeyboardButton('Отмена ❌')
    my_settings = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btn_watch, btn_cancel)

    return my_settings
