board = [' ']*9

def print_board():
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def winner(p):
    win_pos = [(0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in win_pos)

def minimax(is_max):
    if winner('O'): return 1
    if winner('X'): return -1
    if ' ' not in board: return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = max(best, minimax(False))
                board[i] = ' '
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = min(best, minimax(True))
                board[i] = ' '
        return best

def best_move():
    best_val = -100
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            value = minimax(False)
            board[i] = ' '
            if value > best_val:
                best_val = value
                move = i
    return move

def play():
    while True:
        print_board()
        pos = int(input("Player X enter position (1-9): ")) - 1
        board[pos] = 'X'

        if winner('X'):
            print_board()
            print("Player X wins!")
            return

        if ' ' not in board:
            print("Draw!")
            return

        board[best_move()] = 'O'

        if winner('O'):
            print_board()
            print("Computer (O) wins!")
            return

play()
