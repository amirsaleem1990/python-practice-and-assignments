# Exercise #14
# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
'''
Write a program (function!) that takes a list and returns a new list that contains all
the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and
another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different
function.
'''
def list_remove_duplicates_v1(lst):
    a = list()
    [a.append(i) for i in lst if i not in a]; return a


    
def list_remove_duplicates_v2(lst):
    return list(set(lst))
