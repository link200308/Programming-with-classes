'''
Author: William Hartfield
Tic-Tac-Toe
'''
def main():
    player = next_player("")
    board = make_board()
    while not (winner(board) or game_draw(board)):
        display_board(board)
        move(player, board)
        player = next_player(player)
    display_board(board)
    print("Great game. Thanks for playing! Please play again!") 

# Creates the playing board.
def make_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

# Displays the board 
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def game_draw(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True 
    
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def move(player, board):
    square = int(input(f"{player}'s turn to choose a spot (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"

if __name__ == "__main__":
    main()