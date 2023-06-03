from Engine.Color import Color

class Style():
	"""[GUI] Настройка цветов для GUI элементов"""

	def __init__(self, text:str=None, text_fill:str=None, background:str=None, background_fill:str=None, disable:str=None):
		self.text = text or Color.rgb_text(196, 196, 196)
		self.text_fill = text_fill or Color.rgb_text(255, 255, 255)

		self.background = background or Color.rgb_background(0, 0, 0)
		self.background_fill = background_fill or Color.rgb_background(127, 127, 127)

		self.disable = disable or Color.rgb_background(0, 0, 0)