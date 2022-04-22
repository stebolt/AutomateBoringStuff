from hashlib import new


oneList = ['apples', 'bananas', 'tofu', 'cats']
twoList = ['goalie', 'defender', 13, 47.0, 'striker']
emptyList = []

def addAnd(andList):
    try:
        for x in range(len(andList) - 1):
            print(str(andList[x]), end=' ')
        print('and ' + str(andList[-1]))
    except:
        IndexError(print('The list is empty or otherwise invalid'))
   
addAnd(oneList)
addAnd(twoList)
addAnd(emptyList)