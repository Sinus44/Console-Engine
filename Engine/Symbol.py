class Symbol:
	"""Описывает символ в консоли"""
	def __init__(self, char:str=" ", background_color:str="", text_color:str=""):
		self.text_color = text_color
		self.background_color = background_color
		self.char = char