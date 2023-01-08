class Byte:
	def bytesToHex(b):
		"""Преобразует BYTES в строку с HEX"""
		return b.hex()

	def getHexByte(hex, pos):
		"""Возвращает байт в виде HEX из HEX строки по номеру позиции"""
		return hex[pos * 2] + hex[pos * 2 + 1]

	def getHexBytesSize(hex, pos, size):
		return Byte.getHexBytesNormal(hex, pos, pos + size - 1)

	def getHexBytesNormal(hex, startPos, endPos):
		"""Возвращает байты в виде HEX из HEX строки по номеру позиции начальной и конечной"""
		outStr = ""

		for i in range(startPos, endPos + 1):
			outStr += Byte.getHexByte(hex, i)
		return outStr

	def getHexBytesReverse(hex, startPos, endPos):
		"""Возвращает байты в виде HEX из HEX строки по номеру позиции начальной и конечной обратный порядок байт"""
		outStr = ""
		for i in range(endPos, startPos - 1, -1):
			outStr += Byte.getHexByte(hex, i)
	
		return outStr

	def hexToDec(hex):
		"""Преобразует HEX в INT"""
		return int(hex, base=16)

	def decToHex(dec):
		"""Преобразует INT в HEX"""
		return dec.hex()
