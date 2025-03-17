words = ['I', 'need', 'another', 'five', 'years']

first_letters = [] # This is our accumulator again

for word in words:
    first_letter = word[0]
    first_letters.append(first_letter)

print(first_letters)
print(words)


# @TASK: Complete this exercise.

print("")
print("Function: add_one_hundred_to_numbers")

# Return a new list of each number with 100 added
def add_one_hundred_to_numbers(numbers):
    new_numbers = []
    for number in numbers:
        number = number + 100
        new_numbers.append(number)
    return new_numbers

print(add_one_hundred_to_numbers([1, 2, 3, 4]))
print(add_one_hundred_to_numbers([2, 3, 4, 5]))