from Engine.GUIElement import Element

class Button(Element):
	"""[GUI] Кнопка"""

	def on_hover(self, event):
		"""Мышь наведена"""
		self.hovered = True

	def no_hover(self, event):
		"""Более мышь не наведена"""
		self.hovered = False
	
	def format(self):
		"""Формат кнопки"""
		return f"[ {self.text} ]"

	def draw(self):
		"""Отрисовка"""
		text = self.format()
		self.intersection_length = len(text)

		if self.enable:
			if self.hovered:
				self.window.text(self.x, self.y, text, text_prefix=self.style.background_fill + self.style.text_fill)
			else:
				self.window.text(self.x, self.y, text, text_prefix=self.style.background + self.style.text)
		else:
			self.window.text(self.x, self.y, text, text_prefix=self.style.disable + self.style.text)