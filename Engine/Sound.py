import winsound

class Sound:
    """Воспроизведение звуков из WAV файлов"""
    def __init__(self, file_path:str):
        """Примает путь к файлу для воспроизведения"""
        self.file_path = file_path

    def play(self, use_async=True):
        """Начинает воспроизведение"""
        winsound.PlaySound(self.file_path, winsound.SND_FILENAME + (winsound.SND_ASYNC if use_async else 0))

    def stop(self):
        """Остановка воспроизведения"""
        winsound.PlaySound(None, 0)