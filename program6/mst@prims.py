# Lab 6:Write a function that return the MST using PRIM's Algorithm #
import sys 
class Graph():

	def __init__(self, sides):
		self.V = sides
		self.graph = [[0 for column in range(sides)]
					for row in range(sides)]
	def printMST(self, base):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(base[i], "-", i, "\t", self.graph[i][base[i]])

	def minKey(self, main, mstSet):
		min = sys.maxsize
		for v in range(self.V):
			if main[v] < min and mstSet[v] == False:
				min = main[v]
				min_index = v

		return min_index
	def primMST(self):
		key = [sys.maxsize] * self.V 
		parent = [None] * self.V 		
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):

				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u
		self.printMST(parent)
#driver code to check prims algorithm
g = Graph(4)
g.graph = 	[[ 1, 2, 0, 6, 0],
			[ 3, 0, 4, 8, 5 ],
			[0, 8, 0, 0, 7 ],
			[ 5, 8, 9, 0, 11] ]
			
g.primMST()