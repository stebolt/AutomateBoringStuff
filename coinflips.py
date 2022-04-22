# Random chance of coinflips
import random
numberofStreaks = 0
for experimentNumber in range(10000):
    #code that creates the list of 100 heads or tails
    coinFlips = ''
    for x in range(100):
        if random.randint(0,1) == 0:
            coinFlips += 'H'
        else:
            coinFlips += 'T'
    
    #code that checks for a streak of 6 Hs or Ts in a row
    if 'HHHHHH' in coinFlips:
        numberofStreaks += 1
    elif 'TTTTTT' in coinFlips:
        numberofStreaks += 1
    
print('Chance of a streak %s%%' % (numberofStreaks / 100))