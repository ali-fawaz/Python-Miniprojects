import random

target = random.randint(1, 10)

score = 0
guessed = False

while not guessed:
    print('Enter your guess.')
    user_guess = int(input())

    score = score + 1

    if user_guess == target:
        print('You guessed it correctly!')
        guessed = True
    elif user_guess < target:
        print('Guess higher!')
    else:
        print('Guess lower!')

print('Your score was:')
print(score)
