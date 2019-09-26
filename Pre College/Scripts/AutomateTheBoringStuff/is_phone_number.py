def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# number needs to be unicoded for IDLE
num0 = u"442-555-1234"

# This works via Python3 on Solus Linux
num1 = "442-555-1234"

# This will return false
not_num = "12-13-2017"

print(is_phone_number(num0))
print(is_phone_number(num1))
print(is_phone_number(not_num))

# This will output:
# True
# True
# False
