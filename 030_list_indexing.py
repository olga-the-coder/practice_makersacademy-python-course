my_list = [44, 35, 21, 63]
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])

# == Exercise One ==

print("")
print("Function: get_first_item")

def get_first_item(the_list):
    return the_list[0]

print(get_first_item(["a", "b", "c", "d", "e"]))
print(get_first_item([34, 44, 54, 64]))

# == Exercise Two ==

print("")
print("Function: get_last_item")

def get_last_item(the_list):
    return the_list[-1]

print(get_last_item(["a", "b", "c", "d", "e"]))
print(get_last_item([34, 44, 54, 64]))

# == Exercise Three ==

print("")
print("Function: get_nth_item")

def get_nth_item(the_list, n):
    return the_list[n]

print(get_nth_item([34, 44, 54, 64], 1))
print(get_nth_item(["a", "b", "c", "d", "e"], 3))

# == Exercise Four ==

print("")
print("Function: get_items_between_one_and_three")

def get_items_between_one_and_three(the_list):
    return the_list[1:3]

print(get_items_between_one_and_three([34, 44, 54, 64]))
print(get_items_between_one_and_three(["a", "b", "c", "d", "e"]))
