class Byte:
	"""Работа с данными BYTES-HEX-DEC-STRING"""

	def stringToBytes(string):
		"""Преобразует строку в байты\nПринимает: (string) string - входная строка\nВозвращает: (bytes) - Массив байтов"""
		return bytes(string, "utf-8")

	def hexToFixedHex(hex, length):
		"""Добавляет нули до определенного кол-ва длины всей строки\nПринимает: (string) hex - строка с содержимым формата hex, (int) length - длинна которую необходимо достичь"""
		return ("0" * (length - len(hex))) + hex

	def bytesToInt(b):
		"""Преобразует BYTES в INT\nПринимает: (bytes) b - Байт\nВозвращает: (int) - число"""
		return int(b)

	def bytesToHex(b):
		"""Преобразует BYTES в HEX\nПринимает: (bytes) b - Массив байтов\nВозвращает: (string) - Строка формата hex"""
		return b.hex()

	def hexStringToBytes(hex):
		"""Преобразует HEX_STRING в BYTES\nПринимает: (string) hex - строка формата hex\nВозвращает: (bytes) - массив байт"""
		outBytes = b""
		for i in range(0, len(hex),2):
			outBytes += Byte.hexToBytes(hex[i:i+2])

		return outBytes
	
	def hexToBytes(hex):
		"""Преобразует HEX в BYTES\nПринимает: (string) hex - hex-байт\nВозвращает: (bytes) - байт"""
		return Byte.decToBytes(Byte.hexToDec(hex))
	
	def hexToDec(hex):
		"""Преобразует HEX в INT\nПринимает: (string) hex - hex-байт\nВозвращает: (int) - число"""
		return int(hex, base=16)

	def decToHex(dec):
		"""Преобразует INT в HEX\nПринимает: (int) dec - число\nВозвращает: (string) hex - строка формата hex"""
		return hex(dec)[2:]
	
	def decToBytes(dec):
		"""Преобразует INT в BYTES\nПринимает: (int) dec - число\nВозвращает: (bytes) - массив байт"""
		return dec.to_bytes(1, 'little')

	def getHexByte(hex, pos):
		"""Возвращает HEX_BYTE из HEX_STRING по номеру позиции\nПринимает: (string) hex - строка формата hex, (int) pos - позиция необходимого байта\nВозвращает: (string) hex - hex-байт"""
		return hex[pos * 2] + hex[pos * 2 + 1]

	def getHexBytesSize(hex, pos, size):
		"""Возвращает HEX_BYTES из HEX_STRING с начальной позиции указанной длиной\nПринимает: (string) hex - строка формата hex, (int) pos - позиция необходимого байта, (int) size - кол-во необходимых байт\nВозвращает: (string) - строка формата hex"""
		return Byte.getHexBytesNormal(hex, pos, pos + size - 1)

	def getHexBytesNormal(hex, startPos, endPos):
		"""Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной\nПринимает: (string) hex - строка формата hex, (int) startPos - начальная позиция, (int) endPos - конечная позиция\nВозвращает: (string) - строка формата hex"""
		return hex[startPos*2:(endPos+1)*2]

	def getHexBytesReverse(hex, startPos, endPos):
		"""Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной, обратный порядок байт\nПринимает: (string) hex - строка формата hex, (int) startPos - начальная позиция, (int) endPos - конечная позиция\nВозвращает: (string) - строка формата hex"""
		outStr = ""
		
		for i in range(endPos, startPos - 1, -1):
			outStr += Byte.getHexByte(hex, i)
	
		return outStr
