from create_bot import launch_bot
from aiogram import executor
from create_bot import dp
from HandlersBot import start, audio_ytb_convert, watch_settings, download_audio

launch_bot()

start.register_handler_start(dp)
audio_ytb_convert.register_handlers_audio_ytb(dp)
watch_settings.register_handlers_watch_settings(dp)
download_audio.register_handlers_download_audio(dp)


executor.start_polling(dp, skip_updates=True)
