import os



possibleItems = { 
        "food" : 0,
        "wate" : 0,
        "rope" : 0,
        "torc" : 0,
        "sack" : 0,
        "wood" : 0,
        "iron" : 0,
        "stee" : 0,
        "ging" : 0,
        "garl" : 0,
        "fish" : 0,
        "ston" : 0,
        "wool" : 0,
        }
inventory = {}

def getItem(item):
    amount0 = possibleItems[item]
    #inventory.update.possibleitems[item + amount0]
    # iterate possible Items
    # if amount of possible item > 0 then add the item to the inventory
    inventory.update( {item}  )
    
   
x = input("item ")
y = input("amount ")
getItem(x)











'''
os.system('cls')
print("get or show item: ")
x = str(input)
if x in "get, Get, GET":
    print("item: ")
    item = input()
    print("amount: ")
    amount = input()
    getItem(item, amount)
if x in "show, show item, showitem":
    print("item")
    item = input()
    showItem(item)        '''