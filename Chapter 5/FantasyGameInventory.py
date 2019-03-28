inventory = {"rope" : 1, "torch": 2, "arrow": 16, "gold coin": 125, "bronze dagger" : 1}
loot = ["gold coin", "gold coin", "rope", "torch", "ruby"]

def displayInventory(inventory):
    for k, v in inventory.items():
        print(str(k) + " " + str(v))
    print ("Total number of items: " + str(sum(inventory.values())))

def addToInventory(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)

displayInventory(inventory)
addToInventory(inventory, loot)
displayInventory(inventory)