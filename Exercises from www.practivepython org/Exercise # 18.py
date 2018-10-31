# Exercise # 18
import random
cow = list()
bull = list()
count = int()
c = [random.choice('1234567890') for i in range(4)]
while len(cow) < 4:
    a = input('\nguess a four(4) digit number: ')
    for i in range(4):
        if a[i] == c[i]: cow.append('cow')
        elif a[i] in c: bull.append('bull')
    print(str(len(cow))+' Cow', str(len(bull)) + ' Bull')
    count += 1
    print(c)
print('\n(you gess the correct number in ' + str(count) + ' tries)')
