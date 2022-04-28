#Assignment: Tic-Tac-Toe
#Author: Victoria Wrinkle


def main():
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



if __name__ == "__main__":
    main()