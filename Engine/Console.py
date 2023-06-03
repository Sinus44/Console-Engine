import ctypes
import sys
import os
import ctypes.wintypes
import threading
import time
import win32file
import win32pipe
import random
import json

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.wintypes._COORD),
        ("dwCursorPosition", ctypes.wintypes._COORD),
        ("wAttributes", ctypes.wintypes.WORD),
        ("srWindow", ctypes.wintypes.SMALL_RECT),
        ("dwMaximumWindowSize", ctypes.wintypes._COORD),
    ]

class Console:
	"""Создание дополнительного отдельного окна консоли"""
	def __init__(self):
		self.id = random.randint(1000, 9999)
		self.pipe_out_name = r"\\.\pipe\consoleout" + str(self.id)
		self.pipe_in_name = r"\\.\pipe\consolein" + str(self.id)
		self.enable = False

		self.pipe_in = win32pipe.CreateNamedPipe(
			self.pipe_in_name,
			win32pipe.PIPE_ACCESS_DUPLEX,
			win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
			1, 1024 * 1024, 1024 * 1024, 0, None
		)

		threading.Thread(target=os.system, args=[f"start py ./engine/sub_console.py {self.id}"], daemon=False).start()
		time.sleep(0.5)

		try:
			self.pipe_out = win32file.CreateFile(
				self.pipe_out_name,
				win32file.GENERIC_READ | win32file.GENERIC_WRITE,
				0, None,
				win32file.OPEN_EXISTING,
				0, None
			)
			self.enable = True
		except:
			print(f"[ERROR][Console] Не удалось соединится с консолью")
			self.pipe_out = None
			self.enable = False

	def _send_(self, data):
		"""Байтовая отправка команд"""
		if not self.enable: return
		try:
			win32file.WriteFile(self.pipe_out, data)
		except:
			self.enable = False

	def _get_(self):
		"""Байтовое принятие команд"""
		if not self.enable: return
		try:
			return win32file.ReadFile(self.pipe_in, 1024 * 1024)
		except:
			self.enable = False

	def input_init(self):
		"""Инициализация ввода"""
		request = (8).to_bytes(1, "little")
		self._send_(request)

	def input_tick(self):
		"""Получение ивентов"""
		request = (7).to_bytes(1, "little")
		self._send_(request)
		res = self._get_()
		return json.loads(res[1][1:].decode()) if res != None else [{'type': 'exit'}]

	def print(self, data):
		"""Вывод в консоль"""
		request = ((2).to_bytes(1, "little")) + data.encode()
		self._send_(request)

	def set_size(self, w:int, h:int):
		"""Изменение размера консоли"""
		if w > 255 or h > 255: return
		request = ((5).to_bytes(1, "little")) + ((w).to_bytes(1, "little")) + ((h).to_bytes(1, "little"))
		self._send_(request)
		time.sleep(0.1)

	def set_title(self, title:str):
		"""Смена заголовка"""
		request = ((3).to_bytes(1, "little")) + title.encode()
		self._send_(request)
		time.sleep(0.01)

	def set_icon(self, path:str):
		"""Смена иконки"""
		request = ((4).to_bytes(1, "little")) + path.encode()
		self._send_(request)

	def close(self):
		"""Закрытие окна"""
		if not self.enable: return
		request = (1).to_bytes(1, "little")
		self._send_(request)
		self.enable = False

	def get_size(self):
		"""Получение размеров окна"""
		request = ((6).to_bytes(1, "little"))
		self._send_(request)
		time.sleep(1)
		res = self._get_()
		if int(res[1][0]) == 1:
			return (int(res[1][1]), int(res[1][2]))
		else:
			return (0, 0)

	def __del__(self):
		self.close()