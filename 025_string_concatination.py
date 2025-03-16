# Concatenation means 'joining together'.

my_string = "Ant" + "eater"
print(my_string)

# However, this expression won't work. we need to explicitly convert the number to a string using the `str` function built-in to Python.
# my_string = "Forty" + 2

my_string = "Forty" + str(2)
print(my_string)

# There is another way to concatenate strings

my_name = "Kay"
print(f"Hello, {my_name}!")

print(f"Your name is {len(my_name)} characters long")

# f-strings are a form of what's called string interpolation.

# == Exercise One ==

print("")
print("Function: greet")

def greet(name):
    return f"Hello, {name}!"

print(greet("Crab"))



