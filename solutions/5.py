def convert_camel_case(string, sep):
    res = ""
    for char in string:
        if char.upper() == char:
            res += sep + char.lower()
        else:
            res += char
    return res

string = input()
print(convert_camel_case(string, "_"))
