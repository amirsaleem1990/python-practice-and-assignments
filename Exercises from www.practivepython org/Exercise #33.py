# Exercise #33
# http://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
'''
This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises
are: Part 2, Part 3, and Part 4.
For this exercise, we will keep track of when our friend’s birthdays are, and be able to
find that information based on their name. Create a dictionary (in your file) of names
and birthdays. When you run your program it should ask the user to enter a name, and
return the birthday of that person back to them. The interaction should look something
like this:
>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
'''

birthday = {
    'amir' : '7 april 1990',
    'umair' : '1 jan 1985',
    'adil' : '1 jan 1987'
    }
print('welcome to the birthday dictionary. We know the birthdays of: ')
[print(i) for i in birthday]
a = input('\nWho\'s birthday you want to look up? ')
print(birthday[a])
