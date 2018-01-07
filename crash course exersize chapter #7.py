# 7.4
a = input("Enter pizza topping: \n(type 'quit' to Exit this program) ")
while a != 'quit':
    print("** you was done the (" + a + ") topping to your pizza**")
    a = input("\nEnter pizza topping: \n(type 'quit' to Exit this program) ")

# 7.5
a = float(input('Enter your age: '))
while a > 0:
    if a < 3: print('The ticket is free!')
    elif 3 <= a < 12: print('The ticket is 10$')
    else: print('The ticket is 15$')        
    a = float(input('\nEnter your age: '))
    
#7.6
#7.4 v2
a = input("Enter pizza topping(single word without space) : \n(type 'quit' to Exit this program) ")
b = 0
while a != 'quit' and b < 5:
    if ' ' in a: break
    b = b + 1
    print("you was done the (" + a + ") topping to your pizza")
    a = input("\nPlz Enter another topping(single word without space): \n(type 'quit' to Exit from program) ")

#7.6
#7.5 v2
active = True
while active:
    a = int(input('\nPlease Enter your age:\n(if you are above 50 you not allowed to buy a ticket) ')) 
    if a < 3: print('The ticket is free!')
    elif 3 <= a < 12: print('The ticket is 10$')
    elif a < 51: print('the ticket is 15$')
    else: print('you are above 50.. you not allowed to buy a ticket'); active = False
    
    

# 7.7
b = True
while b: print('stop this loop by press "CTRL+C"')

