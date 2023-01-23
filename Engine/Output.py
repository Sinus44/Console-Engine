import ctypes
import os

class Output:
	"""Настройка выходного буффера окна консоли"""

	def init(mode=5):
		"""Иницаилизация окна консоли\nПринимает: (int) mode - режим работы"""
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.SetConsoleMode(handle, mode)
	
	def getTitle():
		"""Получение заголовка окна консоли\nВозвращает: (string) - текущий заголовок окна консоли"""
		out = (ctypes.c_char * 128)()
		ctypes.windll.kernel32.GetConsoleTitleW(ctypes.byref(out), ctypes.wintypes.DWORD(256))
		return str(bytes(out), encoding="utf-8")

	def title(title="Console Engine by Sinus"):
		"""Установка заголовка окна консоли\nПринимает: (string) title - строка заголовок"""
		ctypes.windll.kernel32.SetConsoleTitleW(title)
	
	def resize(w=60, h=40):
		"""Установка размера буффера окна консоли (в символах)\nПринимает: (int) w - ширина окна консоли, (int) h - высота окна консоли"""
		os.system(f'mode con cols={w} lines={h}')
