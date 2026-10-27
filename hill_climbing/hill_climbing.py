import random

class Environment:
    def __init__(self, n):
        self.n = n

        self.board = [random.randint(0, n - 1) for _ in range(n)]


class HillClimbingAgent:
    def __init__(self, environment):
        self.environment = environment
        self.n = environment.n

        self.board = environment.board

        print("Initial Board:")
        self.printBoard()

        while True:
            currentHeuristic = self.heuristic(self.board)

            if currentHeuristic == 0:
                print("Solution Found!")
                break

            bestBoard = self.board.copy()
            bestHeuristic = currentHeuristic

            for col in range(self.n):
                for row in range(self.n):
                    if row != self.board[col]:
                        newBoard = self.board.copy()
                        newBoard[col] = row

                        h = self.heuristic(newBoard)

                        if h < bestHeuristic:
                            bestHeuristic = h
                            bestBoard = newBoard

            if bestHeuristic >= currentHeuristic:
                print("Local maximum reached. No solution found.")
                break

            self.board = bestBoard

        print("\nFinal Board:")
        self.printBoard()
        print("Heuristic:", self.heuristic(self.board))

    def heuristic(self, board):
        conflicts = 0

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if board[i] == board[j] or \
                   abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1

        return conflicts

    # Display the board
    def printBoard(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.board[col] == row:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()



n = int(input("Enter the number of queens: "))

theEnvironment = Environment(n)
theAgent = HillClimbingAgent(theEnvironment)
