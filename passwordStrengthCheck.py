# password strength check
import re


def checkLength(password):
    passLengthRegex = re.compile(r'\S{8}')
    moLength = passLengthRegex.search(password)
    passUpperRegex = re.compile(r'[A-Z]')
    moUpper = passUpperRegex.search(password)
    passLowerRegex = re.compile(r'[a-z]')
    moLower = passLowerRegex.search(password)
    passDigitRegex = re.compile(r'[0-9]')
    moDigit = passDigitRegex.search(password)
    if moUpper and moLower and moDigit and moLength:
        return True
    else:
        print


print('Enter a password to validate')
password = input()
if checkLength(password):
    print('Valid password')
else:
    print('Invalid password')
