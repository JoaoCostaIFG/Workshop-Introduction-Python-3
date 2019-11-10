names = input().split()

name = ""
if len(names) == 1:
    name = names[0]
else:
    name = names[0]

    for i in range(1, len(names) - 1):
        if names[i].capitalize() == names[i]:
            name += " " + names[i][0] + "."

    name += " " + names[-1]

print(name)
