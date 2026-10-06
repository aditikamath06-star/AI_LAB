class Environment:
    def __init__(self):

        print("Enter Initial State (9 numbers, use 0 for blank):")
        self.initialState = list(map(int, input().split()))

        print("Enter Goal State (9 numbers, use 0 for blank):")
        self.goalState = list(map(int, input().split()))


class AStarAgent:
    def __init__(self, environment, heuristic):

        self.environment = environment
        self.heuristic = heuristic

        print("Initial State:")
        self.printState(environment.initialState)

        self.aStar()

    def aStar(self):

        initial = self.environment.initialState
        goal = self.environment.goalState

        openList = []

        g = 0
        h = self.calculateHeuristic(initial)
        f = g + h

        openList.append((f, g, initial, [initial]))

        visited = set()

        while openList:


            openList.sort(key=lambda x: x[0])

            f, g, state, path = openList.pop(0)

            stateTuple = tuple(state)

            if stateTuple in visited:
                continue

            visited.add(stateTuple)

            if state == goal:

                print("Goal State Reached!")
                print("Cost:", g)

                print("\nSolution Path:")

                for s in path:
                    self.printState(s)

                return

            blankPosition = state.index(0)

            row = blankPosition // 3
            col = blankPosition % 3

            moves = [
                (-1, 0), # Up
                (1, 0), # Down
                (0, -1), # Left
                (0, 1) # Right
            ]

            # Generate successors
            for dr, dc in moves:

                newRow = row + dr
                newCol = col + dc

               
                if 0 <= newRow < 3 and 0 <= newCol < 3:

                    newPosition = newRow * 3 + newCol

                    newState = state.copy()

                    newState[blankPosition], newState[newPosition] = \
                        newState[newPosition], newState[blankPosition]

                    newStateTuple = tuple(newState)

                    if newStateTuple not in visited:

                        newG = g + 1
                        newH = self.calculateHeuristic(newState)
                        newF = newG + newH

                        newPath = path + [newState]

                        openList.append(
                            (newF, newG, newState, newPath)
                        )

        print("No solution found.")

    # Calculate heuristic
    def calculateHeuristic(self, state):

        # Case 1: Number of Misplaced Tiles
        if self.heuristic == 1:

            count = 0

            for i in range(9):

                if state[i] != 0 and \
                   state[i] != self.environment.goalState[i]:
                    count += 1

            return count

        # Case 2: Manhattan Distance
        elif self.heuristic == 2:

            distance = 0

            for i in range(9):

                if state[i] != 0:

                    currentRow = i // 3
                    currentCol = i % 3

                    goalPosition = \
                        self.environment.goalState.index(state[i])

                    goalRow = goalPosition // 3
                    goalCol = goalPosition % 3

                    distance += abs(currentRow - goalRow) + \
                                abs(currentCol - goalCol)

            return distance

        return 0

    def printState(self, state):

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()


# Create Environment
theEnvironment = Environment()

# Case 1: Misplaced Tiles
print("\n===== A* using Misplaced Tiles =====")
theAgent1 = AStarAgent(theEnvironment, 1)

# Case 2: Manhattan Distance
print("\n===== A* using Manhattan Distance =====")
theAgent2 = AStarAgent(theEnvironment, 2)