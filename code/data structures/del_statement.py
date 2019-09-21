#!/usr/bin/env python3

alist = [1, 2, 3, 4, 5, 6, 7, 8]
print("Our list:", alist)

del alist[1]
print("Our list:", alist)

del alist[0:3]
print("Our list:", alist)

del alist[:]
print("Our list:", alist)

