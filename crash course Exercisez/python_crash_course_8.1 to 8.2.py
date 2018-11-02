# python crash course exercise
'''
try It your self
8-1. Message: Write a function called display_message() that prints one
sentence telling everyone what you are learning about in this chapter
Call the function, and make sure the message displays correctly
'''
def display_message():
    return 'what you are learning about in this chapter? '

print(display_message())

#############################################
'''
8-2. Favorite Book: Write a function called favorite_book() that accepts
one parameter, title The function should print a message, such as One of
my favorite books is Alice in Wonderland Call the function, making sure
to include a book title as an argument in the function call
'''
def favorite_book(title):
    return 'One of my favorite books is {}'.format(title)
print(favorite_book('quran'))

#############################################
