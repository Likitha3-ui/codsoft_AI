import random
import time

board = [" " for _ in range(9)]

player_score = 0
computer_score = 0


def print_board():

    print("\n")

    for row in range(3):

        start = row * 3

        print(
            f" {board[start]} | {board[start + 1]} | {board[start + 2]} "
        )

        if row < 2:
            print("---|---|---")


def print_positions():

    print("\nBoard Positions\n")

    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")


def check_winner(player):

    winning_combinations = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:

        if (
            board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player
        ):

            return True

    return False


def check_draw():

    return " " not in board


def player_move():

    while True:

        try:

            move = int(
                input("\nEnter your position (1-9): ")
            ) - 1

            if move < 0 or move > 8:
                print("Choose between 1 and 9.")
                continue

            if board[move] != " ":
                print("Position already taken.")
                continue

            board[move] = "X"
            break

        except:
            print("Invalid input.")


def computer_move():

    print("\nComputer is thinking...")
    time.sleep(1)

    available_moves = []

    for index in range(9):

        if board[index] == " ":
            available_moves.append(index)

    move = random.choice(available_moves)

    board[move] = "O"


def reset_board():

    global board

    board = [" " for _ in range(9)]


print("=" * 50)
print("         TIC TAC TOE AI")
print("=" * 50)

print_positions()

while True:

    reset_board()

    while True:

        print_board()

        player_move()

        if check_winner("X"):

            print_board()
            
            print("\n Congratulations! You won.")

            player_score += 1

            break

        if check_draw():

            print_board()

            print("\n Match Draw.")

            break

        computer_move()

        if check_winner("O"):

            print_board()

            print("\n Computer Wins.")

            computer_score += 1

            break

        if check_draw():

            print_board()

            print("\n Match Draw.")

            break

    print("\nScore Board")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":

        print("\nThank you for playing Tic Tac Toe AI.")
        break