# Exercise # 20
def element_search(lst, number):
    while len(lst)>1:
        if lst[len(lst)//2] > number: lst = lst[: len(lst)//2]; print(lst)
        else: lst = lst[len(lst)//2:]; print(lst)
    if number in lst: print('your number in the list')
    else: print('your number not in your list')

a = [2, 3, 5, 8, 9, 11, 14,15, 16, 20, 22, 25, 29, 34, 45]

