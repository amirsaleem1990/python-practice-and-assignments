# Exercise #30 & 31 & 32
# http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
# http://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
# http://www.practicepython.org/exercise/2017/01/10/32-hangman.html

def pick_word():
    import random
    return random.choice([i.lower() for i in open('/home/hp/Desktop/Exercises from www.practivepython org/exercise_30_related file.txt', 'r').read().split()])

def guess_letters():
    print('\nWelcome to Hangman!\n')
    aa = pick_word(); a = [i for i in aa]
    m = aa[:]; l = 0; ss = list()
    d = ['_' for i in range(len(aa))]
    [print(i, end='') for i in d]; print('\n')
    while '_' in d and l < len(aa):
        if d != m:
            print(str(len(aa)-l) + ' turn(s) left')
            b = input('Enter a single latter: '); ss.append(b)
            if len(b) == 1 and b not in d and ss.count(b)==1:
                l +=1
                if b in aa:
                    for i in range(aa.count(b)):
                        d[aa.index(b)] = b; a[a.index(b)]= ' '
                [print(i, end='') for i in d]; print('\n')
            else: print('you entered this latter before.. plz enter onother latter..\n')
    if d == m:
        print('Congratulation! you guess the word in ' + str(l)+' turns\n[for restart the game type guess_letters()]')
    else: print('Game over!..... try again\(you wasnt seccesfully guessed the word (' + aa + ')')
    nn = input('Are you want to play this game one more time? \n[y/n] ')
    if nn== 'y': print(guess_letters())
    elif nn == 'n': return 'Take care.. bye bye'
    
print(guess_letters())

