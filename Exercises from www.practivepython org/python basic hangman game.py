# Exercise #30 & 31 & 32
'''
def pick_word():
    return random.choice([i.lower() for i in open('/home/hp/Desktop/Exercises from www.practivepython org/exercise_30_related file.txt', 'r').read().split()])
'''
def guess_letters():
    import random
    print('\nWelcome to Hangman!\n')
    ll = int(input('how long word you wish to guess? '))
    a = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(ll)] 
    m = a[:]; l = 0; ss = list()
    d = ['_' for i in range(len(a))]
    [print(i, end='') for i in d]; print('\n')
    while '_' in d and l < ll:
        if d != m:
            print(str(ll-l) + ' turn(s) left')
            b = input('Enter a single latter: '); ss.append(b)
            if len(b) == 1 and b not in d and ss.count(b)==1:
                l +=1
                if b in a:
                    for i in range(a.count(b)):
                        d[a.index(b)] = b; a[a.index(b)]= ' '
                [print(i, end='') for i in d]; print('\n')
            else: print('you entered this latter before.. plz enter onother latter..\n')
    if d == m:
        return 'Congratulation! you guess the word in ' + str(l)+' turns\n[for restart the game type guess_letters()]'
    else: return'Game over!..... try again\n'
print(guess_letters())
nn = input('Are you want to play this game one more time? \n[y/n] ')
while nn== 'y': print(guess_letters())
if nn == 'n': print('Take care.. by by')
