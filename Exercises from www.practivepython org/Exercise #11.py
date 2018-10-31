# Exercise 11
# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
'''
Ask the user for a number and determine whether the number is prime or not. (For those
who have forgotten, a prime number is a number that has no divisors.). You can (and
should!) use your answer to Exercise 4 to help you. Take this opportunity to practice
using functions, described below.
'''

a = int(input('Enter a number and check: your number is prime or not? :'))
b = [i for i in range(2, a+1, 1) if a % i == 0]
if (list([a])) == b: print('Your number is Prime')
else: print('your number is not prime')
