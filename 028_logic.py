# Operators like `or` are called 'logical' or 'Boolean' operators.
# That `or` operator says "evaluate to true if the condition on the left, or on
# the right, or both evaluate to true".

def starts_wit_x_or_y(the_str):
    first_letter = the_str[0]
    if first_letter == 'x' or first_letter == 'y':
        return "It does!"
    else:
        return "It does not"

print(starts_wit_x_or_y("hello world"))
print(starts_wit_x_or_y("Yes Sir"))
print(starts_wit_x_or_y("yellow ball"))

# Operator 'or' returns True if one of the statements is true

print("")
print("Function: a_or_b")

def a_or_b(a, b):
  return a or b

print(a_or_b(True, True))
print(a_or_b(True, False))
print(a_or_b(False, True))
print(a_or_b(False, False))

# Operator 'and' returns True if both statements are true

print("")
print("Function: a_and_b")

def a_and_b(a, b):
  return a and b

print(a_and_b(True, True))
print(a_and_b(True, False))
print(a_and_b(False, True))
print(a_and_b(False, False))

# Operator 'not' Reverse the result, returns False if the result is true    not(x < 5 and x < 10)

print("")
print("Function: not_a")

def not_a(a):
  return not a

print(not_a(True))
print(not_a(False))

