import threading
import time

class Scene_Control:
	"""Управления отображаемыми сценами"""

	def __init__(self, update_time=0, frame_time=0.001):
		self.scenes_list = {}
		self.selected = ""
		self.prev = ""
		self.update_time = max(update_time, 0)
		self.frame_time = max(frame_time, 0.001)
		self.enable = False
		self.last_frame_time = 0
		self.last_update_time = 0

	def set(self, name:str):
		"""Установка сцены по имени"""
		if not (name in self.scenes_list):
			print(f"[ERROR][SCENE] Scene {self.selected} not defined in scenes list") 
		else:
			self.prev = self.selected

			if self.prev:
				self.scenes_list[self.prev].remove()

			self.selected = name
			self.scenes_list[self.selected].select()

	def add(self, name:str, scene:object):
		"""Добавление сцены"""
		self.scenes_list[name] = scene

	def add_from_dict(self, scenes:dict):
		"""Импорт сцен из словаря"""
		for scene in scenes:
			self.add(scene, scenes[scene])

	def _draw_(self):
		time.sleep(self.frame_time)
		if not self.selected:
			print("[ERROR][SCENE][DRAW] Scene dont set")
		else:
			self.scenes_list[self.selected].draw()

	def _update_(self):
		time.sleep(self.update_time)
		if not self.selected:
			print("[ERROR][SCENE][UPDATE] Scene dont set")
			self.enable = False
		else:
			self.scenes_list[self.selected].update()

	def play(self):
		"""Начинает воспроизведение сцены"""
		if not self.enable:
			self.enable = True
			while self.enable:

				if not self.update_time or time.time() - self.last_update_time > self.update_time:
					threading.Thread(target=self._update_).start()
					self.last_update_time = time.time()

				if not self.frame_time or time.time() - self.last_frame_time > self.frame_time:
					threading.Thread(target=self._draw_).start()
					self.last_frame_time = time.time()

	def remove(self, name:str):
		"""Удаление сцены из списка"""
		self.scenes_list.pop(name)

	def remove_all(self):
		"""Удаление всех сцен из списка"""
		for scene in self.scenes_list:
			self.remove(scene)

	def stop(self):
		"""Остановка воспроизведения сцены"""
		self.enable = False

class Scene:
	"""Экземпляр сцены"""
	
	def __init__(self, **kwargs):
		self.__dict__ = kwargs

	def start(self):
		"""Выполняется при запуске сцены"""
		...

	def update(self):
		"""Метод для обновления логики прилоежния"""
		...

	def draw(self):
		"""Метод для обновления отрисовки приложения"""
		...

	def remove(self):
		"""Вызывается при смене сцены"""
		...