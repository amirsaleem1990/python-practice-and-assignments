def sort_last(tuples):
    output = sorted(tuples, key=lambda x: x[-1])
    return output
print(sort_last([(1, 3), (2, 1), (3, 2)]))
