#  Function with 2 arguments, the full string and the separator
def convert_camel_case(string, sep):
    res = ""
    for char in string:
        if char.upper() == char:  # If it's an uppercase, add it lowered with the sep
            res += sep + char.lower()
        else:
            res += char  # Else add the same char
    return res

string = input()
print(convert_camel_case(string, "_"))  # Call the function and print its return value
