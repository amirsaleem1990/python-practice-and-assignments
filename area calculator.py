# area calculator
a = True
while a:
    print('\n***************************\nWelcome to Area Calculator\n***************************')
    b = input('\nwhich shape you want to calulate? \n[sq]:\t for square\n[rec]:\t for rectriangle\n[cir]:\t for circle\n')
    if b == 'sq':
        d = int(input('\nEnter one side length: '))
        print('\nyour square has area of '+str(d * d)+' '+ c+'s')
    elif b == 'rec':
        e = input('\nEnter lenght and hight seperated by space eg: 22 77 ')
        g = e[:e.find(' ')]; h = e[e.find(' ') +1 :]
        print('\nyour rectriange has area of '+str(int(g)*int(h)))
    #elif b == 'cir':
        #f = input('\nEnter daya meter for your sircle: ')
        #pppppppppppppppppppppppppppppppppppppppppppppp
	#print('sorry.. yet not circle ready')
    else: continue
    i = input('\nAre you want to calculate once more? \n[y/n] ')
    if i == 'y': a = True
    else: a = False
        
        
