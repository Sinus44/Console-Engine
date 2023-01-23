from random import random

class Perceptron:
	"""Простой нейрон"""
	def __init__(self, inputs, learningRate=0.1):
		"""Конструктор\nПринимает: (int) inputs - кол-во входных нейронов, (float) learningRate - скорость обучения"""
		self.input = [0 for i in range(inputs)]
		self.w = [random() for i in range(inputs + 1)]
		self.sum = 0
		self.learningRate = learningRate

	def exp(self, x):
		"""Экспонента числа\nПринимает: (float) x - число\nВозвращает: (float) - экспонента числа"""
		e = 2.718
		return e ** x

	def derivative(self, x):
		"""Производная функции активации\nПринимает: (float) x - число\nВозвращает: (float) - производная функии активации"""
		return x * (1 - x)

	def activation(self, x):
		"""Функция активации\nПринимает: (float) x - число\nВозвращает: (float) - функия активации"""
		return 1 / (1 + self.exp(-x))

	def predict(self, input):
		"""Предсказывает выхоное значение исходя из входных данных\nПринимает: (array_float) input - массив входных данных"""
		self.input = input + [1]
		sum = 0
		for i in range(len(self.input)):
			sum += self.input[i] * self.w[i]
		self.sum = sum
		self.out = self.activation(sum)
		return self.out

	def learn(self, input, out):
		"""Обучение нейрона с учителем\nПринимает: (array_float) input - массив входных данных, (float) out - ожидаемое выходное значение\nВозвращает: (float) - ошибка между ожидаемым и фактическим результатом"""
		y = self.predict(input)
		err = out - y
		for i in range(len(self.w)):
			self.w[i] += (self.learningRate * (err)) * self.input[i]
		return err
    
	def learnNoLearer(self, err):
		"""Обучение нейрона с без учителя\nПринимает: (float) err - ошибка нейрона"""
		if err == 0: return
		for i in range(len(self.w)):
			self.w[i] += (self.learningRate * (err)) * self.input[i]