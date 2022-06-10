def right_justify(s):
    """Adjusts last character of string to column 70;
    s == string object"""
    spaces = " "; rt_side = 70 - len(s); new_s = str((spaces * rt_side) + s)
    return new_s

print(right_justify("Test")); print(right_justify("Test again"))
# Error code: print(right_justify(22))