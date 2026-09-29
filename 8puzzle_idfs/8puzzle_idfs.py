def goal_test(state, goal):
    return state == goal


def get_moves(state):
    moves = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    if row > 0:
        moves.append(-3) # Up
    if row < 2:
        moves.append(3) # Down
    if col > 0:
        moves.append(-1) # Left
    if col < 2:
        moves.append(1) # Right

    return moves


def make_child(state, move):
    child = list(state)
    zero = child.index(0)
    new_pos = zero + move

    child[zero], child[new_pos] = child[new_pos], child[zero]

    return tuple(child)


def recursive_dls(state, goal, limit, path):

    if goal_test(state, goal):
        return path

    if limit == 0:
        return "cutoff"

    cutoff_occurred = False

    for move in get_moves(state):

        child = make_child(state, move)

        if child in path:
            continue

        result = recursive_dls(
            child, goal, limit - 1, path + [child]
        )

        if result == "cutoff":
            cutoff_occurred = True

        elif result != "failure":
            return result

    if cutoff_occurred:
        return "cutoff"
    else:
        return "failure"


def idfs(initial_state, goal):

    limit = 0

    while True:

        result = recursive_dls(
            initial_state, goal, limit, [initial_state]
        )

        if result != "cutoff":
            return result

        limit += 1


print("Enter the initial state:")
print("Enter 0 for the blank space")
initial_state = tuple(map(int, input().split()))

print("\nEnter the goal state:")
print("Enter 0 for the blank space")
goal = tuple(map(int, input().split()))

solution = idfs(initial_state, goal)

if solution == "failure":
    print("\nNo solution found")
else:
    print("\nSolution path:")

    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
