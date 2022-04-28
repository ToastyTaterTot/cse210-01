#Assignment: Tic-Tac-Toe
#Author: Victoria Wrinkle


def main():
    player = next_player('')
    board = make_board()
    while not (winner(board) or tie(board)):
        show_board(board)
        move(player, board)
        player = next_player(player)
    show_board(board)
    print('Good game. Thanks for playing!')

def make_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board   

def show_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}|')
    print(f'-+-+-')
    print(f'{board[3]}|{board[4]}|{board[5]}|')
    print(f'-+-+-')
    print(f'{board[6]}|{board[7]}|{board[8]}|')
    print(f'-+-+-')

def tie(board):
    for square in range(9):
        if board[square] != 'x' and board[square] != 'o':
            return False
    return True

def winner(board):
    return (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6])

def move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == '' or current == 'o':
        return 'x'
    elif current == 'x':
        return 'o'

if __name__ == "__main__":
    main()