stuff = {'rope': 1, "torch": 6, "gold coin": 42, "dagger": 1, 'Arrow': 12}
inv = ['gold coin','dagger','gold coin','gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory: ')
    items_total = 0
    for k,v in inventory.items():
        print(str(v) +" "+ k)
        items_total += v

    print("Total Number of Items: " + str(items_total))

def addToInventory(inventory, addItems):
    items_total = 0
    for k in addItems:
        if k in stuff.keys():
            stuff[k] += 1
    else:
        inventory[k] =+ 1

    for k,v in inventory.items():
        print(str(v) +" "+ k)
        items_total += v

    print("Total Number of Items: " + str(items_total))

addToInventory(stuff, inv)