import random, sys
print ('ROCK, PAPER, SCISSORS')
wins = 0
draws = 0
losses = 0

while True:
    print ('%s Wins, %s Losses, %s Draws' % (wins, losses, draws))
    while True:
        print ('Enter your move (r)ock (p)aper (s)cissors (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print ('type one of r, p, s or q')
        #Display the player choice
    if playerMove == 'r':
        print ('ROCK versus...')
    elif playerMove == 'p':
        print ('PAPER versus...')
    elif playerMove == 's':
        print ('SCISSORS versus...')
    #Display what the computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print ('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    #Display the results
    if playerMove == computerMove:
        print('It\'s a draw!')
        draws = draws + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1            