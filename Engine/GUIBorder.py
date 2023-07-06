from Engine.GUIStyle import Style
from Engine.Symbol import Symbol

class Border:
	"""[GUI] Рамка для изображения"""
	
	def __init__(self, window:object, style:object, symbol:str="*"):
		self.window = window
		self.style = style
		self.symbol = symbol
		
	def draw(self):
		"""Отрисовка"""
		self.window.rect(0, 0, self.window.w, self.window.h, Symbol(char=self.symbol, text_color=self.style.text, background_color=self.style.background))