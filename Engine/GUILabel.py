from Engine.GUIElement import Element

class Label(Element):
	"""[GUI] Текст"""
	def draw(self):
		"""Отрисовка"""
		if self.visible:
			self.window.text(self.x, self.y, self.text, text_prefix=self.style.background + self.style.text)