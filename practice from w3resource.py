# practice from w3resource.com
'''
1- Write a python program to calculate the length of a string
'''
def len_of_str(string):
    return(len(string))
print(len_of_str('amir saleem'))

'''
2- Write a python program to count the number of characters
(character frequency) in a string.
Sample String: google.com
Expected Result : {'o':3, 'g':2, '':1, 'e':1, 'l':1, 'm':1, 'c':1}
'''
def cout_nm_of_chr(string):
    a = dict()
    for i in string:
        if i not in a: a[i] = string.count(i)
    return a
print(cout_nm_of_chr('google.com'))

'''
3- Write a python program to get a string made of the first 2 and
last 2 chars from a given a string. if the string length is less
than 2,retern instead of the empty string.
Sample string: 'w3resource'
Expected Result: 'w3ce'
Sample string: 'w3'
Expected Result: 'w3w3'
Sample string: 'w'
Expected Result: Empty string
'''
def mix(string):
    if len(string) < 2:
        return ''
    else:
        return string[:2]+string[-2:]
print(mix('w3resource'))
print(mix('w3'))
print(mix('w'))

########################################
'''
4- Write a python program to get a string from a givin string where
all occurrences of its first char have been changed to '$' expect
the first char itself.
Sample string: 'restart'
Expected Result: 'resta$t'
'''
def change(string):
    return string[0]+string[1:].replace(string[0], '$')

#########################################
'''
5- Write a python program to get a single string from two givin
strings. separated by a space and swap the first two characters of
each string.
Sample string: 'abc', 'xyz'
Expected Result: 'xyc abz'
'''
def swap(str1, str2):
    return str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]
print(swap('abc', 'xyz'))
##########################################
'''
6- Write a python program to add 'ing' at the end of a given
string (length should be at least 3). if the givin string already
ends with 'ing' the add 'ly' instead. if the string length of the
given string is less than 3, leave it unchanged.
Sample String: 'abc'
Expected Result: 'abcing'
Sample String: 'string'
Expected Result: 'stringly'
'''
def add_ing(string):
    if len(string) < 3:
        return string
    else:
        if string[-3:] == 'ing': return string+'ly'
        else: return string+'ing'
print(add_ing('abc'))
print(add_ing('string'))
############################################
'''
7- Write a python program to find the first appearance of the
substring'not' and 'poor' from a given string. if 'bad' follows
the 'poor', replace the whole 'not'...'poor' substring with
'good'. Return the resulting string.
Sample String: 'The lyrics is not htat poor!'
Expected Result: 'The lyrice is good!'
'''
def bad_poor(string):
    if string.index('not') < string.index('poor'):
        return string[:string.index('not')]+ ' good' + string[string.index('poor')+4:]

print(bad_poor('The lyrics is not that poor!'))

##############################################
'''
8- write a python function that takes a list of words and returns
the length of the longest one
'''
def longist_one(lst):
    a = list()
    a.append([len(i) for i in lst])
    return max(a[0])

print(longist_one(['a', 'm', 'ir', ' ', 's', 'sal', 'e', 'em']))
print(longist_one(['a', 'm', 'ir', ' ', 's', 'sa', 'e', 'em']))
###############################################
'''
9- write a python program to remove the nth index character from
a nonempty string.
'''
def rmv_nth(string):
    return string[:9]+string[10:]
print(rmv_nth('my name is amir saleem'))
################################################
'''
10- write a python program to change a given string to a new
string where the first and last chars have been exchanged
'''
def first_last_exchange(string):
    return string[-1]+string[1:-1]+string[0]
print(first_last_exchange('amir saleem'))
#################################################
'''
11- Write a python program to remove the characters which have
odd index values of a given string
'''
def no_odd(string):
    [print(string[i], end='') for i in range(1, len(string)+1, 2)]; return ''
print(no_odd('my name is amir saleem'))
##################################################
'''
12- Write a python program to count the occurrences of each word
in given sentence'
'''
def count_of_occurrences(string):
    a = list(set(string))
    for i in a:
        print(i, string.count(i))
    return ''
print(count_of_occurrences('amir saleem'))
##################################################
'''
13- Write a python script that takes input from the user and
displays that input back in upper and lower casses
'''
a = input('Type anything: ')
print('\nyour input in upper case:\n',a.upper()); print('\nyour input in lower case:\n',a.lower())

##################################################
'''
14- Write a python program that accepts a comma seperatd sequence
of words as input and prints the unique words in sorted from
(alphanumerically).
Sample Words: red, white, black, red, green, black
Expected Result: black, green, red, whited, red
'''
b = input('type anything.. we remove dulacates from your input \n')
c = list(set(b)); c.sort()
for i in c: print(i)
###################################################
'''
17- write a python function to get a string made of 4 copies of
the last two characters of a specified stiring(lenght must be at
least 2)
Sample function and result:
insert_end('python') -> onononon
insert_end('Exercises') -> eseseses
'''
def insert_end(string):
    if len(string) > 1:
        return string[-2:]*4

print(insert_end('python'))
print(insert_end('Exercises'))
####################################################
'''
18- write a python function to get a string made of its first
three characters of a specified string. if the length of the
string is less than 3 than return the original string.
Sample function and result:
first_three('ipy') -> ipy
first_three('python') -> pyt
'''
def first_three(string):
    if len(string) < 3: return string
    else: return string[:3]

print(first_three('ipy'))
print(first_three('python'))
######################################################
'''
19- write a python program to get the last part of a string before
a specified character
'''
def e19(string, character):
    return string[:string.index(character)]

print(e19('my name is amir - saleem', '-'))
print(e19('my name ,is amir - saleem', ','))
#######################################################
'''
20- write a python function to reverses a string if it's length
is a multiple of 4
'''
def reverse(string):
    if len(string) % 4 == 0:
        b = str()
        for i in string:
            b = i + b
    return b

print(reverse('aamir saleem'))
print(reverse('computer'))
#########################################################
'''
21- write a python function to convert a given string to all
uppercases if it contains at least 2 uppercases characters in
the first 4 characters.
'''
def conv_to_upper(string):
    a = int()
    for i in string[:4]:
        if i.isupper(): a += 1
    if a >= 2: return string.upper()
    else: return 'program can\'t working'
print('1',conv_to_upper('AmiRsaleem'))
print('2', conv_to_upper('AmirSaleem'))
print('3', conv_to_upper('amirsaleem'))
##########################################################
'''
22- write a python program to sort a string lexicographically
'''

'''
23- write a python program to remove a newline in python
'''
def remove_newline(string):
    return string.replace('\n', '')


print('my name \nis amir saleem')
print(remove_newline('my name \nis amir saleem'))
############################################################
'''
24- write a python program to check whether a string starts with
specified characters
'''
def start_with(string, word):
    return string.startswith(word)

print(start_with('amir saleem', 'f'))
print(start_with('amir saleem', 'a'))
#############################################################
'''
25- write a python program to create a Ceaser encryption.
Note: in cryptography, a caesar cipher, also known as caer's
cipher, the shift cipher, Caesar's code or Caesar shift, is one
of the simplest and most widely known encryption techniques. it is
a type of substitution cipher in which each latter in the
plaintext is replaced by a latter some fixed number of positions
down the alphabet. For example, with a left shift of 3, D would
be replaced by A, E would become B, and so on. The method is
named after Julius Caesar, who used it in his private
correspondence.
'''

'''
26- write a python program to display formatted text(width = 50)
as output.
'''

'''
27- Write a python program to remove existing indentation from all
of the line in a given text.
'''


'''
28- Write a python program to add a prefix text to all of the
lines in a string.
'''

'''
29- Write a python program to set the indentation of the first
line.
'''
def first_line (string):
    return '\t'+string

print(first_line('amir\nsaleem'))
###############################################
'''
30- Write a Pyhton program to print the following floating
numbers upto 2 decimal places.
'''
def upto_2_dcml(float_number):
    return round(float_number, 2)

print(upto_2_dcml(4.7777777))
'''
31- Write a python program to print the following floating numbers
upto 2 decimal places with a sign.
'''

'''
32- Write a python program to print the following floating numbers
with no decimal places.
'''

33- Write a python program to print the following integers with zeros on the left of specified widht.
34- Write a python program to print the following integers with '*' on the right of specified width.
35- Write a python program to display a number with a comma seprator.
36- Write a python program to format a number with a percentage.
37- Write a python program to display a number in left, right, and center alignd of widht 10
38- Write a python program to count occurences of a substring in a string.
39- Write a python program to reverse a string.
40- Write a python program to reverse words in a string
41- Write a python program to strip a set of characters from a string.
42- Write a python program to count repeated characters in a string.
Sample string:
'thequickbrownfoxjumpsoverthelazydog'
Expected output:
0 4
e 3
u 2
h 2
r 2
t 2
43- write a python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder is 1254.725cm3
