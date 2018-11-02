# 7.4
a = input('Enter pizza topping ')
while a != 'quit':
    print("you'll add that topping to your pizza")
    a = input('\nEnter pizza topping ')

# 7.5
a = float(input('Enter your age '))
while a > 0:
    if a < 3: print('The ticket is free!')
    elif 3 <= a < 12: print('The ticket is 10$')
    else: print('the ticket is 15$')        
    a = int(input('Enter your age '))
        
# 7.6
#7.4 v2

a = input('Enter pizza topping ')
b = 0
while a != 'quit' and b < 5:
    if len(a) > 10 : break
    b = b + 1
    print("you'll add " + a + " topping to your pizza")
    a = input('\nEnter pizza topping ')

#7.5 v2
m = 0
a = float(input('Enter your age '))
while a > 0 and m < 6:
    if a > 100: break
    if a < 3: print('The ticket is free!')
    elif 3 <= a < 12: print('The ticket is 10$')
    else: print('the ticket is 15$')
    m +=1
    a = int(input('Enter your age '))
        
# 7.7
b = True
while b:
    print('stop this loop by press CTRL-C')
