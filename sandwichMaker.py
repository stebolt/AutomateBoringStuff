# sandwichMaker.py
import pyinputplus as pyip

price = 0
extras = 0


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


breadChoice = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                             prompt="What bread would you like?\n")
proteinChoice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                               prompt="Which protein would you like?\n")

if pyip.inputYesNo(prompt="Would you like cheese? ") == 'yes':
    cheeseChoice = pyip.inputMenu(
        ['cheddar', 'Swiss', 'mozzarella'], prompt="What cheese would you like?\n")
else:
    cheeseChoice = 'none'


if pyip.inputYesNo(prompt="Add mayo? ") == 'yes':
    extras += 1
if pyip.inputYesNo(prompt="Add mustard? ") == 'yes':
    extras += 1
if pyip.inputYesNo(prompt="Add lettuce? ") == 'yes':
    extras += 1
if pyip.inputYesNo(prompt="Add tomato? ") == 'yes':
    extras += 1

howManySandwiches = pyip.inputInt(
    prompt="How many sandwiches would you like? ", min=1)

price = costTally(breadChoice, proteinChoice,
                  cheeseChoice, extras, howManySandwiches)
print('Price is $' + str(price))
