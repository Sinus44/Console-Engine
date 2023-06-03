from Engine.Input import Input

class Element:
	"""[GUI] База для GUI элементов"""
	
	def __init__(self, **kwargs):
		self.__dict__ = kwargs
		
		if not "enable" in self.__dict__: self.enable = True
		if not "visible" in self.__dict__: self.visible = True
		if not "checked" in self.__dict__: self.checked = False

		if "text" in self.__dict__:
			self.intersection_length = len(self.text)
		else:
			self.text = ""
			self.intersection_length = 0

		self.hovered = False
		self.mouse_key = -1

	def block(self):
		"""Блокировка элемента"""
		self.hovered = False
		self.enable = False

	def intersection(self, x, y):
		"""Проверка на пересечение по координатам"""
		return (self.x <= x < self.x + self.intersection_length) and (self.y == y)

	def event(self, event):
		"""Передайте ивент для выполнения биндов"""
		if self.enable:
			if event["type"] == "mouse":
				if event["mouse_type"] == 1:
					if self.intersection(event["x"], event["y"]):
						self.on_hover(event)
					else:
						self.no_hover(event)

				if event["mouse_key"] != self.mouse_key:
					if self.intersection(event["x"], event["y"]):
						if event["mouse_key"] == 0:
							self.on_mouse_up(event)

						elif event["mouse_key"] == 1:
							self.on_left_click(event)

						elif event["mouse_key"] == 2:
							self.on_right_click(event)

				self.mouse_key = event["mouse_key"]

	def on_hover(self, event):
		"""Наведение мышью на элемент"""
		self.hovered = True

	def no_hover(self, event):
		"""Ивент если мышь более не наведена на элемент"""
		self.hovered = False

	def on_mouse_up(self, event):
		"""Ивент отпускания кнопки мыши"""
		...

	def on_left_click(self, event):
		"""Ивент нажатия ЛКМ"""
		...

	def on_right_click(self, event):
		"""Ивент нажатия ЛКМ"""
		...

	def on_change(self, event):
		"""Изменение состояние"""
		...

	def on_select(self, event):
		"""Выбор элемента"""
		...
