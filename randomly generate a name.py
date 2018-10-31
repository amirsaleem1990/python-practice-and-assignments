
from random import choice as c
a = list('amir')
d = list('abcdefghijklmnopqrstuvwxyz')
count = int()
while True:
    b = list()
    for i in range(4):
        b.append(c(d))
    count += 1
    if b == list('amir'):
        print('after try {} times'.format(count))
        break
