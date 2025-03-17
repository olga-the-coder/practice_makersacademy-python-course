# `while` loop

i = 0
while i < 10:
    print(f"The number is now {i}")
    i = i + 1

# @TASK: Here's an exercise where you can put it into practice:

print("")
print("Function: add_cats_repeatedly")

def add_cats_repeatedly(word_list, count):
    i = 1
    while i <= count:
        word_list.append("cats")
        i = i + 1
    return word_list

print(add_cats_repeatedly([], 3))
print(add_cats_repeatedly(['dogs'], 2))


