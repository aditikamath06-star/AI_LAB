import random

a = [[" ", " ", " "],
     [" ", " ", " "],
     [" ", " ", " "]]

user = input("Choose X or O: ").upper()
while user not in ["X", "O"]:
    user = input("Invalid choice. Choose X or O: ").upper()

computer = "O" if user == "X" else "X"

def display():
    print()
    print(a[0][0], "|", a[0][1], "|", a[0][2])
    print("--+---+--")
    print(a[1][0], "|", a[1][1], "|", a[1][2])
    print("--+---+--")
    print(a[2][0], "|", a[2][1], "|", a[2][2])
    print()

def win(symbol):
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2] == symbol:
            return True
        if a[0][i] == a[1][i] == a[2][i] == symbol:
            return True
    if a[0][0] == a[1][1] == a[2][2] == symbol:
        return True
    if a[0][2] == a[1][1] == a[2][0] == symbol:
        return True
    return False

def is_full():
    for row in a:
        if " " in row:
            return False
    return True

# Display board at startup so the user sees it immediately
display()

while True:
    try:
        position = int(input("Enter position (1-9): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    # Bounds check BEFORE indexing the list
    if position < 1 or position > 9:
        print("Invalid position! Pick between 1 and 9.")
        continue

    row = (position - 1) // 3
    column = (position - 1) % 3

    if a[row][column] != " ":
        print("Position already taken! Choose another.")
        continue

    a[row][column] = user
    display()

    if win(user):
        print(user, "wins!")
        break

    if is_full():
        print("DRAW")
        break

    # Computer Move
    while True:
        computer_position = random.randint(1, 9)
        r = (computer_position - 1) // 3
        c = (computer_position - 1) % 3
        if a[r][c] == " ":
            a[r][c] = computer
            break

    print("Computer chose:", computer_position)
    display()

    if win(computer):
        print(computer, "wins!")
        break

    if is_full():
        print("DRAW")
        break