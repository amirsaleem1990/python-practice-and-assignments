# python crash course Exercise
'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and
the text of a message that should be printed on the shirt The function
should print a sentence summarizing the size of the shirt and the message
printed on it Call the function once using positional arguments to make a
shirt Call the function a second time using keyword arguments.
'''
def make_shirt(size, message):
    return 'your shirt size is {}. we print on your shirt this massage: {}'.format(size, message)
print(make_shirt('medium', 'amir saleem'))
print(make_shirt(message = 'amir saleem', size = 'small'))
##################################################
'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are
large by default with a message that reads I love Python Make a large
shirt and a medium shirt with the default message, and a shirt of any size
with a different message.
'''
def make_shirt(size = 'large', message = 'I love python Make a large shirt'):
    return 'your shirt size is {}. we print on your shirt this massage: {}'.format(size, message)

print(make_shirt())





'''
8-5. Cities: Write a function called describe_city() that accepts the name
of a city and its country The function should print a simple sentence,
such as Reykjavik is in Iceland Give the parameter for the country a
default value Call your function for three different cities, at least one
of which is not in the default country.
'''
def describe_city(name, country = 'pakistan'):
    return name + ' in ' + country
print(describe_city('karachi'))
print(describe_city('dehli', 'india'))
print(describe_city('lahore'))
