import ctypes
import os
import time
from Engine.Console import Console
from Engine.Symbol import Symbol

class Window:
	"""Изображение в консоли"""

	def __init__(self, w:int, h:int):
		self.console = Console()

		self.input_tick = self.console.input_tick
		self.set_title = self.console.set_title
		self.set_icon = self.console.set_icon
		self.close = self.console.close

		self.size = self.console.set_size(w, h)
		self.console.input_init()

		self.w = w
		self.h = h

		self.buffer = []
		for i in range(self.h):
			self.buffer.append([])
			for j in range(self.w):
				self.buffer[i].append([])

		self.prev_frame = None

	def set_size(self, w:int, h:int):
		"""Изменение размеров окна"""
		self.w = w
		self.h = h
		self.console.set_size(self.w, self.h)
		self.console.input_init()

	def print(self):
		"""Вывод буффера в консоль"""
		if self.prev_frame and self.prev_frame == self.buffer:
			...#return

		s = ""
		for string in self.buffer:
			string_text = ""
			prev_symb = Symbol()

			for symbol in string:
				if symbol.text_color != prev_symb.text_color: string_text += symbol.text_color
				if symbol.background_color != prev_symb.background_color: string_text += symbol.background_color
				string_text += symbol.char
				prev_symb = symbol

			s += string_text

		self.console.print(s)
		self.prev_frame = self.buffer

	def clear(self):
		"""Отчистка вывода в консоль"""
		self.fill()
		self.print()

	def fill(self, symbol:object=None):
		"""Заливка всего буффера определенным символом"""
		for i in range(self.h):
			for j in range(self.w):
				self.point(j, i, symbol)

	def point(self, x:int, y:int, symbol:object=None):
		x = int(x)
		y = int(y)
		"""Установка символа в буффер по координатам"""
		if (0 <= x < self.w) and (0 <= y < self.h):
			self.buffer[y][x] = symbol or Symbol()

	def rect_fill(self, x:int=0, y:int=0, w:int=1, h:int=1, symbol:object=None):
		"""Заполненный прямоугольник в буффер"""
		for i in range(h):
			for j in range(w):
				self.point(j + x, i + y, symbol)

	def rect(self, x:int=0, y:int=0, w:int=1, h:int=1, symbol:object=None):
		"""Пустотелый прямоугольник в буффер"""
		for i in range(h):
			for j in range(w):
				if i == 0 or i == h-1 or j == 0 or j == w - 1:
					self.point(j + x, i + y, symbol)

	def circle_fill(self, x:int=0, y:int=0, r:int=1, symbol:object=None):
		"""Залитый круг в буффер"""
		for i in range(self.h):
			for j in range(self.w):
				if (i - y) ** 2 + (j - x) ** 2  <= r ** 2:
					self.point(j, i, symbol)

	def circle(self, x:int=0, y:int=0, r:int=1, symbol:object=None):
		"""Пустотелый круг в буффер"""
		disp_x = x
		disp_y = y
		x = 0
		y = r
		delta = (1 - 2 * r)
		error = 0
		while y >= 0:
			self.point(disp_x + x, disp_y + y, symbol)
			self.point(disp_x + x, disp_y - y, symbol)
			self.point(disp_x - x, disp_y + y, symbol)
			self.point(disp_x - x, disp_y - y, symbol)

			error = 2 * (delta + y) - 1
			if ((delta < 0) and (error <= 0)):
				x += 1
				delta = delta + (2 * x + 1)
				continue
			error = 2 * (delta - x) - 1
			if ((delta > 0) and (error > 0)):
				y -= 1
				delta = delta + (1 - 2 * y)
				continue
			x += 1
			delta = delta + (2 * (x - y))
			y -= 1

	def line(self, x1:int=0, y1:int=0, x2:int=0, y2:int=0, symbol:object=None):
		"""Линия по координатам"""
		delX = abs(x2 - x1)
		delY = abs(y2 - y1)

		signX, signY = 0, 0

		if x1 < x2: signX = 1
		else: signX = -1

		if y1 < y2: signY = 1
		else: signY = -1

		error = delX - delY
		self.point(x2, y2, symbol)

		while (x1 != x2 or y1 != y2): 
			self.point(x1, y1, symbol)
			error_2 = error * 2
		
			if error_2 > -delY: 
				error -= delY
				x1 += signX
		
			if error_2 < delX:
				error += delX
				y1 += signY

	def text(self, x:int, y:int, text:str="TEXT", background_color:str="", text_color:str=""):
		"""Текст"""
		text = str(text)
		x = int(x)
		y = int(y)

		if (x < 0 or y < 0) or (x + len(text) > self.w):
			return

		for i in range(len(text)):
			self.point(x + i, y, Symbol(background_color=background_color, text_color=text_color, char=text[i]))

	def table(self, x, y, data, header):
		"""Таблица"""
		data = data.copy()
		header = header.copy()

		for i, row in enumerate(data):
			for j, cell in enumerate(row):
				data[i][j] = str(cell)

		max_widths = []
		for title in header:
			max_widths.append(len(title))

		for i, row in enumerate(data):
			for j, cell in enumerate(row):
				max_widths[j] = max(max_widths[j], len(cell))

		width = sum(max_widths) + len(max_widths) + 1

		# Нормализация длины заголовка
		for i, title in enumerate(header):
			header[i] += " " * (max_widths[i] - len(title))

		# Нормализация длины информации
		for i, row in enumerate(data):
			for j, cell in enumerate(row):
				data[i][j] += " " * (max_widths[j] - len(data[i][j]))

		out_strings = []

		out_strings.append("-" * width)
		out_strings.append("|" + "|".join(header) + "|")
		out_strings.append("-" * width)

		for row in data:
			out_strings.append("|" + "|".join(row) + "|")

		out_strings.append("-" * width)

		for i, string in enumerate(out_strings):
			self.text(x, y + i, string)