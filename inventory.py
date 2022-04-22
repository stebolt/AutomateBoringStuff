# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print (str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for x in addedItems:
        if x in inventory.keys():
            inventory[x] = inventory[x] + 1
        else:
            inventory[x] = 1

    return inventory
    print('Done')

displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
