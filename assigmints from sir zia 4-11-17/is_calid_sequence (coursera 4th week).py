def is_valid_sequence(x1):
    '''
    (str) -> True or False
    return a True if argume
    is_valid_sequence('AGT')
    True
    is_valid_sequence('atg')
    False
    is_valid_sequence('ATGM')
    True
    is_valid_sequence('ATGCCCCTG')
    True
    '''
    
    a = []
    b = 'ATGC'
    for c in x1:
        if c not in b:
            a.extend(c)
    if len(a) == 0:
        return True
    else:
        return False
    
