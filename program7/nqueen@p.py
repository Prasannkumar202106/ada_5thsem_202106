# Lab-7 program to solve N Queen 
# Problem using backtracking
global N
N = 5
  
def printSolution(field): 
    for i in range(N):
        for j in range(N):
            print(field[i][j], end = " ")
        print() 
  

def isSafe(field, row, col):
  
    # Check this row on left side
    for i in range(col):
        if field[row][i] == 1:
            return False
  
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if field[i][j] == 1:
            return False
  
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), 
                    range(col, -1, -1)):
        if field[i][j] == 1:
            return False
  
    return True
  
def solveNQUtil(field, col):
      
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True
  
    
    for i in range(N):
  
        if isSafe(field, i, col):
              
            # Place this queen in board[i][col]
            field[i][col] = 1
  
            # recur to place rest of the queens
            if solveNQUtil(field, col + 1) == True:
                return True
  
            
            field[i][col] = 0
  
   
    return False
  

def solveNQ():
    field = [ [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0] ]
              
  
    if solveNQUtil(field, 0) == False:
        print ("Solution does not exist")
        return False
  
    printSolution(field)
    return True
  

solveNQ()