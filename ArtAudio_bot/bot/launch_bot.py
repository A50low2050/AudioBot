
from aiogram import executor
from create_bot import dp
from HandlersBot import start, audio_ytb_convert, watch_settings


start.register_handler_start(dp)
audio_ytb_convert.register_handlers_audio_ytb(dp)
watch_settings.register_handlers_watch_settings(dp)


executor.start_polling(dp, skip_updates=True)
