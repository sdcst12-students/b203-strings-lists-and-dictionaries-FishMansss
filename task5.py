import os


##possible items
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



     
##ui + displays
g=1
while g==1:
    os.system('cls')
    print("get, drop or show item: ")
    x = input()
    if x in "get, get item, getitem":
       
        print("item: ")
        item = input()
        print("amount: ")
        amount = int(input())

        possibleItems[item] += amount
        
    if x in "drop, drop item, dropitem":
       
        print("item: ")
        item = input()
        print("amount: ")
        amount = int(input())
        possibleItems[item] -= amount
        

    if x in "show, show item, showitem":
      
        print(possibleItems)
        input('press "ENTER" to continue ')