class Ant:

	def __init__(self, location):
		self.location = location
		self.answer = []
		self.cost = None

	def obterCidade(self):
		return self.location

	def setCidade(self, location):
		self.location = location

	def obterSolucao(self):
		return self.answer

	def setSolucao(self, answer, cost):
		if not self.cost:
			self.answer = answer[:]
			self.cost = cost
		else:
			if cost < self.cost:
				self.answer = answer[:]
				self.cost = cost

	def obterCustoSolucao(self):
		return self.cost
