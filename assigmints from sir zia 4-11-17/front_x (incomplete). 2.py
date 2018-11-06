def front_x(words):
  a = []
  b = []
  words.sort()
  for i in words:
      if i[0] == 'x':
          a.extend([i])
  for ib in a:
      if ib in a:
          words.remove(ib)
  return a + words
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

