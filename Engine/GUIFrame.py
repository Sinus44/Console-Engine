from Engine.Symbol import Symbol

class Frame:
	"""[GUI] Фон"""
	
	def __init__(self, window:object, style:object):
		self.window = window
		self.style = style
	
	def draw(self):
		"""Отрисовка"""
		self.window.fill(Symbol(background_color=self.style.background, char=" "))