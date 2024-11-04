#!python3
"""
Have the user enter an integer value 'n'
write a python script to use all of the integers from 1-n as the keys and the squares of those numbers as the values (2 points)
sample result:
x = { 1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64, 9 : 81, 10 : 100 }
"""
import math
def squares(n):
    # n should be an integer value
    # x will be the generated dictionary
    x={}
    for i in range(n):
        if i**2 == round(i**2,0):
            x.update({i : i**2})        
    return x


x = input("input a range: ")
x = int(x)
squares(x)


'''
assert squares(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
assert squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}'''