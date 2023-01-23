class Vector:
	"""Векторы и математические функции для них"""

	def __init__(self, x=0, y=0):
		"""Коструктор\nПринимает: (float) x - координата x, (float) y - координата y"""
		self.x = x
		self.y = y
	
	def length(self):
		"""Длина вектора\nВозвращает: (float) - длина вектора"""
		return (x ** 2 + y ** 2) ** 0.5
	
	def __add__(self, y):
		"""Сложение векторов\nПринимает: (Vector or float or int) y - второй член\nВозвращает: (Vector) - сам себя"""
		if type(y) == type(self):
			self.x += y.x
			self.y += y.y
			return self

		if type(y) == type(0) or type(y) == type(0.0):
			self.x += y
			self.y += y
			return self
	
		raise Exception("Unkown type")
		