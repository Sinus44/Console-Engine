class Mmath:
	"""Математические функции"""

	def round(x):
		"""Правильное математическое округление\nПринимает: (float OR int) x - число\nВозвращает: (int) x - округленное число"""
		return int((x // 1) if x % 1 < 0.5 else ((x // 1) + 1))
	
	def clamp(x, minValue=0, maxValue=1):
		"""Ограничение значения минимальным и максимальным\nПринимает: (float OR int) x - число, (float OR int) maxValue - максимальное значение, (float OR int) minValue - минимальное значение\nВозвращает: (float OR int) - число в заданном диапазоне"""
		return max(min(x, maxValue), minValue)