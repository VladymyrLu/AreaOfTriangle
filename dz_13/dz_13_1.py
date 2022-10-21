def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change([1,5,10,20,10]))



