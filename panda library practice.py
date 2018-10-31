import pandas as pd

a = pd.Series(list('amirsaleem'))
#print('a: '); print(a)
###########
b = {'name' : 'amir'.title(),
     'age' : 27,
     'gender' : 'male',
     'status' : 'married',
     's' : 'male'}
c = pd.Series(b)
#print(c)

d = pd.Series(b, index=['n', 'a', 'g', 's', 'ss'])
#print(d)
e = pd.Series(list('amirsaleem'), index = [i for i in range(10,20)])
#print(e)
f = pd.Series(b, index = ['name', 'gender'])
#print(f)
g = pd.Series(b, index = ['name', 'gender', 'height'])
#print(g)
h = pd.Series([float(i) for i in range(34, 41)])
#print(h)
i = dict()
for a in range(323, 329):
    i[float(a)] = chr(a)
j = pd.Series(i)
#print(j[0]) # Error
#print(j.iloc[0]) # ok
k = pd.Series([float(i) for i in range(22, 28)])
#print(s[k])
# makhsoos elements leny k lye dict ki tarah.
l = pd.Series(i, index = [323.0, 325.0])
###
m = pd.Series([100.00, 120.00, 101.00, 3.00])

total = 0
for item in m: total += item
#print(total)
# opar or neechy waly dono 1 hi kaam kar rahy hen.. magar neechy wala zyada
# fast h.
import numpy as np
total = np.sum(m)
# ab ham is ko check karen gy k aakhri wala waqai pehly waly sy fast h?
n = pd.Series(np.random.randint(0,1000,10000))
print(n.head(), len(n))
