board = [' ']*9

def show():
    print()
    print(board[0],'|',board[1],'|',board[2])
    print('--+---+--')
    print(board[3],'|',board[4],'|',board[5])
    print('--+---+--')
    print(board[6],'|',board[7],'|',board[8])
    print()

def win(p):
    return ((board[0]==board[1]==board[2]==p) or
            (board[3]==board[4]==board[5]==p) or
            (board[6]==board[7]==board[8]==p) or
            (board[0]==board[3]==board[6]==p) or
            (board[1]==board[4]==board[7]==p) or
            (board[2]==board[5]==board[8]==p) or
            (board[0]==board[4]==board[8]==p) or
            (board[2]==board[4]==board[6]==p))

def play():
    player = 'X'
    for _ in range(9):
        show()
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
        if board[pos] == ' ':
            board[pos] = player
            if win(player):
                show()
                print("Player", player, "wins!")
                return
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move")
    show()
    print("Game Draw")

play()
