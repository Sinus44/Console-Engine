class Scene:
	"""Управления отображаемыми сценами"""

	list = {}
	selected = ""
	prev = ""

	def set(name):
		"""Установка сцены по имени\nПринимает: (string) name - имя сцены"""
		Scene.prev = Scene.selected
		Scene.selected = name

	def add(name, scene):
		"""Добавление сцены\nПринимает: (string) name - имя сцены, (Scene) scene - сцена"""
		Scene.list[name] = scene

	def addFromDict(scenes):
		"""Импорт сцен из объекта формата { name:scene }\nПринимает: (array_dict_name_scene) scenes - массив сцен для добавления"""
		for scene in scenes:
			Scene.add(scene, scenes[scene])

	def play():
		"""Воспроизведение сцены"""
		Scene.list[Scene.selected].play()