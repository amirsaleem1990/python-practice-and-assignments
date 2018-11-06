# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  a = []
  b = 0
  words.sort()
  for i in words:
      if i == 'x':
          a.extend([i])
  for ib in words:
      if ib == 'x':
          words.remove(ib)
  return a
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
print("# ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']")
