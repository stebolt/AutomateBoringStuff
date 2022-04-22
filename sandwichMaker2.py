# sandwichMaker.py
import pyinputplus as pyip


def costTally(bread, protein, cheese, extras, howMany):
    totalCost = 0
    if bread == 'sourdough':
        totalCost += 1.5
    else:
        totalCost += 1
    if protein == 'tofu':
        totalCost += 4
    else:
        totalCost += 6
    if cheese != 'none':
        totalCost += 1
    return (totalCost + (extras * .25)) * howMany


def pickCheese():
    if pyip.inputYesNo(prompt="Would you like cheese? ") == 'yes':
        cheeseChoice = pyip.inputMenu(
            ['cheddar', 'Swiss', 'mozzarella'], prompt="What cheese would you like?\n")
    else:
        cheeseChoice = 'none'
    return cheeseChoice


def pickExtras():
    extras = 0
    if pyip.inputYesNo(prompt="Add mayo? ") == 'yes':
        extras += 1
    if pyip.inputYesNo(prompt="Add mustard? ") == 'yes':
        extras += 1
    if pyip.inputYesNo(prompt="Add lettuce? ") == 'yes':
        extras += 1
    if pyip.inputYesNo(prompt="Add tomato? ") == 'yes':
        extras += 1
    return extras


price = costTally(pyip.inputMenu(['wheat', 'white', 'sourdough'],
                                 prompt="What bread would you like?\n"),
                  pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                                 prompt="Which protein would you like?\n"),
                  pickCheese(),
                  pickExtras(),
                  pyip.inputInt(prompt="How many sandwiches would you like? ", min=1))
print('Price is $' + str(price))
