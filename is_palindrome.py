def is_palindrome_v1(s):
    ''' (str) -> bool
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('danted')
    False
    '''
    d = [i for i in s]
    d.reverse()
    return d == [m for m in s]
