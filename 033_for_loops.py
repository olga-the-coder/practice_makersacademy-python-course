# for loop

for letter in ["a", "b", "c"]:
    print(letter)

print("")
# `range` more or less creates a list of the numbers from its first parameter to
# one below its last parameter. So: the numbers 0-9.

def print_number_in_range():
    for number in range (0, 10):
        print(number)

print_number_in_range()

# Compare this to the `while` version which does the same thing:
print("")

def print_numbers_in_range_with_a_while():
    number = 0
    while number < 10:
        print(number)
        number += 1

print_numbers_in_range_with_a_while()