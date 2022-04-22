def collatz(number):
    if number % 2 == 0: # Number is even
        return number // 2
    else:               #Number is odd
        return 3 * number + 1

print('Enter a number...')
try:
    entry = int(input())
    while entry != 1:
        entry = collatz(entry)
        print(entry)
except ValueError:
    print('You didn\'t enter an integer, try again')
