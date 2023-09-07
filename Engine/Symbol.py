from Engine.Color import Color


class Symbol:
	"""Описывает символ в консоли"""
	def __init__(self, char:str=" ", background_color:str="", text_color:str=""):
		"""char - сам символ, background_color - цвет фона, text_color - цвет текста"""
		self.text_color = text_color or Color.default
		self.background_color = background_color or Color.default
		self.char = char