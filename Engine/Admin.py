import ctypes
import sys

class Admin:
	"""Запуск от имени адмнистратора"""

	def checkAdmin():
		"""Проверяет запущен ли скрипт с правами администратора\nВозвращает: (bool) - True если скрипт запущен с правами администратора"""
		return bool(ctypes.windll.shell32.IsUserAnAdmin())

	def restartAsAdmin():
		"""Перезапускает скрипт с правами администратора"""
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,__file__, None, 1)
		exit()