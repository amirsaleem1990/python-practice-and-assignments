# Exercise #5
# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
'''
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of
different sizes.
Extras:
1- Randomly generate two lists to test this
2- Write this in one line of Python (don’t worry if you can’t figure this out at this
point - we’ll get to it soon)
'''
# v1
from random import randint as r
a = [i for i in range(r(0,10))]
b = [i for i in range(r(0,10))]
def list_overlap(list1, list2):
    print('list1: \n', [i for i in list1])# deleting this line from code not affect our code
    print('list2: \n', [i for i in list2])# deleting this line from code not affect our code
    print('common elements in two lists: ')# deleting this line from code not affect our code
    return list(set([i for i in b if i in a]))
print(list_overlap(a, b))
'''
# v2
import random
a = [int(random.choice('0123456789')) for i in range(8)]
b = [int(random.choice('0123456789')) for i in range(6)]
def list_overlap(list1, list2):
    print('list1: \n', [i for i in list1])
    print('list2: \n', [i for i in list2])
    print('common elements in two lists: ')
    return list(set([i for i in b if i in a]))
print(list_overlap(a, b))
'''
