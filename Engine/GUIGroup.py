from Engine.Logging import Logging

class Group:
	"""[GUI] Группа GUI элементов"""

	def __init__(self, window:object, x:int, y:int, interval:int=1):
		self.window = window
		self.x = x
		self.y = y
		self.elements = []
		self.interval = interval
		self.selected = {}

	def append(self, element:object):
		"""Добавление элементов в группу"""
		self.elements.append(element)
	
	def eventHandler(self):
		"""Обработка событий для всех элементов в группе"""
		for element in self.elements:
			element.intersectionFromEvent()

			if hasattr(element, "inputFromEvent"):
				element.inputFromEvent()
	
	def click(self):
		"""Обработка событий для всех элементов в группе"""
		for element in self.elements:
			if element.focused:
				element.click(element)
	
	def sort(self):
		"""Автопозиционирование элементов группы"""
		for i in range(len(self.elements)):
			element = self.elements[i]
			element.x = self.x
			element.y = self.y + i * (self.interval + 1)

	def draw(self):
		"""Отрисовка всех элементов группы"""
		for element in self.elements:
			element.draw()