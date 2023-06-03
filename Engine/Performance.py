import time
import timeit

class Performance:
	"""Замер времени выполнения кода"""
	
	startTime = 0
	
	def start():
		"""Указывает начальное время отсчета"""
		Performance.startTime = time.time()
	
	def time() -> float:
		"""Возвращает время прошедшее с точки отсчета"""
		return time.time() - Performance.startTime

	def function(func, repeats:int=1, count:int=1) -> float:
		"""Возвращает время выполнения функции"""
		return timeit.repeat(func, repeat=repeats, number=count)