class Config(dict):
	"""Обработка конфигурационных файлов *.cfg, чтение, запись, автосохранение"""

	def __init__(self, path, autosave=False):
		"""Конструктор\nПринимает: (string) path - путь к cfg файлу, (bool) autosave - автосохранение файла"""
		super().__init__()
		self.path = path
		self.autosave = autosave

	def setSection(self, key, value):
		"""Установить значение всей секции\nПринимает: (string) key - имя секции, (string) value - значение секции"""
		if value == "":
			self.pop(key)
		else:
			self[key] = value

		if self.autosave:
			self.write()

	def setParam(self, section, key, value):
		"""Установить значение в запись секции\nПринимает: (string) section - имя секции, (string) key - ключ, (string) value - значение записи"""
		if value == "":
			self[section].pop(key)
		else:
			self[section][key] = value

		if self.autosave: self.write()

	def read(self):
		"""Чтение файла"""
		file = open(self.path, "r")
		string = file.read()

		strings = string.split("\n")
		
		for s in strings:
			if not(len(s)):
				continue

			if s[0] == "[":
				section = str(s[1:-1])
				self[section] = {}
				lastSection = section

			elif s[0] == ";" or s[0] == "#":
				continue
			
			else:
				data = s.split(" = ")

				for i in range(2, len(data)):
					data[1] += " = " + data[i]

				self[lastSection][data[0]] = data[1]

	def write(self):
		"""Запись в файл"""
		file = open(self.path, "w")
		out = ";AUTO GENERATED, DONT CHANGE IF DONT KNOW"

		for section in self:
			out += f"\n[{section}]"

			for prop in self[section]:
				out += f"\n{prop} = {self[section][prop]}"
			out += "\n"

		file.write(out)
		file.close()