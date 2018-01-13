# Exercise 4
# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
'''
Create a program that asks the user for a number and then prints out a list of all the
divisors of that number. (If you don’t know what a divisor is, it is a number that
divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13
has no remainder.)
'''

a = int(input('Enter a number: '))
[print(i) for i in range(2, a+1, 1) if a % i == 0]
