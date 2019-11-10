# a)
num = int(input())

alist = []
for i in range(num):
    read = input().split()
    alist.append( (read[0], float(read[1])) )

print("a)", alist[-1])

# b)
def sorting_key(t):
    return t[1]

sorted_list = sorted(alist, key=sorting_key)

print("b)", sorted_list[-1])
