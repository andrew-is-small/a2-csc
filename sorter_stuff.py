def sortfunction(a):
    # bigger a is first
    return 100 - a


lst = [1, 3, 4, 2, 6, 5]
print(sorted(lst, key=sortfunction))
