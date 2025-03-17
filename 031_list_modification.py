my_list = ["a", "b", "c"]
my_list.append("d")
print(my_list)

# The behaviour of append is to modify the list 'in-place'. Don't worry too much
# about this right now. If you have any trouble with it, you can always create a
# new list by using the `copy` method.

my_list = ["a", "b", "c"]
my_copy = my_list.copy()
my_copy.append("d")
print(my_list)
print(my_copy)

print("")
print("Function: append_item_to_list")

def append_item_to_list(the_list, item):
    the_list.append(item)
    return the_list

print(append_item_to_list(['a', 'b'], 'c'))
print(append_item_to_list([3, 1], 6))

# == Exercise One ==

print("")
print("Function: remove_item_from_list")

def remove_item_from_list(the_list, item):
    the_list.remove(item)
    return the_list

print(remove_item_from_list(['a', 'b'], 'b'))
print(remove_item_from_list([1, 3], 3))

# == Exercise Two ==

print("")
print("Function: count_items_in_list")

def count_items_in_list(the_list, item):
    return the_list.count(item)

print(count_items_in_list(['a', 'b', 'a'], 'a'))
print(count_items_in_list([4, 1, 4, 4], 4))

# == Exercise Three ==

print("")
print("Function: get_index_of_item")

def get_index_of_item(the_list, item):
    return the_list.index(item)

print(get_index_of_item(['a', 'b', 'c'], 'b'))
print(get_index_of_item([33, 44, 55], 55))

# == Exercise Four ==

print("")
print("Function: reverse_list")

def reverse_list(the_list):
    return list(reversed(the_list))

print(reverse_list(['a', 'b', 'c']))
print(reverse_list([33, 44, 55]))

# == Exercise Five ==

print("")
print("Function: list_length")

# Note — it's the same as for strings!
def list_length(the_list):
    return len(the_list)

print(list_length(['a', 'b', 'c']))
print(list_length([33, 44]))

