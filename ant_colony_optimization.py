import random, math
from graph import Graph
from ant import Ant

class Ant_Colony_Optimization:
	
	def __init__(self, graph, num_ants, alpha=1.0, beta=5.0, 
						iterations=10, evaporation=0.5):
		self.graph = graph
		self.locationsLength = len( graph.locations )
		self.num_ants = num_ants
		self.alpha = alpha # importância do feromônio
		self.beta = beta # importância da informação heurística
		self.iterations = iterations # quantidade de iterações
		self.evaporation = evaporation # taxa de evaporação
		self.ants = [] # lista de ants

		locations = self.graph.getLocationsList()
		# cria as ants colocando cada uma em uma location diferente
		for k in range(self.num_ants):
			location_ant = random.choice(locations)
			locations.remove(location_ant)
			self.ants.append(Ant(location=location_ant))
			if not locations:
				locations = [location for location in range(1, self.locationsLength + 1)]
		
		# reestrutura location como set
		locations = self.graph.locations

		# calcula o cost guloso pra usar na inicialização do feromônio
		# cost = 0.0 # cost guloso
		# initial_vertex = random.randint(1, locationsLength) # seleciona um vértice aleatório
		# current_vertex = initial_vertex
		# visited = [current_vertex] # lista de visited
		# while True:
		# 	neighbors = self.graph.neighbors[current_vertex][:]
		# 	costs, chosen = [], {}
		# 	for neighbor in neighbors:
		# 		if neighbor not in visited:
		# 			cost = self.graph.obterCustoEdge(current_vertex, neighbor)
		# 			chosen[cost] = neighbor
		# 			costs.append(cost)
		# 	if len(visited) == self.locationsLength:
		# 		break
		# 	min_cost = min(costs) # pega o menor cost da lista
		# 	cost += min_cost # adiciona o cost ao total
		# 	current_vertex = chosen[min_cost] # atualiza o vértice corrente
		# 	visited.append(current_vertex) # marca o vértice corrente como visitado

		# # adiciona o cost do último visitado ao cost
		# cost += self.graph.obterCustoEdge(visited[-1], initial_vertex)
		# cost = 0.0;
		# inicializa o feromônio de todas as edges
		for key_edge in self.graph.edges:
			# pheromone = 1.0 / (self.locationsLength * cost)
			self.graph.setFeromonioEdge(key_edge[0], key_edge[1], 0.0)

	def run(self):

		for it in range(self.iterations):
			for k in range(self.num_ants):
				# adiciona a location de origin de cada ant
				locations = [ self.ants[k].location ]

			# para cada ant constrói  solução
			for k in range(self.num_ants):
				# lista de listas com as locations visitadas por cada ant
				visited = []
				startLocation = self.ants[k].location
				visited.append(startLocation)

				for i in range(1, self.locationsLength ):
					
					location = None

					# obtém todos os neighbors que não foram visited
					a = set(self.graph.neighbors[self.ants[k].location ])
					b = set(visited[k])
					not_visited = list( a - b )
					
					# somatório do conjunto de locations não visitadas pela ant "k"
					# servirá para utilizar no cálculo da probability
					sum = 0.0
					for location in not_visited:
						# calcula o feromônio
						pheromone =  self.graph.obterFeromonioEdge(self.ants[k].location , location)
						# obtém a distância
						distance = self.graph.obterCustoEdge(self.ants[k].location , location)
						# adiciona no somatório
						sum += (math.pow(pheromone, self.alpha) * math.pow(1.0 / distance, self.beta))

					# probabilities de escolher um path
					probabilities = {}

					for location in not_visited:
						# calcula o feromônio
						pheromone = self.graph.obterFeromonioEdge(self.ants[k].location , location)
						# obtém a distância
						distance = self.graph.obterCustoEdge(self.ants[k].location , location)
						# obtém a probability
						probability = (math.pow(pheromone, self.alpha) * math.pow(1.0 / distance, self.beta)) / (sum if sum > 0 else 1)
						# adiciona na lista de probabilities
						probabilities[location] = probability

					# obtém a location escolhida
					chosen = max(probabilities, key=probabilities.get)

					# adiciona a location escolhida a lista de locations visitadas pela ant "k"
					visited[k].append(chosen)

				# atualiza a solução encontrada pela ant
				if startLocation in self.graph.neighbors[ location ]:
					self.ants[k].setSolucao(visited[k], self.graph.obterCustoCaminho(visited[k]))

			# atualiza quantidade de feromônio
			for edge in self.graph.edges:
				# somatório dos feromônios da edge
				sum_pheromone = 0.0
				# para cada ant "k"
				for k in range(self.num_ants):
					edges_ant = []
					# gera todas as edges percorridas da ant "k"
					for j in range(self.locationsLength - 1):
						edges_ant.append((visited[k][j], visited[k][j+1]))
					# adiciona a última edge
					edges_ant.append((visited[k][-1], visited[k][0]))
					# verifica se a edge faz parte do path da ant "k"
					if edge in edges_ant:
						sum_pheromone += (1.0 / self.graph.obterCustoCaminho(visited[k]))
				# calcula o new feromônio
				new_pheromone = (1.0 - self.evaporation) * self.graph.obterFeromonioEdge(edge[0], edge[1]) + sum_pheromone
				# seta o new feromônio da edge
				self.graph.setFeromonioEdge(edge[0], edge[1], new_pheromone)


		# percorre para obter as soluções das ants
		answer, cost = None, None
		for k in range(self.num_ants):
			if not answer:
				answer = self.ants[k].obterSolucao()[:]
				cost = self.ants[k].obterCustoSolucao()
			else:
				aux_cost = self.ants[k].obterCustoSolucao()
				if aux_cost < cost:
					answer = self.ants[k].obterSolucao()[:]
					cost = aux_cost
		print('Solução final: %s | cost: %d\n' % (' -> '.join(str(i) for i in answer), cost))
