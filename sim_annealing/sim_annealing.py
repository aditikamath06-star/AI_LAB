import random
import math

class Environment:
    def __init__(self):
        
        self.board = [random.randint(0, 7) for _ in range(8)]

class SimulatedAnnealingAgent:
    def __init__(self, environment):
        self.board = environment.board

        T = 1000

        while T > 0:
            nextBoard = self.board.copy()

            col = random.randint(0, 7)
            row = random.randint(0, 7)
            nextBoard[col] = row

            
            deltaE = self.cost(self.board) - self.cost(nextBoard)

            
            if deltaE > 0:
                self.board = nextBoard

            
            else:
                p = math.exp(deltaE / T)

                if random.random() < p:
                    self.board = nextBoard

            
            T -= 1

           
            if self.cost(self.board) == 0:
                break

        self.printBoard()

        if self.cost(self.board) == 0:
            print("Solution Found!")
        else:
            print("Solution not found.")

        print("Cost:", self.cost(self.board))
    def cost(self, board):
        conflicts = 0

        for i in range(8):
            for j in range(i + 1, 8):
                if board[i] == board[j] or \
                   abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1

        return conflicts

    def printBoard(self):
        for row in range(8):
            for col in range(8):
                if self.board[col] == row:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()


theEnvironment = Environment()
theAgent = SimulatedAnnealingAgent(theEnvironment)
