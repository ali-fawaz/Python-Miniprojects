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
    if has_player_won(board, 1) or has_player_won(board, 2):
        return True
    elif 0 not in board:
        return True
    else:
        return False


def choose(strategy, board):
    return strategy(board)

def choose_at_random(board):
    return random.randint(0, 8)


def choose_user(board):
    print('Choose your position')
    return int(input())

def choose_basic(board):
    if board[4] == 0:
        return 4
    else:
        for i in [0, 2, 6, 8]:
            if board[i] == 0:
                return i

        for i in [1, 3, 5, 7]:
            if board[i] == 0:
                return i


def choose_blocking(board):
    opponent = 1

    for i in range(0, 9):
        if board[i] == 0:
            checking_board = board.copy()
            checking_board[i] = opponent
            if has_player_won(checking_board, opponent):
                return i
        
    if board[4] == 0:
        return 4
    else:
        for i in [0, 2, 6, 8]:
            if board[i] == 0:
                return i

        for i in [1, 3, 5, 7]:
            if board[i] == 0:
                return i




def choose_win(board):
    opponent = 1
    player = 2

    for i in range(0, 9):
        if board[i] == 0:
            checking_board = board.copy()
            checking_board[i] = player
            if has_player_won(checking_board, player):
                return i

    for i in range(0, 9):
        if board[i] == 0:
            checking_board = board.copy()
            checking_board[i] = opponent
            if has_player_won(checking_board, opponent):
                return i
        
    if board[4] == 0:
        return 4
    else:
        for i in [0, 2, 6, 8]:
            if board[i] == 0:
                return i

        for i in [1, 3, 5, 7]:
            if board[i] == 0:
                return i


def does_move_fork(board, player, position):
    check_board = board.copy()
    check_board[position] = player

    winning_moves = 0
    for next_position in range(0, 9):
        check_board_possible = check_board.copy()
        check_board_possible[next_position] = player

        if has_player_won(check_board_possible, player) and check_board[next_position] == 0:
            winning_moves += 1
    
    return winning_moves > 1


def choose_fork(board):
    opponent = 1
    player = 2

    for i in range(0, 9):
        if board[i] == 0:
            checking_board = board.copy()
            checking_board[i] = player
            if has_player_won(checking_board, player):
                return i

    for i in range(0, 9):
        if board[i] == 0:
            checking_board = board.copy()
            checking_board[i] = opponent
            if has_player_won(checking_board, opponent):
                return i
        
    for i in range(0, 9):
        if board[i] == 0:
            if does_move_fork(board, opponent, i):
                return i

    for i in range(0, 9):
        if board[i] == 0:
            if does_move_fork(board, player, i):
                return i


    if board[4] == 0:
        return 4
    else:
        for i in [0, 2, 6, 8]:
            if board[i] == 0:
                return i

        for i in [1, 3, 5, 7]:
            if board[i] == 0:
                return i


def xo_game(strategy_x, strategy_y):
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    while not game_ended(board):
        x_has_chosen = False
        while not x_has_chosen:
            position = strategy_x(board)

            if board[position] == 0:
                board[position] = 1
                x_has_chosen = True

        y_has_chosen = False
        while not y_has_chosen:
            if 0 in board:
                position = strategy_y(board)

                if board[position] == 0:
                    board[position] = 2
                    y_has_chosen = True
            else:
                y_has_chosen = True

        
    if has_player_won(board, 1):
        return 1
    elif has_player_won(board, 2):
        return 2
    else:
        return 0


def xo_tournament(strategy_x, strategy_y, num_games):
    score_x = 0
    score_y = 0

    for i in range(num_games):
        result = xo_game(strategy_x, strategy_y)

        if result == 1:
            score_x += 1
        elif result == 2:
            score_y += 1
    
    return score_x, score_y


print(xo_tournament(choose_at_random, choose_basic, 1000))
print(xo_tournament(choose_at_random, choose_blocking, 1000))
print(xo_tournament(choose_at_random, choose_win, 1000))
print(xo_tournament(choose_at_random, choose_fork, 1000))