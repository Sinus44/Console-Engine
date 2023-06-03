import winsound

class Sound:
    """Воспроизведение звуков из WAV файлов"""
    def __init__(self, file_path:str):
        self.file_path = file_path

    def play(self):
        """Начинает воспроизведение"""
        winsound.PlaySound(self.file_path, winsound.SND_FILENAME + winsound.SND_ASYNC)

    def stop(self):
        """Остановка воспроизведения"""
        winsound.PlaySound(None, 0)