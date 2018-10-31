import csv
file = open('mpg.csv')
mpg = list(csv.DictReader(file))

# 'manufacturer' k set
manufacturers = set(i['manufacturer'] for i in mpg)
####print(manufacturers); print('count of total manufactureres:  '+ str(len(manufacturers)))

# 'mode' k set
models = set(i['model'] for i in mpg)
####print('models verity:  ', end='')
####print(models)
# 'displ' k set
displ = set(i['displ'] for i in mpg)
####print('unique engine displacement in liters :', end=''); print(displ)

# 'year' k set
year = set(i['year'] for i in mpg)
####print('uniqe years :', end=''); print(year)
# 'cyl'  k set
cyl = set(i['cyl'] for i in mpg)
####print('unique cylinders: ',end=''); print(cyl)
# 'trans' k set
trans = set(i['trans'] for i in mpg)
####print('unique types of transmissions :', trans)
# 'drv' k set
drv = set(i['drv'] for i in mpg)
####print('# note: drv : f = front-wheel drive, r = rear wheel drive, 4 = 4wd')
####print('uniqeu drv\'s: ', drv)
# 'hwy'  k set
hwy = set(i['hwy'] for i in mpg)
####print('uniqe highway mpg: ', hwy)
# 'fl'  k set
fl = set(i['fl'] for i in mpg)
####print('# note: fl : fuel (e = ethanol E85, d = diesel, r = regular, p = premium, c = CNG)')
####print('unique fl\'s: ', fl)
# 'class'  k set
clas = set(i['class'] for i in mpg)
####print('uniqe classe\'s: ', clas)
#--------------------
# (hwy) k colum ka average leny k lye:
####print(sum(float(i['hwy']) for i in mpg)/len(mpg))

# srif wo cars chahyen jin ka model 1999 ho or manufacturer 'audi' ho:
z = list()
for i in mpg:
    if i['year'] == '1999' and i['manufacturer'] == 'audi':
        z.append(i[''])

# srif wo 10 cars chahyen jin ka cty mpg sab sy kam ho:
mm = sorted(set(int(i['cty']) for i in mpg))
zz = mm[:11] 
a = [i[''] for i in mpg for b in zz if str(b) == i['hwy']]
b = [i for i in mpg for b in a if i[''] == b]

# 'hwy' colum ka average chahye:
c = sum(float(i['hwy']) for i in mpg)/len(mpg)
####print(c)
d = set(i['cyl']for i in mpg)
'''
Here's a more complex example where we are grouping the cars by
number of cylinder, and finding the average cty mpg for each
group.
'''
final = list() 
for a in cyl:
    summ = 0; counter = 0
    for b in mpg:
        if b['cyl'] == a: summ += float(b['cty']); counter += 1
    final.append((a, summ/counter))
(print(i) for i in final)














