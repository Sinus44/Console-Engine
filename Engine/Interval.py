import threading
import time

class Interval:
	"""Цикличный вызов функции в соответветсвии с интервалом"""

	def __init__(self, callback, t=1, daemon=False):
		"""Конструктор\nПринимает: (function) callback - функция для вызова, (float) t - время в секундах, (bool) daemon - закрытие потока при закрытии главного потока"""
		self.on = False
		self.callback = callback
		self.time = t
		self.thread = threading.Thread(target=self.function, daemon=daemon)

	def start(self):
		"""Запускает цикл"""
		self.on = True
		self.thread.start()

	def stop(self):
		"""Останавливает цикл"""
		self.on = False
	
	def function(self):
		"""Метод котоый будет запущен в отдельном потоке"""
		while self.on:
			self.callback()
			time.sleep(self.time)