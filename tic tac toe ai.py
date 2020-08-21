import time
import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]


def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def is_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
       return True
    else:
        return False


def is_board_full(board):
    if "_" in board:
        return False
    else:
        return True


def get_computer_move(board, player):
    # if the center square is empty chose that
    for i in range(0,8):
        if board[i] == ("_"):
            board[i] = player
            if is_winner(board, player):
                return i
            else:
                board[i] = ("_")
    
    move = random.randint(0,8)
    if board[4] == ("_"):
        return 4
    else:
        while True:
         if board[move] == "_":
            return move
         break
    return 4
            
# player X
while True:
    print_board()
    data_valid = False
    while data_valid == False:
            try:
                choice = input("Please choose an input by typing a number from 1 to 9 for X: ")
                choice = int(choice)-1
            except:
                print("Invalid Input, try again. ")
                continue
            if choice > (10):
                print("Please type a number within the limit which is from 1 to 9")
                continue
            if choice < 0:
                print("invalid input, please try again.")
                continue
            else:
                data_valid = True
                break
    
    if board[choice] == ("_"):
        board[choice] = ("X")
    else:
        print("sorry that place is not empty")
    time.sleep(1)
    # check x winner:
    if is_winner(board, "X"):
        print("X wins.")
        print_board()
        break


 # player O
    choice = get_computer_move(board,  "O")
    if  board[choice] == ("_"):
        board[choice] = ("O")
    else:
        print("sorry that place is not empty")
        


    # if the board is full then......
    if is_board_full(board):
        print("Tie!")
        break

    # check o winner:
    if is_winner(board, "O"):
        print("O wins.")
        print_board()
        break

