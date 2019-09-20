#!/bin/python

alist = [1, 2]
print("Our list:", alist)

# Appends an element to the end of the list
alist.append(5)
print("Our list:", alist)

# Appends all the elements in 'anotherlist' to 'alist'
anotherlist = [3, 4]
alist.extend(anotherlist)
print("Our list:", alist)

# Inserts an item, x, at a given position, i, in a list (list.inser(i,x))
alist.insert(1, 9)
print("Our List:", alist)

# Removes the first item from the list with value x (list.remove(x))
alist.remove(9)
print("Our List:", alist)

# Remove and return an item from a list at a given position, i
# If no argument is given, remove and return the last element from the list
alist.pop(1)
print("Our List:", alist)

# Return the index of the first item with value x in the list
print("Our List:", alist.index(1))

