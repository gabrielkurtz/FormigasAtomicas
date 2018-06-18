import csv
from graph import Graph
from ant_colony_optimization import Ant_Colony_Optimization

FILENAME = "./graph10.csv"

if __name__ == "__main__":
	graph = Graph()

	# with open( FILENAME , "r") as theFile:
	# 	reader = csv.DictReader(theFile)
	# 	for line in reader:
	# 		graph.addEdge(int(line['origin']), int(line['destination']), int(line['value']))
	# d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}

	# GEREADO A MAO 2
	graph.addEdge(1,2,3)
	graph.addEdge(2,4,3)
	graph.addEdge(2,5,2)
	graph.addEdge(4,5,3)
	graph.addEdge(4,6,2)
	graph.addEdge(5,2,2)
	graph.addEdge(5,6,3)
	graph.addEdge(6,1,3)


	# GERADO A MAO 1
	# graph.addEdge(d['B'], d['A'], 42)
	# graph.addEdge(d['A'], d['B'], 42)
	# graph.addEdge(d['C'], d['A'], 61)
	# graph.addEdge(d['A'], d['C'], 61)
	# graph.addEdge(d['C'], d['B'], 14)
	# graph.addEdge(d['B'], d['C'], 14)
	# graph.addEdge(d['D'], d['A'], 30)
	# graph.addEdge(d['A'], d['D'], 30)
	# graph.addEdge(d['D'], d['B'], 87)
	# graph.addEdge(d['B'], d['D'], 87)
	# graph.addEdge(d['D'], d['C'], 20)
	# graph.addEdge(d['C'], d['D'], 20)
	# graph.addEdge(d['E'], d['A'], 17)
	# graph.addEdge(d['A'], d['E'], 17)
	# graph.addEdge(d['E'], d['B'], 28)
	# graph.addEdge(d['B'], d['E'], 28)
	# graph.addEdge(d['E'], d['C'], 81)
	# graph.addEdge(d['C'], d['E'], 81)
	# graph.addEdge(d['E'], d['D'], 34)
	# graph.addEdge(d['D'], d['E'], 34)
	# graph.addEdge(d['F'], d['A'], 82)
	# graph.addEdge(d['A'], d['F'], 82)
	# graph.addEdge(d['F'], d['B'], 70)
	# graph.addEdge(d['B'], d['F'], 70)
	# graph.addEdge(d['F'], d['C'], 21)
	# graph.addEdge(d['C'], d['F'], 21)
	# graph.addEdge(d['F'], d['D'], 33)
	# graph.addEdge(d['D'], d['F'], 33)
	# graph.addEdge(d['F'], d['E'], 41)
	# graph.addEdge(d['E'], d['F'], 41)
	# graph.addEdge(d['G'], d['A'], 31)
	# graph.addEdge(d['A'], d['G'], 31)
	# graph.addEdge(d['G'], d['B'], 19)
	# graph.addEdge(d['B'], d['G'], 19)
	# graph.addEdge(d['G'], d['C'], 8)
	# graph.addEdge(d['C'], d['G'], 8)
	# graph.addEdge(d['G'], d['D'], 91)
	# graph.addEdge(d['D'], d['G'], 91)
	# graph.addEdge(d['G'], d['E'], 34)
	# graph.addEdge(d['E'], d['G'], 34)
	# graph.addEdge(d['G'], d['F'], 19)
	# graph.addEdge(d['F'], d['G'], 19)
	# graph.addEdge(d['H'], d['A'], 11)
	# graph.addEdge(d['A'], d['H'], 11)
	# graph.addEdge(d['H'], d['B'], 33)
	# graph.addEdge(d['B'], d['H'], 33)
	# graph.addEdge(d['H'], d['C'], 29)
	# graph.addEdge(d['C'], d['H'], 29)
	# graph.addEdge(d['H'], d['D'], 10)
	# graph.addEdge(d['D'], d['H'], 10)
	# graph.addEdge(d['H'], d['E'], 82)
	# graph.addEdge(d['E'], d['H'], 82)
	# graph.addEdge(d['H'], d['F'], 32)
	# graph.addEdge(d['F'], d['H'], 32)
	# graph.addEdge(d['H'], d['G'], 59)
	# graph.addEdge(d['G'], d['H'], 59)
	
	ant_colony_optimization = Ant_Colony_Optimization(graph=graph, num_ants = len( graph.locations ), alpha=1.0, beta=5.0, iterations=100, evaporation=0.5)
	
	ant_colony_optimization.run()
	

'''
import csv, random
class GrafoCompleto(Graph):
		# gera um grafo completo
	def gerar(self):
		with open('graphTiny.csv', 'w', newline='') as csvfile:
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