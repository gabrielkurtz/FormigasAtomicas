
class Edge:

	def __init__(self, origin, destination, cost):
		self.origin = origin
		self.destination = destination
		self.cost = cost
		self.pheromone = None

	def obterOrigem(self):
		return self.origin

	def obterDestino(self):
		return self.destination

	def obterCusto(self):
		return self.cost

	def obterFeronomio(self):
		return self.pheromone

	def setFeromonio(self, pheromone):
		self.pheromone = pheromone



class Graph:

	def __init__(self):
		self.edges = {} 
		self.neighbors = {} 
		self.locations = set()


	def addEdge(self, origin, destination, cost):
		edge = Edge(origin=origin, destination=destination, cost=cost)
		self.locations.update([ origin, destination ])
		self.edges[(origin, destination)] = edge
		if origin not in self.neighbors:
			self.neighbors[origin] = [destination]
		else:
			self.neighbors[origin].append(destination)

	def getLocationsList(self):
		return list ( self.locations )

	def getCostEdge(self, origin, destination):
		return self.edges[(origin, destination)].cost

	def getPheromoneEdge(self, origin, destination):
		return self.edges[(origin, destination)].pheromone

	def setPheromoneEdge(self, origin, destination, pheromone):
		self.edges[(origin, destination)].pheromone = pheromone

	def getPathCost(self, path, finish = False):
		cost = 0
		for i in range(len ( path ) - 1):
			cost += self.getCostEdge(path[i], path[i+1])
		if finish:
			cost += self.getCostEdge(path[-1], path[0])
		return cost
