# Execsize #9
# www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
from random import randint as r
a = int(input('we have number.. gess the number\n(from 0 to 9): '));b = r(0, 9)
if a == b: print('Exactly right!!')
elif a - b > 3 or b - a > 3: print('You guessed too low')
else: print('You guessed too high')
print('your number: '+ str(a)); print('our number: ' + str(b))
