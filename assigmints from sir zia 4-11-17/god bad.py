a = 'i m amir not good bad saleem'
b = a.find('amir')
c = a.find('saleem')
d = c + 6
a = a.replace(a[b:d], 'changed')
