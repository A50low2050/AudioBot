from moviepy.audio.io.AudioFileClip import AudioFileClip
from Dbase import select_path_videos, select_exit_path
import os

PATH = select_path_videos()
EXIT_PATH = select_exit_path()


class DownloadAudio:

    def __init__(self, name_file):
        self.name_file = name_file

    def download_audio(self):
        try:

            file = self.name_file

            new_file = file.split('.')[0]

            full_path = os.path.join(PATH, file)
            print(full_path)

            audio = AudioFileClip(full_path)

            end_path = os.path.join(EXIT_PATH, new_file + '.mp3')

            audio.write_audiofile(end_path)

            return 'Загрузка аудио завершенна ✅'
        except Exception as ex:
            print(ex)
            return 'К сожалению, не удалось загрузить аудиофайл'
