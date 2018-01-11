# Exercise #30
# download the SOWPODS dictionary file from http://norvig.com/ngrams/sowpods.txt
import random
def pick_word():
    return random.choice([i.lower() for i in open('/home/hp/Desktop/Exercises from www.practivepython org/exercise_30_related file.txt', 'r').read().split()])

# Exercise #32

def guess_letters():
    random_word = pick_word()
    a = [i for i in random_word]
    m = a[:]
    l = 0
    d = ['_' for i in range(len(random_word))]
    print('Welcome to Hangman!')
    [print(i, end='') for i in d]; print('\n')
    while '_' in d and l < 6:
        if d != m:
            print(str(6-l) + ' turns left')
            b = input('Enter a single latter: ')
            if b not in d:
                l +=1
                if len(b) == 1 and b in a:
                    for i in range(a.count(b)):
                        d[a.index(b)] = b; a[a.index(b)]= ' '
                [print(i, end='') for i in d]; print('\n')
            else: print('you entered this latter before.. plz enter onother latter..\n')
    if d == m:
        return 'Congratulation! you guess the word in ' + str(l)+' turns'
    else: return 'Game over!... try again'
print(guess_letters())









