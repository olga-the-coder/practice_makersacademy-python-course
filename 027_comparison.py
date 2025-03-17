#"python comparison operators"

# Python equal operator
print("")
print("Function: a_is_equal_to_b")

def a_is_equal_to_b(a, b):
    return a == b

print(a_is_equal_to_b(1, 2))
print(a_is_equal_to_b("a", "a"))
print(a_is_equal_to_b(6, 6))

# == Exercise One ==

print("")
print("Function: a_is_less_than_b")

def a_is_less_than_b(a, b):
    return a < b

print(a_is_less_than_b(1, 2))
print(a_is_less_than_b(1, 1))
print(a_is_less_than_b(2, 1))

# == Exercise Two ==

print("")
print("Function: a_is_greater_than_b")

def a_is_greater_than_b(a, b):
    return a > b

print(a_is_greater_than_b(1, 2))
print(a_is_greater_than_b(1, 1))
print(a_is_greater_than_b(2, 1))

# == Exercise Three ==

print("")
print("Function: a_is_less_than_or_equal_to_b")

def a_is_less_than_or_equal_to_b(a, b):
    return a <= b

print(a_is_less_than_or_equal_to_b(1, 2))
print(a_is_less_than_or_equal_to_b(1, 1))
print(a_is_less_than_or_equal_to_b(2, 1))

# == Exercise Four ==

print("")
print("Function: a_is_greater_than_or_equal_to_b")

def a_is_greater_than_or_equal_to_b(a, b):
    return a >= b

print(a_is_greater_than_or_equal_to_b(1, 2))
print(a_is_greater_than_or_equal_to_b(1, 1))
print(a_is_greater_than_or_equal_to_b(2, 1))

# == Exercise Five ==

print("")
print("Function: a_is_not_equal_to_b")

def a_is_not_equal_to_b(a, b):
    return a != b

print(a_is_not_equal_to_b(1, 2))
print(a_is_not_equal_to_b(1, 1))
print(a_is_not_equal_to_b(2, 1))

# == Exercise Six ==

print("")
print("Function: a_is_within_b")

# May be a little tricky — search for "python check if string contains
# substring"

#Checking Python Substring in String using In Operator

def a_is_within_b(a, b):
    return a in b

print(a_is_within_b("e","hello"))
print(a_is_within_b("f","hello"))

# Check Python Substring in String using Find() method

def a_is_within_b_using_find_method(a, b):
    if (b.find(a) == -1):
        return False
    else:
        return True

print(a_is_within_b_using_find_method("e","hello"))
print(a_is_within_b_using_find_method("f","hello"))

# Check Python Substring in String using Split() method

def a_is_within_b_using_split_method(a, b):
    s = b.split()
    if a in s:
        return True
    else:
        return False

print(a_is_within_b_using_split_method("of","hello world of python"))
print(a_is_within_b_using_split_method("apple","hello world of python"))