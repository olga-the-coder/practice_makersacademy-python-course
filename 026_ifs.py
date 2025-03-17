# Programs often have to make decisions based on their input. For this, we use
# the `if` keyword.

leaves_on_the_tree = 0
#leaves_on_the_tree = 5

if leaves_on_the_tree == 0:
    print("It must be winter - or a dead tree")
else:
    print("This is a happy tree with nice leaves")


# == Exercise One ==

print("")
print("Function: is_first_of_the_month")

def is_first_of_the_month(day_number):
    if day_number == 1:
        print("First of the month!")
    else:
        print("Not first of the month")

is_first_of_the_month(1)
is_first_of_the_month(12)

# == Exercise Two ==

print("")
print("Function: has_five_chars")

def has_five_chars(the_str):
    if len(the_str) == 5:
        print(f"{the_str} is five characters long")
    else:
        print("Not five characters")

has_five_chars("ABCDE")
has_five_chars("Nope")
has_five_chars("Nor this one")