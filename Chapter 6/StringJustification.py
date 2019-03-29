items = {"copper" : 120, "silver" : 29, "gold" : 876, "gems" : 1100}

def printItems(items, rightJust, leftJust):
    print ("ALL ITEMS".center(rightJust + leftJust, "*"))
    for k, v in items.items():
        print (k.ljust(leftJust) + str(v).rjust(rightJust))

printItems(items, 10, 6)