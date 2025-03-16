# A string has a number of characters inside it in a particular order.

note = "The Most Perfect Crab"
print(note)

# We can access the first character like this:
print(note[0])

# And the last character like this:
print(note[-1])

# You can also get a 'slice' of the string like this:
# This gets the portion of the string between index 0 and 3: 'The'
print(note[0:3])


# == Exercise One ==

print("")
print("Function: get_first_letter")

def get_first_letter(the_str):
    return the_str[0]

print("get_first_letter('The king granted them')")
print(get_first_letter("The king granted them"))

# == Exercise Two ==

print("")
print("Function: get_last_letter")

def get_last_letter(the_str):
    return the_str[-1]

print("get_last_letter('The king granted them')")
print(get_last_letter("The king granted them"))

# == Exercise Three ==

print("")
print("Function: get_nth_letter")

def get_nth_letter(the_str, n):
    return the_str[n]

print("get_nth_letter('The king granted them',4)")
print(get_nth_letter("The king granted them", 4))

# == Exercise Four ==

print("")
print("Function: get_letters_between_four_and_eight")

def get_letters_between_four_and_eight(the_str):
    return the_str[4:8]

print("get_letters_between_four_and_eight('The king granted them')")
print(get_letters_between_four_and_eight("The king granted them"))

