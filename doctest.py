def f(x1):
    '''
    >>> f(2)
    4
    >>> f(3)
    6
    >>> f(9)
    17
    >>> f(7)
    14
    '''
    return x1 * 2


import doctest
print(doctest.testmod())
