# Exercise #15
# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
'''
Write a program (using functions!) that asks the user for a long string containing
multiple words. Print back to the user the same string, except with the words in
backwards order. For example, say I type the string:

My name is Michele

Then I would see the string:

Michele is name My

shown back to me.
'''
def reverse_word_order_v2(a):
    b = [i for i in a.split()]; b.reverse()
    return b

'''
def reverse_word_order(a):
    b = str()
    for i in a.split():
        b = i+ ' ' + b
    return b

'''
print(reverse_word_order_v2('my name is amir saleem'))
