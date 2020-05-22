import random


def has_player_won(board, player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False


def game_ended(board):
    print(board)
    if has_player_won(board, 1) or has_player_won(board, 2):
        return True
    elif 0 not in board:
        return True
    else:
        return False


def does_move_win(board, player, position):
    check_board = board.copy()
    check_board[position] = player
    return has_player_won(board, player)


def does_move_fork(board, player, position):
    check_board = board.copy()
    check_board[position] = player

    winning_moves = 0
    for next_position in range(0, 9):
        if does_move_win(check_board, player, next_position) and check_board[next_position] == 0:
            winning_moves += 1
    
    return winning_moves > 1


def choose_move(board):
    # immediate computer win
    for position in range(0, 9):
        if board[position] == 0 and does_move_win(board, 2, position):
            return position
    
    # block immediate player win
    for position in range(0, 9):
        if board[position] == 0 and does_move_win(board, 1, position):
            return position
    
    # computer fork move
    for position in range(0, 9):
        if board[position] == 0 and does_move_fork(board, 2, position):
            return position

    # block player form move
    for position in range(0, 9):
        if board[position] == 0 and does_move_fork(board, 1, position):
            return position

    # pick center
    if board[4] == 0:
        return 4
    
    # pick corner
    for position in [0, 2, 6, 8]:
        if board[position] == 0:
            return position
    
    # pick side
    for position in [0, 2, 6, 8]:
        if board[position] == 0:
            return position


board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while not game_ended(board):
    print('Board:')
    print(str(board[0]) + ' - ' + str(board[1]) + ' - ' + str(board[2]))
    print(str(board[3]) + ' - ' + str(board[4]) + ' - ' + str(board[5]))
    print(str(board[6]) + ' - ' + str(board[7]) + ' - ' + str(board[8]))
    
    has_chosen = False
    while not has_chosen:
        print('Choose your position')
        position = int(input())

        if board[position] == 0:
            board[position] = 1
            has_chosen = True
        else:
            print('That box is full')

    print('Computer is choosing...')
    computer_has_chosen = False
    count = 0
    while not computer_has_chosen:
        if 0 in board:
            position = choose_move(board)

            print(position)

            if board[position] == 0:
                board[position] = 2
                computer_has_chosen = True
        else:
            computer_has_chosen = True


print('Board:')
print(str(board[0]) + ' - ' + str(board[1]) + ' - ' + str(board[2]))
print(str(board[3]) + ' - ' + str(board[4]) + ' - ' + str(board[5]))
print(str(board[6]) + ' - ' + str(board[7]) + ' - ' + str(board[8]))

if has_player_won(board, 1):
    print('You won!')
elif has_player_won(board, 2):
    print('The computer won!')
else:
    print('Tie!')