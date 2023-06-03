from Engine.GUIStyle import Style

class Border:
	"""[GUI] Рамка для изображения"""
	
	def __init__(self, window:object, style:object, symbol:str="*"):
		self.window = window
		self.style = style
		self.symbol = symbol
		
	def draw(self):
		"""Отрисовка"""
		self.window.rect(0, 0, self.window.w, self.window.h, self.style.text + self.style.background + self.symbol)