import random, math
from graph import Graph
from ant import Ant
from plot import plot
import matplotlib.pyplot as plt
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

		for key_edge in self.graph.edges:
			# pheromone = 1.0 / (self.locationsLength * cost)
			self.graph.setPherormoneEdge(key_edge[0], key_edge[1], 0.1)

	def run(self):
		''' Executa algoritmo de colônia de formigas '''

		''' Adiciona a posição inicial como visitada '''
		for it in range(self.iterations):
			visited = []
			for k in range(self.num_ants):
				startLocation = self.ants[k].location
				visited.append([startLocation])

			# Constroi uma solução para cada formiga
			for k in range(self.num_ants):

				location = None
				startLocation = self.ants[k].location
				
				for i in range(0, self.locationsLength ):
					'''
					caso a formiga não esteja em nenhuma posição
						ou
					posição não tenha vizinhos / para onde ir

					quebra iteração, não há solução ...
					'''
					if self.ants[k].location == None or self.ants[k].location not in self.graph.neighbors:
						break
					
					# operação entre conjuntos para obter os não visitados
					a = set(self.graph.neighbors[self.ants[k].location ])
					b = set(visited[k])
					not_visited = list( a - b )
					
					'''
					se todos já foram visitados e não há mais para onde ir
					quebra iteração, não há solução ...
					'''
					if(len (not_visited) == 0 ):
						break
					# somatório do conjunto de locations não visitadas pela formiga "k"
					# servirá para utilizar no cálculo da probabilidade
					sum = 0.0
					for location in not_visited:
						# calcula o feromônio
						pheromone =  self.graph.getPherormeneEdge(self.ants[k].location , location)
						# obtém a distância
						distance = self.graph.getCostEdge(self.ants[k].location , location)
						# adiciona no somatório
						sum += (math.pow(pheromone, self.alpha) * math.pow(1.0 / distance, self.beta))

					# probabilidades de escolher um caminho
					probabilities = {}

					for location in not_visited:
						# calcula o feromônio
						pheromone = self.graph.getPherormeneEdge(self.ants[k].location , location) # self.graph.egdes[(self.ants[k].location, location)].pherormone
						# obtém a distância
						distance = self.graph.getCostEdge(self.ants[k].location , location)
						# obtém a probability
						probability = (math.pow(pheromone, self.alpha) * math.pow(1.0 / distance, self.beta)) / (sum if sum > 0 else 1)
						'''
						adiciona na lista de probabilities
						é multiplicado por um fator randomico para possibilitar a mutação
						tendo em vista a distribuição sendo aleatória o caminho com maior probabilidade ainda é priorizado
						'''
						probabilities[location] = random.uniform(0, 1) * probability

					# obtém a 'location' escolhida
					
					chosen = max(probabilities, key=probabilities.get)

					'''
					adiciona a location escolhida a lista de locations visitadas pela ant "k"
					se 'movimenta' até a posição escolhida
					'''
					self.ants[k].location = chosen
					visited[k].append(chosen)

				'''
				atualiza a solução encontrada pela ant
				se houverem locações
				se houver ligação entre a posição inicial do grafo e a localização final
				e se todas as edges foram visitadas

				adiciona ao custo calculado a ultima ligação entre o primeiro o ultimo nodo
				'''
				if location != None and location in self.graph.neighbors and startLocation in self.graph.neighbors[ location ] and len( visited[k] ) == len ( self.graph.locations ):
					self.ants[k].setSolucao(visited[k], self.graph.getPathCost(visited[k],  finish = True))

			# atualiza quantidade de feromônio
			for edge in self.graph.edges:
				# somatório dos feromônios da edge
				sum_pheromone = 0.0
				# para cada ant "k"
				for k in range(self.num_ants):
					# Formiga Não chegou a achar solução
					if len( self.ants[k].answer ) == 0:
						continue
					edges_ant = []
					# gera todas as edges percorridas da ant "k"
					for j in range(len ( visited[k] ) - 1):
						edges_ant.append((visited[k][j], visited[k][j+1]))
					# adiciona a última edge
					edges_ant.append((visited[k][-1], visited[k][0]))
					# verifica se a edge faz parte do path da ant "k"
					if edge in edges_ant:
						sum_pheromone += (1.0 / self.graph.getPathCost(visited[k]))
				# calcula o novo ferormonio
				new_pheromone = (1.0 - self.evaporation) * self.graph.getPherormeneEdge(edge[0], edge[1]) + sum_pheromone
				# seta o novo feromônio da edge
				self.graph.setPherormoneEdge(edge[0], edge[1], new_pheromone)


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
		if answer == None or len( answer ) == 0:
			print("Nenhuma solução encontrada")
		else:
			print('Solução final: %s | cost: %d\n' % (' >> '.join(str(i) for i in answer) , cost))
			plot( answer )
