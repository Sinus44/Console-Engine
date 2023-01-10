from Engine.Byte import Byte

class EBM:
	"""Импорт файлов *.ebm, получение данных из файла и их структуризация"""
	
	def __init__(self, path):
		"""Импорт файлов *.ebm, получение данных из файла и их структуризация"""
		self.path = path

		file = open(path, "rb")
		self.dataBytes = file.read()
		file.close()

		self.dataHex = Byte.bytesToHex(self.dataBytes)

		if Byte.getHexBytesSize(self.dataHex, Byte.hexToDec("0"), 3) != "45424d":
			raise Exception("Incorrect type")

		self.w = Byte.hexToDec(Byte.getHexBytesSize(self.dataHex, Byte.hexToDec("3"), 2))
		self.h = Byte.hexToDec(Byte.getHexBytesSize(self.dataHex, Byte.hexToDec("5"), 2))

		self.pixelsCount = self.w * self.h

		pixelsHexData = self.dataHex[Byte.hexToDec("7")*2:]
		pixelsHexArray = []

		for _ in range(self.pixelsCount):
			pixelData = pixelsHexData[:6]
			pixelsHexData = pixelsHexData[6:]
			pixelsHexArray.append(pixelData)

		self.array = []
		for i in range(self.h):
			string = []
			for j in range(self.w):
				pos = i * self.w + j

				x1 = Byte.hexToDec(pixelsHexArray[pos][:2])
				x2 = Byte.hexToDec(pixelsHexArray[pos][2:4])
				x3 = Byte.hexToDec(pixelsHexArray[pos][4:])

				string.append((x1, x2, x3))

			self.array.append(tuple(string))

		self.buffer = tuple(self.array)