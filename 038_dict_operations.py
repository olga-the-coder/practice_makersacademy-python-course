# Here's a great use for dictionaries: counting!
# For example, counting how many times each letter appears in a string.

# We can use a for loop to iterate over some items, and then use a dictionary to
# keep count of the items we've seen.

text = "the quick brush jumped over the lazy crab"

letter_counts = {}

for letter in text:
    if letter not in letter_counts:
        letter_counts[letter] = 1
    else:
        letter_counts[letter] += 1

print(letter_counts)

# @TASK: Complete this exercise.

print("")
print("Function: count_words_by_length")

# Write this function that counts the number of words by how many letters they
# have. For example:

# words:  ["hat", "cat", "I", "bird"]
# result: {3: 2, 1: 1, 4: 1}
# Since there are two words of length 3, etc.

def count_words_by_length(words):
    words_length_counts = {}
    for word in words:
        if len(word) not in words_length_counts:
            words_length_counts[len(word)] = 1
        else:
            words_length_counts[len(word)] += 1
    return words_length_counts

print(count_words_by_length(["hat", "cat", "I", "bird"]))
print(count_words_by_length(["four", "four", "four", "one"]))




