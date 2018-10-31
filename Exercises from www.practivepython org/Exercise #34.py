# Exercise #34
# http://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
'''
This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises
are: Part 1, Part 3, and Part 4.
In the previous exercise we created a dictionary of famous scientists’ birthdays. In this
exercise, modify your program from Part 1 to load the birthday dictionary from a JSON
file on disk, rather than having the dictionary defined in the program.
Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
and update the JSON file you have on disk with the scientist’s name. If you run the
program multiple times and keep adding new names, your JSON file should keep getting
bigger and bigger.
'''

import json
birthday = {'amir' : '7-aug-1990','umair' : '1-jan-1985','adil' : '1-jan-1987'}
with open("info.json", "w") as f:
    json.dump(birthday, f)
    b = 1
    while b:
        a = input('add your friend name and his birthday to our json dict. : \n[folow this formet: {"amir" : "8-july-1997"}] ')
        if a == '': b = 0; open('info.json', 'r').close()
        else: json.dump(a, f)




# Exercise #35
