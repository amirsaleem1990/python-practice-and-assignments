# Exersize #6
# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
# v_1
a = input('Enter a word,  we tell you is this palidrome or not: ')
f = 1
for i in range(len(a)//2):
    if a[i] != a[-(i+1)]: f = 0
print(bool(f))
    
'''
# v_2
a = input('Enter a word,  we tell you is this palidrome or not: ')
f = True
for i in range(len(a)//2):
    if f: f = a[i] == a[-(i+1)]
    else: f = False
print(f)


# v_3
a = input('Enter a word,  we tell you is this palidrome or not: ')
f = True
for i in range(len(a)//2):
    if a[i] == a[-(i+1)]: None# f = True
    else: f = False
print(f)
'''
