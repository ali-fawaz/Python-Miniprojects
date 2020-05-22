import random
import itertools

def dilemma_round(history, score_a, score_b, strategy_a, strategy_b, sim=False):
    move_a = strategy_a(history, 0)
    move_b = strategy_b(history, 1)

    if move_a == move_b:
        if move_a == 'coop':
            score_a += 2
            score_b += 2
        elif move_a == 'betray':
            score_a -= 1
            score_b -= 1
        else:
            print('error')
    else:
        if move_a == 'coop' and move_b == 'betray':
            score_a -= 2
            score_b += 3
        elif move_a == 'betray' and move_b == 'coop':
            score_a += 3
            score_b -= 2
        else:
            print('error')

    if sim == True:
        print(f'Player A: ' + move_a)
        print(f'Player B: ' + move_b)
        print(f'Scores: A: ' + str(score_a) + ', B:' + str(score_b))

    history.append((move_a, move_b))
    return history, score_a, score_b


def random_move(history, player):
    choice = random.randint(1, 2)
    if choice == 1:
        return 'coop'
    else:
        return 'betray'


def user_move(history, player):
    has_chosen = False
    while not has_chosen:
        print('Type coop or betray')
        user_move = input()
        if user_move in {'coop', 'betray'}:
            return user_move
        else:
            print('Not a valid  move')


def dilemma_game(strategy_a, strategy_b, num_rounds, sim=False, print_scores=True):
    history = []
    score_a, score_b = 0,  0

    for i in range(num_rounds):
        history, score_a, score_b = dilemma_round(history, score_a, score_b, strategy_a, strategy_b, sim)
    
    if print_scores:
        print(f'{strategy_a.__name__}: ' + str(score_a) + f', {strategy_b.__name__}: ' + str(score_b))

    return score_a, score_b


def always_cooperate(history, player):
    return 'coop'


def always_betray(history, player):
    return 'betray'


def mirror_opponent_first_move(first_move, history, player):
    if not history:
        return first_move(history, player)
    else:
        if player == 0:
            opponent = 1
        else:
            opponent = 0

        last_opponent_move = history[-1][opponent]

        return last_opponent_move


def mirror_opponent_random(history, player):
    return mirror_opponent_first_move(random_move, history, player)


def mirror_opponent_coop(history, player):
    # tit for tat
    return mirror_opponent_first_move(always_cooperate, history, player)


def mirror_opponent_betray(history, player):
    return mirror_opponent_first_move(always_betray, history, player)


def historical_majority(history, player):
    if player == 0:
        opponent = 1
    else:
        opponent = 0
    
    if not history:
        return 'coop'
    else:
        coops, betrays = 0, 0

        for play in history:
            if play[opponent] == 'coop':
                coops += 1
            else:
                betrays += 1
        
        if coops > betrays:
            return 'coop'
        elif coops < betrays:
            return 'betray'
        else:
            return 'coop'


def probing(history, player):
    if player == 0:
        opponent = 1
    else:
        opponent = 0
    
    if not history:
        return 'betray'
    elif len(history) == 1:
        return 'coop'
    elif len(history) == 2:
        return 'coop'
    else:
        if (history[1][opponent] == 'coop') and (history[2][opponent] == 'coop'):
            return 'betray'
        else:
            return 'coop'

# https://medium.com/thinking-is-hard/a-prisoners-dilemma-cheat-sheet-4d85fe289d87

strategies = [random_move, always_cooperate, always_betray,
              mirror_opponent_random, mirror_opponent_coop,
              mirror_opponent_betray, historical_majority,
              probing]

scores = {}
for strategy in strategies:
    scores[strategy.__name__] = 0

num_rounds = 1000
for pair in itertools.combinations_with_replacement(strategies, 2):
    score_a, score_b = dilemma_game(pair[0], pair[1], num_rounds, print_scores=True)

    scores[pair[0].__name__] += score_a
    scores[pair[1].__name__] += score_b

print(scores)