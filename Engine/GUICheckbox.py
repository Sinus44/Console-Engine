from Engine.GUIElement import Element

class Checkbox(Element):
	"""[GUI] Чекбокс - Переключатель"""

	def __bool__(self):
		"""Возвращает состояние переключателя"""
		return self.checked

	def on_left_click(self, event):
		"""Событие нажатия"""
		self.checked = not(self.checked)
		self.on_change(event)

	def draw(self):
		"""Отрисовка"""
		text = ("[X] " if self.checked else "[ ] ") + self.text
		self.intersection_length = len(text)

		if self.enable:
			if self.hovered:
				self.window.text(self.x, self.y, text, text_prefix=self.style.background_fill + self.style.text_fill)
			else:
				self.window.text(self.x, self.y, text, text_prefix=self.style.background + self.style.text)
		else:
			self.window.text(self.x, self.y, text, text_prefix=self.style.disable + self.style.text)