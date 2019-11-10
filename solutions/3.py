num = int(input())
num2 = num

if (num == 0):
    res = "0"
else:
    res = ""
    while num > 0:
        res += str(int(num % 8))
        num = int(num / 8)

    res = res[::-1]

print("Result: 0o", res, sep="")
print("Confirmation:", oct(num2)) # Use this to confirm your results
