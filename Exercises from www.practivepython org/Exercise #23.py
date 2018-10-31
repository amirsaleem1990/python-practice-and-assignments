# Exercise #23
# http://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
'''
Given two .txt files that have lists of numbers in them, find the numbers that are
overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt
file has a list of happy numbers up to 1000.
(If you forgot, prime numbers are numbers that can’t be divided by any other number. And
yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The
explanation is easier with an example, which I will describe below.)
'''
def file_ovelap(file1, file2):
    a = [i for i in open(file1, 'r').read().split()]; b = [m for m in open(file2, 'r').read().split()]
    [print(z, end=' ') for z in a if z in b]; return ''
     
a = ('/home/hp/Desktop/Exercises from www.practivepython org/exercise_23_related file_1.txt')
b = ('/home/hp/Desktop/Exercises from www.practivepython org/exercise_23_related file_2.txt')

print(file_ovelap(a, b))
