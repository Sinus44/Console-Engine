from random import random

class Perceptron:
	"""Простой нейрон"""
	def __init__(self, inputs, learningRate=0.1):
		self.input = [0 for i in range(inputs)]
		self.w = [random() for i in range(inputs + 1)]
		self.sum = 0
		self.learningRate = learningRate

	def exp(self, x):
		"""Возвращает экспоненту числа"""
		e = 2.718
		return e ** x

	def derivative(self, x):
		"""Производная функции активации"""
		return x * (1 - x)

	def activation(self, x):
		"""Функция активации"""
		return 1 / (1 + self.exp(-x))

	def predict(self, input):
		"""Предсказывает выхоное значение исходя из входных данных"""
		self.input = input + [1]
		sum = 0
		for i in range(len(self.input)):
			sum += self.input[i] * self.w[i]
		self.sum = sum
		self.out = self.activation(sum)
		return self.out

	def learn(self, input, out):
		"""Обучение нейрона с учителем"""
		y = self.predict(input)
		err = out - y
		for i in range(len(self.w)):
			self.w[i] += (self.learningRate * (err)) * self.input[i]
		return err
    
	def learnNoLearer(self, err):
		"""Обучение нейрона с без учителя"""
		for i in range(len(self.w)):
			self.w[i] += (self.learningRate * (err)) * self.input[i]
		return err