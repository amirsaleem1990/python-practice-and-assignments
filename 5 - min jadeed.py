"""Wordcount exercise
Python class
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...
Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that"s fine). Store all the words as lowercase,
so "The" and "the" count as the same word.
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
Use str.split() (no arguments) to split on all whitespace.
Workflow: don"t build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that"s working, try for the next milestone.
Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""
from collections import Counter as c
import sys
filename = ('new')
f = filename

def file_to_list(filename):
    return [i.lower() for i in open(filename, 'r').read().split()]
def print_words(filename):
    a = file_to_list(filename)
    b = sorted(list(set(a)))
    [print(i, a.count(i)) for i in b]
def print_top(filename):
    a = (c(file_to_list(filename)).most_common(20))
    [print(i[0], i[1]) for i in a]

def main():
  if len(sys.argv) != 3:
    print("usage: ./wordcount.py {--count | --topcount} file")
    sys.exit(1)
  option = sys.argv[1]
  filename = sys.argv[2]
  if option == "--count":
    print_words(filename)
  elif option == "--topcount":
    print_top(filename)
  else:
    print("unknown option: " + str(option))
    sys.exit(1)

if __name__ == "__main__":
    print_top('new')
