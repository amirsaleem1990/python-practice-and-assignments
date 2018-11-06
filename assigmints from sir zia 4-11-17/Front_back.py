# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  c = round((len(a)+.1) / 2) #3
  d = round((len(b)+.1) / 2) #2
  e = len(a)//2 #2
  f = len(b)//2 #1
  return a[ :c] +b [ :d] + a[-e: ] +b [-f: ]
  
front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten', 'Donut')

##
##  print()
##  print ('front_back')
##  test(front_back('abcd', 'xy'), 'abxcdy')
##  test(front_back('abcde', 'xyz'), 'abcxydez')
##  test(front_back('Kitten', 'Donut'), 'KitDontenut')
