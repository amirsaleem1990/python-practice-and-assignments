
name = ['a', 'b', 'c', 'd', 'e', 'f']
age = [28, 27, 25, 23, 21, 19]
status = ['married', 'married', 'married', 'single', 'single', 'single']
children = [2, 1, 2, 0, 0, 0]
dic = {}

for i in range(len(name)):
    dic[name[i]] = [age[i], status[i], children[i]]
print(dic)

############
students = {
    'a' : {'age': 28, 'status': 'married', 'children':2},
    'b' : {'age': 27, 'status': 'married', 'children':1},
    'c' : {'age': 25, 'status': 'married', 'children':2},
    'd' : {'age': 23, 'status': 'single', 'children':0},
    'e' : {'age': 21, 'status': 'single', 'children':0},
    'f' : {'age': 19, 'status': 'single', 'children':0}
    }

name = []
age = []
status = []
children = []
for i in students:
	name.append(i)
	age.append(students[i]['age'])
	status.append(students[i]['status'])
	children.append(students[i]['children'])
print(name, age, status, children)
##########

for i in students:
    if 'married' in students[i]. values():
	    print(i, students[i])
