# list.sort() vs sorted(list)

# the list.sort() method sorts the list in place, that is, it modifies the list itself
# without returning a new list object

# the sorted(list) function returns a new sorted list without modifying the original list

L = [1, 5, 3, 9, 8, 2, 4, 7, 6]
L_sorted = sorted(L)  # returns a new sorted list
print(L_sorted)
print(L)

L.sort()  # sorts the list in place without returning a new list
print(L)
