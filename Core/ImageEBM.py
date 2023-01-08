from Core.Color import Color
from Core.EBM import EBM

class ImageEBM(EBM):
	"""Импорт картинок пригодных для вставки в Window"""
	
	def __init__(self, path, alpha=False):
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
		if self.alphaColor == color:
			return 0

		return Color.Background.rgb(color[0], color[1], color[2]) + " "