example_numbers = [1, 2, 3, -2, -2, 2, None, -3, 4, 4, None, 3, 3, 2, 2, 1]

# Desired output:
# 1: xx
# 2: xxxxxx
# 3: xxxx
# 4: xx


def generate_frequency_graph(numbers):
  integers = get_only_integers(numbers)
  positive_integers = convert_negatives_to_positives(integers)
  number_frequency = calc_frequency_of_numbers(positive_integers)
  graph = format_graph(number_frequency)
  return graph

def get_only_integers(numbers):
    integers = []
    for number in numbers:
        if number != None:
            integers.append(number)
    return integers


def convert_negatives_to_positives(integers):
    positive_integers = []
    for integer in integers:
        if integer < 0:
            positive_integers.append(integer * -1)
        else:
            positive_integers.append(integer)
    return positive_integers

def calc_frequency_of_numbers(positive_integers):
    number_frequency = {}
    for integer in positive_integers:
        if integer not in number_frequency:
            number_frequency[integer] = 1
        else:
            number_frequency[integer] += 1
    return number_frequency

def format_graph(number_frequency):
    graph = ""
    for integer in number_frequency:
        graph = graph + f"{integer}: {number_frequency[integer] * 'x'}\n"
    return graph

print(generate_frequency_graph(example_numbers))