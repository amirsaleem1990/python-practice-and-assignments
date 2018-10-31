# Exercise #16
# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
'''
Write a password generator in Python. Be creative with how you generate passwords - strong
passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The
passwords should be random, generating a new password every time the user asks for a new
password. Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word
or two from a list.

'''
def password_generator_v1():
    a = input('how strong you want your password to be? \n[week/normal/strong] ')
    import string
    import random
    n = string.ascii_letters+string.digits
    if a == 'week': [print(random.choice(n),end='') for i in range(2)]; return ' '
    elif a == 'normal': [print(random.choice(n),end='') for i in range(5)]; return ' '
    elif a == 'strong': [print(random.choice(n),end='') for i in range(8)]; return ' '    
    
'''
def password_generator()_v2:
    a = input('how strong you want your password to be? \n[week/normal/strong] ')
    import string
    import random
    n = [chr(i) for i in range(34, 127)]
    if a == 'week':
        d = [''.join(random.choice(string.ascii_letters)) for i in range(2)]
        [print(i,end='') for i in d]
    elif a == 'normal':
        d =  [random.choice(string.ascii_letters) for i in range(6)]
        [print(''.join(i).upper(),end='') for i in d]
    elif a == 'strong':
        d = [random.choice(n) for i in range(10)]
        [print(''.join(i).upper(), end='') for i in d]
        
'''
print(password_generator_v1())
