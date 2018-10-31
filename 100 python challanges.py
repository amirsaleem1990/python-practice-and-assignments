'''
1- Write a program which will find all such numbers which are divisible
by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a
single line.
'''
[print(i, end=',') for i in range(2000,3201) if i & 7 == 0 and i % 5 != 0]
###########################################
'''
2- Write a program which can compute the factorial of a given numbers. The
results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
'''
e = int(input('Enter a number: ')); d = 1
for i in [e - i for i in range(e)]: d *= i
print(d)
############################################
'''
3- With a given integral number n, write a program to generate a
dictionary that contains (i, i*i) such that is an integral number between
1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
f = int(input('Enter a number: '))
dic = dict()
for i in range(1, f+1): dic[i] = i*i
print(dic)
#############################################
'''
4- Write a program which accepts a sequence of comma-separated numbers from
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
def tup_and_list(*numbers):
    print([i for i in numbers])
    print(tuple(i for i in numbers))
#############################################
'''
5- Define a class which has at least two methods:
getString: to get a string from console input printString: to print the
string in upper case.
Also please include simple test function to test the class methods.
'''
class Myclass():
    def getString(self, string):
        self.input = string
    def printString(self):
        return self.input.title()
        
a = Myclass()
print(a.getString('amir saleem'))
print(a.printString())
##############################################
'''
6- Write a program that calculates and prints the value according to the
given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example:
Let us assume the following comma separated input sequence is given to
the program:
100,150,180
The output of the program should be:
18,22,24
'''
from math import sqrt as s
def ex_6(*numbers):
    C = 50; H = 30; 
    return [round(s((2*C*D)//H))for D in numbers]

# for test:
m = [100, 150, 180]
for i in range(5):
    print('***' + str(m[0]), str(m[1]), str(m[2]) + '***')
    print(ex_6(m[0],m[1],m[2]))
    m[0] += 10; m[1] += 15; m[2] += 20
############################################
'''
7- Write a program which takes 2 digits, X,Y as input and generates a
2-dimensional array. The element value in the i-th row and j-th column of
the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
def two_dim_array(nm1, nm2):
    g = list()
    for i in range(nm1):
        g.append([i*b for b in (range(nm2))])
    return g
# for test:
a = [3, 5]
for i in range(5):
    print('***' + str(a[0]) , str(a[1]) + '***')
    print(two_dim_array(a[0], a[1]))
    a[0] += 2; a[1] += 2; a[2] += 2
###################################################
'''
*Question 8
*Level 2
Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
def sort_words(*words):
    return sorted(words)

# for test:
print(sort_words('without','hello','bag','world'))
#######################################################
'''
Question 9
Level 2
Write a program that accepts sequence of lines as input and prints the
lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
def uper(*lines):
    for i in lines: print(i.upper())
    return ''
print(uper('Hello world', 'Practice makes perfect'))
######################################################
'''
Question 10
Level 2
Question:
Write a program that accepts a sequence of whitespace separated words as
input and prints the words after removing all duplicate words and sorting
them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
a = list(set(input('Enter sequance of words sapateated by space: ').split())); a.sort() 
k = str()
for i in a: k += i+' ' 
print(k)
#############################################
'''
Question 11
Level 2

Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not
. The numbers that are divisible by 5 are to be printed in a comma
separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010, 0100
Notes: Assume the data is input by console.
'''
[print(i, end=',') for i in [b for b in input('Enter a sequence of comma separeted 4 digit binary numbers: ').split(',')] if int(i) % 5 == 0]
###############################################
'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a
single line.
'''
# v1:
for i in range(1000, 3001):
    a = str(i); 
    if int(a[0]) % 2 == 0 and int(a[1]) % 2 == 0 and int(a[2]) % 2 == 0 and int(a[3]) % 2 == 0:
        print(i, end=',')    

# v2:
d = list()
for i in range(1000, 3000):
    a = str(i); c = 0
    for b in a:
        if int(b) % 2 == 0: c += 1
    if c == len(a): d.append(i)
print(d)

##################################################
'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
a = [i for i in input('Enter a sentence: ')]
print('LETTERS '+ str(len([i for i in a if i.isalpha()])))
print('DIGITS ' + str(len([i for i in a if i.isdigit()])))
    
##################################################
'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper
case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
a = [i for i in input('Enter a sentence: ')]
print('UPPER CASE '+ str(len([i for i in a if i.isupper()])))
print('LOWER CASE ' + str(len([i for i in a if i.islower()])))

######################################################
'''
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given
digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
a = int(input('Enter a number: '))
print(a+(a*11)+(a*111)+(a*1111))

########################################################
'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is
input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
a = input('Enter a sequence of comma_separated numbers: ').split()
for i in a[0]:
    if i.isdigit() and int(i) % 2 != 0:
        print(i, end=',')
########################################################
'''
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown
as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
a = True; e = int()
while a:
    b = input('\nEnter your transaction: \n[The transaction log format is shown as following]:\nD 100 \nW 200\n[for exit type xit] ')  
    if b.lower() != 'xit':
        c = b[0]; d = b[2:]
        if b[0].lower() == 'd': e += int(b[2:])
        elif b[0].lower() == 'w': e -= int(b[2:])
    else:print(e); a = False
###############################################################
'''
Question 18
Level 3
Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria. Passwords that match the
criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
n = 'ABd1234@1','a F1#','2w3E*','2We3345'
def password(*passwords):
    a = list()
    for i in passwords:
        f = list(i)
        upper = 0; lower = 0; sign = 0; num = 0
        for g in f:
            if g.islower(): lower += 1
            elif g.isupper(): upper += 1
            elif g in '$#@': sign += 1
            elif g.isnumeric(): num += 1
        if upper and lower and sign and num and 5 < len(i) < 13: a.append(i)
    return a

print( password('ABd1234@1','a F1#','2w3E*','2We3345'))
####################################################
'''
Question 19
Level 3
Question:
You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are
numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]
'''
def info(name, age, score, *another_person):
    bb = list(); cc = list()
    for i in name, age, score: cc.append(i)
    bb.append(tuple(cc))
    for i in range(len(another_person)//3):
        bb.append(another_person[i*3:(i*3)+3])
    return sorted(bb)
    
print(info('tom', 19, 80), ('john', 20, 90),('jony', 17, 91),('jony', 17, 93), ('json', 21, 85))

################################################################
'''
Question 20
Level 3
Question:
Define a class with a generator which can iterate the numbers, which are
divisible by 7, between a given range 0 and n.
'''
class generator():
    def gen(self, number):
        return [i for i in range(0, number) if i % 7 == 0]
a = generator()
print(a.gen(70))
print(a.gen(355))
####################################################################
'''
Question 21
Level 3
Question:
A robot moves in a plane starting from the original point (0,0). The
robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The
trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to
compute the distance from current position after a sequence of movement
and original point. If the distance is a float, then just print the
nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''

##################################################
'''
Question 22
Level 3
Question:
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
a = input('Enter your sentence: ').split()
b = list(set(a))
[print(i+':'+str(a.count(i))) for i in b]
#################################################
'''
Question 23
level 1
Question:
    Write a method which can calculate square value of number
'''
class maths():
    import math
    def sqr(self, number):
        return self.math.sqrt(number)
a = maths()
print(a.sqr(5))
print(a.sqr(7))
###################################################
'''
Question 24
Level 1
Question:
Python has many built-in functions, and if you do not know how to use it,
you can read document online or find some books. But Python has abuilt-in
document function for every built-in functions. Please write a program to
print some Python built-in functions documents, such as abs(), int(),
raw_input() And add document for your own function
'''
for i in abs, int, input:
    print('*****Document for '+ str(i) + ' function:*****\n')
    print(i.__doc__)

def print_name(name):
    '''
    (str) -> str
    return a str in title case.
    '''
    return name.title()
print(print_name.__doc__)
##############################################################
'''
Question:
Define a class, which have a class parameter and have a same instance
parameter.
'''


###############################################################
'''
Question:
Define a function which can compute the sum of two numbers.
'''
def sum_two(num1, num2):
    return num1 + num2
print(sum_two(4, 9))
#######################################################
'''
Question:
Define a function that can convert a integer into a string and print it
in console.
'''
def int_to_str(num):
    return str(num)
print(int_to_str(44))
#######################################################
'''
Question:
Define a function that can receive two integral numbers in string form
and compute their sum and then print it in console.
'''
def str_to_int(num1, num2):
    return int(num1) + int(num2)
print(str_to_int('44', '2'))
############################################################
'''
2.10
Question:
Define a function that can accept two strings as input and concatenate
them and then print it in console.
'''
def single_str(str1, str2):
    return str1+ ' ' + str2
print(single_str('amir', 'saleem'))
###################################################
'''
2.10
Question:
Define a function that can accept two strings as input and print the
string with maximum length in console. If two strings have the same
length, then the function should print all strings line by line.
'''
def max_str(str1, str2):
    if len(str1) != len(str2):
        a = str()
        for i in str1, str2:
            if len(i) > len(a): a = i
        return a
    else:
        for i in str1, str2: print(i, end= ' ')
    return ''
print(max_str('amir', 'saleem'))
print(max_str('amir', 'sale'))
print(max_str('abc', 'amir'))
#############################################################
'''
2.10
Question:
Define a function that can accept an integer number as input and print
the "It is an even number" if the number is even, otherwise print "It is
an odd number".
'''
def even_or_odd(num):
    if num % 2 == 0: return 'It is an even number'
    else: return 'It is an odd number'

print(even_or_odd(7))
print(even_or_odd(88))
##############################################################
'''
2.10
Question:
Define a function which can print a dictionary where the keys are numbers
between 1 and 3 (both included) and the values are square of keys.
'''
def dic():
    d = {}
    for i in range(1,4):
        d[i] = i*i
    return d

print(dic())
#################################################################
'''
2.10
Question:
Define a function which can print a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys.
'''
def dic_20():
    d = {}
    for i in range(1,21): d[i] = i*i
    return d

print(dic_20())
######################################################################
'''
2.10
Question:
Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of
keys. The function should just print the values only.
'''
def dic_20_values():
    d = {}
    for i in range(1,21): d[i] = i*i
    return d.values()

print(dic_20_values())
####################################################################
'''
2.10
Question:
Define a function which can generate a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of
keys. The function should just print the keys only.
'''
def dic_20_keys():
    d = {}
    for i in range(1,21): d[i] = i*i
    return d.keys()

print(dic_20_keys())
#####################################################
'''
2.10
Question:
Define a function which can generate and print a list where the values
are square of numbers between 1 and 20 (both included).
'''
def list_20():
    return [i*i for i in range(1, 21)]
print(list_20())
########################################################
'''
Question:
Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to
print the first 5 elements in the list.
'''
def list_20_first_five():
    return [i*i for i in range(1, 21)][:5]
print(list_20_first_five())
#####################################################
'''
2.10
Question:
Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to
print the last 5 elements in the list.
'''
def list_20_last_five():
    return [i*i for i in range(1, 21)][-5:]
print(list_20_last_five())
#######################################################
'''
Question:
Define a function which can generate a list where the values are square
of numbers between 1 and 20 (both included). Then the function needs to
print all values except the first 5 elements in the list.
'''
def list_20_last_15():
    return [i*i for i in range(1, 21)][5:]
print(list_20_last_15())
############################################################
'''
2.10
Question:
Define a function which can generate and print a tuple where the value
are square of numbers between 1 and 20 (both included). 
'''
def tuple_20():
    return tuple([i*i for i in range(1, 21)])
print(tuple_20())
##################################################################
'''
2.10
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the
first half values in one line and the last half values in one line. 
'''
a = (1,2,3,4,5,6,7,8,9,10)
print(a[:len(a)//2]); print(a[len(a)//2:])
##########################################################
'''
2.10
Question:
Write a program to generate and print another tuple whose values are
even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''
a = (1,2,3,4,5,6,7,8,9,10)
print(tuple([i for i in a if i % 2 == 0]))
#######################################################
'''
2.14
Question:
Write a program which accepts a string as input to print "Yes" if the
string is "yes" or "YES" or "Yes", otherwise print "No". 
'''
a = input('Enter something: ')
if a in ['yes', 'YES', 'Yes']: print('Yes')
else: print('No')
###########################################
'''
3.4
Question:
Write a program which can filter even numbers in a list by using filter
function. The list is: [1,2,3,4,5,6,7,8,9,10].
'''



############################################
'''
3.4
Question:
Write a program which can map() to make a list whose elements are square
of elements in [1,2,3,4,5,6,7,8,9,10].
'''
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x * x, a)))
###################################################
'''
3.5
Question:
Write a program which can map() and filter() to make a list whose
elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''


#######################################################
'''
3.5
Question:
Write a program which can filter() to make a list whose elements are
even number between 1 and 20 (both included).
'''
######################################################
'''
Question:
Write a program which can map() to make a list whose elements are square
of numbers between 1 and 20 (both included).
'''
m = list(range(21))
print(list(map(lambda x: x * x, m)))
#####################################################
'''
7.2
Question:
Define a class named American which has a static method called
printNationality.
'''
class American():
    def printNationality(self):
        return 'American'
a = American()
print(a.printNationality())
########################################################
'''
7.2
Question:
Define a class named American and its subclass NewYorker. 
'''
class American():
    """ """
class NewYorker(American):
    """ """
a = American()
b = NewYorker()
##########################################################
'''
Question:
Define a class named Circle which can be constructed by a radius. The
Circle class has a method which can compute the area. 
'''

class Circle():
    def __init__(self, num):
        from math import radians as r
        self.num = num
        self.radius = r(num)
    def area(self):
        return 3.14* self.num/2 * self.num/2

a = Circle(8)
print(a.radius)
print(a.area())
##########################################################
'''
7.2
Define a class named Rectangle which can be constructed by a length and
width. The Rectangle class has a method which can compute the area. 
'''
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

a = Rectangle(12, 16)
print(a.area())
########################################################
'''
7.2
Define a class named Shape and its subclass Square. The Square class has
an init function which takes a length as argument. Both classes have a
area function which can print the area of the shape where Shape's area is
0 by default.
'''
class Square():
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
class Shape(Square):
    def areaa(self, length = 0):
        return length ** 2

a = Square(12)
print(a.area())
b = Shape(13)
print(b.area())
print(b.areaa())

####################################################
'''
Please raise a RuntimeError exception.
'''


#####################################################
'''
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''

####################################################
'''
Define a custom exception class which takes a string message asattribute.
'''


######################################################
'''
Question:
Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to print the user
name of a given email address. Both user names and company names are
composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be
assumed to be a console input.
'''
a = input('Enter your email: ')
b = a.find('@')
print(a[:b])
########################################################
'''
Question:
Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to print the
company name of a given email address. Both user names and company names
are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
In case of input data being supplied to the question, it should be
assumed to be a console input.
'''
a = input('Enter your email: ')
b = a.find('@'); c = a.find('.com')
print(a[b+1:c])
##########################################################
'''
Question:
Write a program which accepts a sequence of words separated bywhitespace
as input to print the words composed of digits only.
Example:
If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
In case of input data being supplied to the question, it should be
assumed to be a console input.
'''
a = input('Enter a string: ').split()
print([i for i in a if i.isnumeric()])
#########################################################
'''
Question:
Print a unicode string "hello world".
'''




##########################################################
'''
Write a program to read an ASCII string and to convert it to a unicode
string encoded by utf-8.
'''





######################################################3
'''
Write a special comment to indicate a Python source code file is in
unicode.
'''






#############################################
'''
Question:
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
console (n>0).
[for i in range(n, n+1)]
'''
n = int(input('Enter a number: '))

a = int()
for i in range(1, n+1):
    a += i/(i+1)
print(a)
#################################################
'''
Question:
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be
assumed to be a console input.
'''







##########################################################33
'''
Question:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input
by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
13
In case of input data being supplied to the question, it should be
assumed to be a console input.
'''
def fibonacci(number):
    b = [0, 1]
    for i in range(number-1): b.append(sum(b[-2:]))
    return b[-1]
# for testing:
for i in range(7,20): print(fibonacci(i))
###########################################################
'''
Question:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci
Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
'''
a = [0, 1]
[a.append(sum(a[-2:])) for i in range(int(input('Enter a number: '))-1)]
print(a)
###############################################################
'''
Question:
Please write a program using generator to print the even numbers between 0
and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
'''
a = int(input('Enter your number: '))
print([i for i in range(a+1) if i % 2 == 0])
#################################################################
'''
Question:
Please write a program using generator to print the numbers which can be
divisible by 5 and 7 between 0 and n in comma separated form while n is
input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
'''
a = int(input('Enter a number: '))
print([i for i in range(a+1) if i % 7 == 0 and i % 5 == 0])
###########################################################33
'''
Question:
Please write assert statements to verify that every number in the list
[2,4,6,8] is even.
'''
a = [2, 4, 7, 8]
for i in a:
    assert i % 2 == 0

##############################################################
'''
Question:
Please write a program which accepts basic mathematic expression from
console and print the evaluation result.
Example:
If the following string is given as input to the program:
35+3
Then, the output of the program should be:
38
'''




############################################################
'''
Question:
Please write a binary search function which searches an item in a sorted
list. The function should return the index of element to be searched in
the list.
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def binary_search(lst, number):
    a = 1; lst1 = lst[:]
    while a:
        if number < lst[len(lst)//2]: lst = lst[:len(lst)//2]
        else: lst = lst[len(lst)//2:]
        if len(lst) == 1: a = 0
    if lst[0] == number: return lst1.index(number)
    else: return 'your number not in your provided list'
# for testing the function
for i in range(15):
    print(str(i), end='\t')
    print(binary_search(a, i))

########################################################
'''
Question:
Please generate a random float where the value is between 10 and 100
using Python math module.
'''
import random
a = [i+(b/100) for i in range(100) for b in range(100)]
rint(random.choice(a))
# for test:
for i in range(5):
    print(random.choice(a))
############################################################
'''
Question:
Please generate a random float where the value is between 5 and 95 using
Python math module.
'''
import random
a = [i+(b/100) for i in range(5, 95) for b in range(100)]
print(random.choice(a))
# for test:
for i in range(5):
    print(random.choice(a))
############################################################
'''
Question:
Please write a program to output a random even number between 0 and 10
inclusive using random module and list comprehension.
'''
import random as r
print(r.choice([i for i in range(0, 11, 2)]))

# for test:
for i in range(15):
    print(r.choice([i for i in range(0, 11, 2)]))
###################################################
'''
Question:
Please write a program to output a random number, which is divisible by 5
or 7, between 0 and 10 inclusive using random module and list
comprehension.
'''
import random as r
print(r.choice([i for i in range(0, 11) if i % 5 == 0 or i % 7 == 0]))

# for test:
for i in range(10):
    print(r.choice([i for i in range(0, 11) if i % 5 == 0 or i % 7 == 0]))    
#####################################################
'''
Question:
Please write a program to generate a list with 5 random numbers between
100 and 200 inclusive.
'''
import random
print([random.randint(100, 200) for i in range(5)])

# for test:
for i in range(5):
    print([random.randint(100, 200) for i in range(5)])
####################################################
'''
Question:
Please write a program to randomly generate a list with 5 even numbers
between 100 and 200 inclusive.
'''
import random
print([random.choice([b for b in range(0, 101, 2)]) for i in range(5)])

# for test:
for i in range(5):
    print([random.choice([b for b in range(0, 101, 2)]) for i in range(5)])
#######################################################
'''
Question:
Please write a program to randomly generate a list with 5 numbers, which
are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''
import random
print([random.choice([b for b in range(1, 1001) if b % 5 == 0 and b % 7 == 0]) for i in range(5)])

# for test:
for i in range(5):
    print([random.choice([b for b in range(1, 1001) if b % 5 == 0 and b % 7 == 0]) for i in range(5)])
#####################################################
'''
Question:
Please write a program to randomly print a integer number between 7 and
15 inclusive.
'''
from random import randint as r
print(r(7, 15))

# for test:
for i in range(5):
    print(r(7, 15))
########################################################3
'''
Question:
Please write a program to compress and decompress the string "hello world!
hello world!hello world!hello world!".
'''






######################################################
'''
Question:
Please write a program to print the running time of execution of "1+1"
for 100 times.
'''
from datetime import datetime
start_time = datetime.now()
for i in range(100):
    1 + 1
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
################################################
'''
Question:
Please write a program to shuffle and print the list [3,6,7,8].
'''
import random
a = list(); lst = [3,6,7,8]; count = 0
while len(a) != len(lst):
    b = random.choice(lst)
    if b not in a: a.append(b)
print(a)
##################################################
'''
Question:
Please write a program to generate all sentences where subject is in
["I", "You"] and verb is in ["Play", "Love"] and the object is in
["Hockey","Football"].
'''
a = ["I", "You"] ; b = ["Play", "Love"]; c = ["Hockey","Football"]
for i in a:
    for z in b:
        for q in c:
            print(i + ' ' + z + ' ' + q)

###################################################
'''
Please write a program to print the list after removing delete even
numbers in [5,6,77,45,22,12,24].
'''	
a = [5,6,77,45,22,12,24]
for i in a:
    if i % 2 == 0:
        a.remove(i)
print(a)
#####################################################
'''
Question:
By using list comprehension, please write a program to print the list
after removing delete numbers which are divisible by 5 and 7 in
[12,24,35,70,88,120,155].
'''
a = [12,24,35,70,88,120,155]
[a.remove(z) for z in [i for i in a if i % 7 == 0 and i % 5 == 0]]
print(a)
#####################################################
'''
Question:
By using list comprehension, please write a program to print the list
after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
'''

a = [12,24,35,70,88,120,155]
[a.remove(a[i]) for i in [i for i in range(-len(a), 0, +2)]]
print(a)
#######################################################
'''
Question:
By using list comprehension, please write a program generate a 3*5*8 3D
array whose each element is 0.
'''
[print(i) for i in [[[0 for i in range(3)]for z in range(6)]for q in range(8)]]
############################################################
'''
Question:
By using list comprehension, please write a program to print the list
after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''
a = [12,24,35,70,88,120,155]
[a.remove(a[i]) for i in (5,4,0)]
print(a)
################################################################
'''
Question:
By using list comprehension, please write a program to print the list
after removing the value 24 in [12,24,35,24,88,120,155].
'''
a = [12,24,35,24,88,120,155]
[a.remove(i) for i in a if i == 24]
print(a)
#################################################################
'''
Question:
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
write a program to make a list whose elements are inter section of the
above given lists.
'''
a = [1,3,6,78,35,55]
b = [12,24,35,24,88,120,155]
print([i for i in list(set(b)) if i in list(set(a))])
############################################################
'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
print this list after removing all duplicate values with original order
reserved.
'''
'''
a = [12,24,35,24,88,120,155,88,120,155]
b = [i for i in range(1,len(a)-1)]; b.reverse()
for i in b:
    if a.count(a[i])>1:
        a.remove(a[i])
print(a)
'''
a = [12,24,35,24,88,120,155,88,120,155]
[a.remove(a[b]) for b in [-i for i in range(1,len(set(a)))] if a.count(a[b]) > 1]
print(a)
############################################################
'''
Question:
Define a class Person and its two child classes: Male and Female. All
classes have a method "getGender" which can print "Male" for Male class
and "Female" for Female class.
'''
class Person():
    """ """
class Male(Person):
    def getGender(self):
        print('Male')
class Female(Person):
    def getGender(self):
        print('Female')

amir = Male()
hamna = Female()
amir.getGender()
hamna.getGender()
############################################################
'''
Question:
Please write a program which count and print the numbers of each
character in a string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''
a = input('Enter a string: ')
b = list(set(a))
for i in b: print(i, str(a.count(i)))
################################################################
'''
Question:
Please write a program which accepts a string from console and print it
in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
'''
a = input('Enter your string: ')
b = [print(a[i],end='')for i in [-b for b in range(1, len(a)+1)]]
#################################################################
'''
Question:
Please write a program which accepts a string from console and print the
characters that have even indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
'''
a = 'H1e2l3l4o5w6o7r8l9d'
[print(a[i],end='') for i in range(0, len(a), 2)]
##################################################################
'''
Question:
Please write a program which prints all permutations of [1,2,3]
'''
import itertools
a = [1,2,3]
[print(i) for i in itertools.permutations(a)]
##################################################################
'''
Question:
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
'''
def Chinese_puzzle(heads, legs):
    rabbits = 0; chickens = 0; total = heads; tot = heads
    while total != 0 and legs > 0 and heads > 0 :
        legs -= 6; heads -= 2; rabbits += 1; chickens += 1; total -= 2
    while total != 0 or legs != 0 or heads != 0 :
        legs += 4; heads += 1; rabbits -= 1; total += 1
        if (tot-(rabbits+chickens))*2 == legs:
            legs -= (total * 2); heads -= total; chickens += total
            print('chickens: ' + str(chickens)); print('rabbits: '+ str(rabbits))
            return ''
# for test:
a = [35, 94]
for i in range(3):
    print('Heads: ' + str(a[0]) + ', Legs: ' + str(a[1]))
    print(Chinese_puzzle(a[0], a[1]))
    a[0] += 1; a[1] += 4
for i in range(3):
    print('Heads: ' + str(a[0]) + ', Legs: ' + str(a[1]))
    print(Chinese_puzzle(a[0], a[1]))
    a[0] += 1; a[1] += 2
