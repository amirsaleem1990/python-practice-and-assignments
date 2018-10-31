# Exercise #13
# 
'''
Write a program that asks the user how many Fibonnaci numbers to generate and then
generates them. Take this opportunity to think about how you can use functions. Make sure
to ask the user to enter the number of numbers in the sequence to generate.(Hint: The
Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the
sum of the previous two numbers in the sequence. The sequence looks like this:
1, 1, 2, 3, 5, 8, 13, …)
'''
def fibonacci():
    a = input('Enter sequence of 2 fibonacci numbers[e.g: 5,8] ')
    m = int(input('how many long range your need to genrate? '))
    b = int(a[:a.index(',')]); c = int(a[1+a.index(','): ]);  z = [b, c]
    [z.append((z[-1])+(z[-2]))for i in range(m)]
    return z
print(fibonacci())
