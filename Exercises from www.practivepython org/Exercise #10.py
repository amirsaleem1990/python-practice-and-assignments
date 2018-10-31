# Exercise #10
'''
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except
require the solution in a different way.
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of
different sizes. Write this using at least one list comprehension.
(Hint: Remember list comprehensions from Exercise 7).
The original formulation of this exercise said to write the solution using one line of
Python, but a few readers pointed out that this was impossible to do without using sets
that I had not yet discussed on the blog, so you can either choose to use the original
directive and read about the set command in Python 3.3, or try to implement this on your
own and use at least one list comprehension in the solution.
Extra:
Randomly generate two lists to test this
'''
from random import randint as r
a = [i for i in range(r(0,10))]
b = [i for i in range(r(0,10))]
def list_overlap_comprehensions(list1, list2):
    print('list1: \n', [i for i in list1])# deleting this line from code not affect our code
    print('list2: \n', [i for i in list2])# deleting this line from code not affect our code
    print('common elements in two lists: ')# deleting this line from code not affect our code
    return list(set([i for i in b if i in a]))
print(list_overlap_comprehensions(a, b))
