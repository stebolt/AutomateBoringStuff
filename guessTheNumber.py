# This is a guess the number game
import random
secretNumber = random.randint(1, 20)
print ('What\'s my secret number? It\'s between 1 and 20')
for guessesTaken in range(1, 7):
    print ('Take a guess...')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good work! you guessed the secret number ' + str(secretNumber) + ' in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope, i was thinking of ' + str(secretNumber) + '.')