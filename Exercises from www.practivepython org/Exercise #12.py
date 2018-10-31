# Exercise #12
# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function.
'''

a = [5, 10, 15, 20, 25]
def list_ends(lst):
    return [lst[0], lst[-1]]
