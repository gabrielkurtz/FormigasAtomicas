#coding: utf-8

import csv
from graph import Graph
from ant_colony_optimization import Ant_Colony_Optimization

FILENAME = "./graph10.csv"

if __name__ == "__main__":
	graph = Graph()

	with open( FILENAME , "r") as theFile:
		reader = csv.DictReader(theFile)
		for line in reader:
			graph.addEdge(int(line['origin']), int(line['destination']), int(line['value']))

	# GEREADO A MAO 1
	# graph.addEdge(1,2,3)
	# graph.addEdge(2,4,3)
	# graph.addEdge(2,5,2)
	# graph.addEdge(4,5,3)
	# graph.addEdge(4,6,2)
	# graph.addEdge(5,2,2)
	# graph.addEdge(5,6,3)
	# graph.addEdge(6,1,3)


	length = len( graph.locations )
	ant_colony_optimization = Ant_Colony_Optimization(graph=graph, 
		num_ants = 100 if length > 100 else length , 
		alpha=1.0, 
		beta=5.0, 
		iterations=100 if length < 100 else 5, 
		evaporation=0.5)
	
	ant_colony_optimization.run()
	

'''
import csv, random
class GrafoCompleto(Graph):
		# gera um grafo completo
	def gerar(self):
		with open('graphN.csv', 'w', newline='') as csvfile:
			fieldnames = ['origin', 'destination', 'value']
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			for i in range(1, self.num_vertex + 1):
				for j in range(1, self.num_vertex + 1):
					if i != j:
						peso = random.randint(1, 100)
						writer.writerow({'origin': i, 'destination': j, 'value': peso})
						self.addEdge(i, j, peso)
'''