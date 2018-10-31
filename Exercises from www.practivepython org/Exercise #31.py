# Exercise #30
# download the SOWPODS dictionary file from http://norvig.com/ngrams/sowpods.txt
import random
def pick_word():
    return random.choice([i.lower() for i in open('/home/hp/Desktop/Exercises from www.practivepython org/exercise_30_related file.txt', 'r').read().split()])

# Exercise #31

def guess_letters():
    random_word = pick_word()
    a = [i for i in random_word]
    m = a[:]
    l = 0
    d = ['_' for i in range(len(random_word))]
    print('Welcome to Hangman!')
    [print(i, end='') for i in d]; print('\n')
    b = input('Enter a single latter: ')
    while '_' in d:
        if len(b) == 1 and b in a:
            for i in range(a.count(b)):
                d[a.index(b)] = b; a[a.index(b)]= ' '
        [print(i, end='') for i in d]; print('\n')
        if d != m:
            b = input('\nEnter a single latter: ')
            l += 1
    return 'Congratulation! you guess the word in ' + str(l)+' turns'
    
print(guess_letters())
