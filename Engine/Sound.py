import winsound

class Sound:
    """Воспроизведение звуков из WAV файлов"""
    def __init__(self, filePath):
        """
        desc: Воспроизведение звуков из WAV файлов
        in: (str) filePath - Путь к файлу для воспроизведения
        """
        self.filePath = filePath

    def play(self):
        """Начинает воспроизведение"""
        winsound.PlaySound(self.filePath, winsound.SND_FILENAME + winsound.SND_ASYNC)

    def stop(self):
        """Остановка воспроизведения"""
        winsound.PlaySound(None, 0)