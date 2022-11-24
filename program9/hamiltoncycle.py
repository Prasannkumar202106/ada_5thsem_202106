#LAB-9 write a program for hamilton cycle using backtracking
class Hamiltonian:
    def __init__(self, begin):
        # start
        self.begin = begin
 
        # list to store the cycle path
        self.cycle = []
 
        # variable to mark if graph has the cycle
        self.hasCycle = False
 
    # method to initiate the search of cycle
    def findCycle(self):
        # add starting vertex to the list
        self.cycle.append(self.begin)
 
        # start the search of the hamiltonian cycle
        self.solve(self.begin)
 
    # recursive function to implement backtracking
    def solve(self, sides):
        # Base condition: if the vertex is the start vertex
        # and all nodes have been visited (start vertex twice)
        if sides == self.begin and len(self.cycle) == N + 1:
            self.hasCycle = True
 
            # output the cycle
            self.displayCycle()
 
            # return to explore more cycles
            return
 
        # iterate through the neighbor vertices
        for i in range(len(edges)):
            if adjacencyM[sides][i] == 1 and visited[i] == 0:
                number = i
 # visit and add vertex to the cycle
                visited[number] = 1
                self.cycle.append(number)
 
                # traverse the neighbor vertex to find the cycle
                self.solve(number)
 
                # Backtrack
                visited[number] = 0
                self.cycle.pop()
 
    # function to display the hamiltonian class
    def displayCycle(self):
        names = []
        for v in self.cycle:
            names.append(edges[v])
        print(names)
 
if __name__ == '__main__':
  edges = ['A', 'B', 'C', 'D', 'E']
  adjacencyM = [[0, 1, 0, 1, 0], 
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1,], 
                [1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0], ]
 
  #list mapping of vertices to mark vertex visited
  visited = [0 for x in range(len(edges))]
 
  #number of vertices in the graph
  N = 5
 
  #Driver code
  hamiltonian = Hamiltonian(0)
  hamiltonian.findCycle()
 
  #if the graph doesn't have any Hamiltonian Cycle
  if not hamiltonian.hasCycle:
    print("No Hamiltonian Cycle")
    