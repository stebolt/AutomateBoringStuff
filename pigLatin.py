print('A change to the proceeds: Enter the English message to translate into Pig Latin: ')
message = input()
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = []  # A list of the words in Pig Latin
for word in message.split():
    # seperate the non letters at the start of the word.
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    # seperate the non letters at the end of the word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        word = word[:1]
    #remember if the word was in uppercase or lowercase
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    # add the pig Latin to the end of the word.
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    # set the word back to upper or title case.
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    # add the non letter to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
# Join all the words together
print(' '.join(pigLatin))
