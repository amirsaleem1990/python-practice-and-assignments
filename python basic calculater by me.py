# basic calculater
e = True
while e:
    a = input('what you want? \n[add]:\t for addition\n[multi]: for multiplication\n[sub]:\t for substraction\n[div]:\t for division\n')
    if a in ['add', 'multi', 'sub', 'div':
        d = input('[Enter 2 numbuers with space. eg: 43 9]\n')
        b = int(d[:d.find(' ')]); c = int(d[d.find(' ')+1:])
        if a.lower() == 'add': print(str(b)+' + '+str(c)+' = '+ str (b+c))
        elif a.lower() == 'multi': print(str(b)+' * '+str(c)+' = '+ str (b*c))
        elif a.lower() == 'sub': print(str(b)+' - '+str(c)+' = '+ str (b-c))
        elif a.lower() == 'div': print(str(b)+' / '+str(c)+' = '+ str (b/c))
        else: print('your choice not it our list.. plz choose correctly')
        f = input('\nAre you want another calculation?\n[y = Yes, anykey = No] ')
        if f.lower() == 'y': e = True
        else: e = False; print('Thank\'s for using our calculator. Take care.. bye bye')
