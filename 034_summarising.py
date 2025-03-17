lines = [
  "My King,",
  "I need another five years.",
  "Then your crab will be ready.",
  "Sincerely,",
  "Chuang-tzu"
]

text = "" # This is called the accumulator variable

for line in lines:
    text = text + line
    text = text + "\n"

print(text)

# join() function

another_text = "\n".join(lines)
print(another_text)

# @TASK: Complete this exercise

print("")
print("Function: add_up_numbers")

# Add up all the numbers in the list
def add_up_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number

    print(sum)

add_up_numbers([1, 2, 3, 4])
add_up_numbers([2, 3, 4, 5])