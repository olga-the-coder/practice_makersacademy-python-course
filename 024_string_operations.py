# == Length ==

length = len("Hello")
print(f"The string is {length} characters long.")

# == Replace ==

old_string = "Hello, YOUR_NAME!"
new_string = old_string.replace("YOUR_NAME", "Kay")
print(new_string)

#len(my_string)               <-- Independent Function
#my_string.replace("h", "w")  <-- Method Function

# == Upper and Lowercase ==

# @TASK Complete these exercises:

# == Exercise One ==

print("")
print("Function: uppercase")

def make_uppercase(string):
    return string.upper()

print(make_uppercase("Hello"))

# == Exercise Two ==

print("")
print("Function: lowercase")

def make_lowercase(string):
    return string.lower()

print(make_lowercase("HelLo"))

# == Exercise Three ==

#.strip() method to remove whitespace and characters from the beginning and the end of a string.
#.lstrip() method to remove whitespace and characters only from the beginning of a string.
#.rstrip() method to remove whitespace and characters
#greeting.strip("H?")  remove "H" and "?", which are at the beginning and at end of the string, respectively.


print("")
print("Function: strip_whitespace")

def strip_whitespace(string):
    return string.strip()

print(strip_whitespace(" hello world "))
print("")

