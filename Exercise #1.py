# Exercise 1
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
'''
Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old.
Extras:
1-Add on to the previous program by asking the user for another number and printing out
that many copies of the previous message. (Hint: order of operations exists in Python)
2-Print out that many copies of the previous message on separate lines. (Hint:
the string "\n is the same as pressing the ENTER button)
'''
import datetime
b = datetime.datetime.now().year
def character_input(name, age):
    return 'hi ' + name + '! you was born in ' + str(b - age) + ' you will become at the age of 100 years old in the year: ' + str(b - age + 100) + '\n' 

print(character_input('amir', 27))
print(character_input('umair', 32))
