class Scene_Control:
	"""Управления отображаемыми сценами"""

	def __init__(self):
		self.scenes_list = {}
		self.selected = ""
		self.prev = ""

	def set(self, name:str) -> None:
		"""Установка сцены по имени"""
		if not (name in self.scenes_list):
			print(f"[ERROR][SCENE] Scene {self.selected} not defined in scenes list") 
		else:
			self.prev = self.selected

			if self.prev:
				self.scenes_list[self.prev].remove()

			self.selected = name
			self.scenes_list[self.selected].select()

	def add(self, name:str, scene:object) -> None:
		"""Добавление сцены"""
		self.scenes_list[name] = scene

	def add_from_dict(self, scenes:dict) -> None:
		"""Импорт сцен из словаря"""
		for scene in scenes:
			self.add(scene, scenes[scene])

	def play(self) -> None:
		"""Воспроизведение сцены"""
		if not self.selected:
			print("[ERROR][SCENE] Scene dont set")
		else:
			self.scenes_list[self.selected].play()

	def remove(self, name:str) -> None:
		"""Удаление сцены из списка"""
		self.scenes_list.pop(name)

	def remove_all(self) -> None:
		"""Удаление всех сцен из списка"""
		for scene in self.scenes_list:
			self.remove(scene)

class Scene:
	"""Экземпляр сцены"""
	
	def __init__(self, **kwargs):
		self.__dict__ = kwargs

	def remove(self):
		...

	def play(self):
		...

	def select(self):
		...