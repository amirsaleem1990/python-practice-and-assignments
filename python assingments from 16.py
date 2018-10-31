'''
15. Write a Python function to create the HTML string with tags around
the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''
def add_tags(word, string):
    return '<'+word+'>'+string+'</'+word+'>'

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
#################
'''
16. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''
def insert_string_middle(a, string):
    return a[:len(a)//2]+string+a[len(a)//2:]

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
