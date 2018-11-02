
# 7.8
sandwich_orders = ['a sandwich', 'pastrami sendwich', 'b sandwich', 'c sandwich', 'pastrami sendwich', 'd sandwich', 'e sandwich', 'pastrami sendwich']
finished_sandwiches = list()
for i in sandwich_orders: print('i made your ' + i); finished_sandwiches.append(i)
[print('fineshed: '+i) for i in finished_sandwiches]


# 7.9
print('The deli was run out of pastrami sandwich')
while 'pastrami sendwich' in finished_sandwiches:
    finished_sandwiches.remove('pastrami sendwich')
print('\nfinished_sandwiches:\n', finished_sandwiches)


# 7.10
a = input('what\'s your dream vacation? ')
b = input('if you could visit one place in the word where you go? ')
print('\nwhat\'s your dream vacation?: \n\t' + a)
print('if you could visit one place in the word where you go? \n\t' + b)
