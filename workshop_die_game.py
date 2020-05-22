import random

user_score = 0
computer_score = 0

while user_score < 5 and computer_score < 5:
    print('Press any key to throw the die')
    input()

    user_die = random.randint(1, 6)
    computer_die = random.randint(1, 6)

    print('Your die throw was:')
    print(user_die)

    print('The computer die throw was:')
    print(computer_die)

    if user_die < computer_die:
        print('The computer won!')
        computer_score = computer_score + 1
    elif user_die > computer_die:
        print('You won!')
        user_score = user_score + 1
    else:
        print('You and the computer tied!')
    
    print('Your current score is:')
    print(user_score)

    print('The computer score is:')
    print(computer_score)

if user_score > computer_score:
    print('You won!')
else:
    print('The computer won!')