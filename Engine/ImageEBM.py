from Engine.Color import Color
from Engine.EBM import EBM

class ImageEBM(EBM):
	"""Импорт картинок пригодных для вставки в Window, из формата *.ebm"""
	
	def __init__(self, path, alpha=False):
		"""Конструктор\nПринимает: (sting) path - путь к файлу, (bool) alpha - использовать прозрачность"""
		super().__init__(path)
		self.alpha = alpha
		self.alphaColor = (0, 0, 0)
		self.contentBuffer = self.buffer
		
		self.buffer = []
		for y in range(self.h):
			self.buffer.append([])
			for x in range(self.w):
				color = self.contentBuffer[y][x]
				self.buffer[y].append(self.getColor(color))

	def getColor(self, color):
		"""Внутренний метод для преобразования кортежа цвета в символ-код\nПринимает: (tuple) color - цвет\nВозвращает: (string) - символ код цвета OR (int) - 0 если alpha канал"""
		if self.alphaColor == color:
			return 0

		return Color.rgbBackground(color[0], color[1], color[2]) + " "