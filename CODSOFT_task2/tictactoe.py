import random

# Create board
board = [" " for _ in range(9)]

# Display board
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check if full
def is_full():
    return " " not in board

# Player move
def player_move():
    while True:
        try:
            move = int(input("Enter position (0-8): "))
            if move >= 0 and move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except:
            print("Enter a number between 0 and 8.")

# AI move
def ai_move():
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "

    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Random move
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"

# Game start
print("Tic-Tac-Toe Game")
print("Positions:")
print("0 | 1 | 2")
print("3 | 4 | 5")
print("6 | 7 | 8")

display_board()

while True:
    player_move()
    display_board()

    if check_winner("X"):
        print("You win!")
        break

    if is_full():
        print("It's a draw!")
        break

    ai_move()
    display_board()

    if check_winner("O"):
        print("AI wins!")
        break

    if is_full():
        print("It's a draw!")
        break