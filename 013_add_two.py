
# @TASK: Write a function called `add_two` that:
#
# * Takes a number as input
# * Adds two to it
# * Returns the result

print("Function: add_two")

def add_two(num1, num2):
    return num1 + num2

#Test function and display the result
num1 = 5
num2 = 6

print(f'Sum of {num1} and {num2} is equal to {add_two(num1, num2)}.')