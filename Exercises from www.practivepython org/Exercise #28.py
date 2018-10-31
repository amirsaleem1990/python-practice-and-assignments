# Exercise #28
# http://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
'''
Implement a function that takes as input three variables, and returns the largest of the
three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally takes
care of for us. All you need is some variables and if statements!
'''
def max_of_three(v1, v2, v3):
    if v1 > v2 and v1 > v3: return v1
    elif v2 > v3 and v2 > v1: return v2
    else: return v3

print('max of (4, 2, 1): ' + str(max_of_three(4, 2, 1)))
print('max of (1, 0, 6): ' + str(max_of_three(1, 0, 6)))
print('max of (4, 7, 1): ' + str(max_of_three(4, 7, 1)))
print('max of (5, 7, 1): ' + str(max_of_three(5, 7, 1)))
print('max of (4, 0, 1): ' + str(max_of_three(4, 0, 1)))
print('max of (4, 7, 9): ' + str(max_of_three(4, 7, 9)))
print('max of (4, 8, 1): ' + str(max_of_three(4, 8, 1)))
