def is_anagram(s1, s2):
    L1 = []
    for i in range(len(s1)):
        L1.append(i)
    L2 = []
    for i in range(len(s2)):
        L2.append(i)
    L1.sort
    L2.sort
    if L1 == L2:
        return True
    else:
        return False

print(is_anagram("silent", "listen"))
print(is_anagram("bear", "breach"))

