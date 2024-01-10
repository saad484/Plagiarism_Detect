from collections import Counter

# Example vector represented as a list
# my_vector = [1, 2, 3, 1, 2, 1, 4, 5, 3, 2, 1]

# # Using Counter to count occurrences
# counter_obj = Counter(my_vector)

# # Accessing counts
# print(counter_obj)
# # Output: Counter({1: 4, 2: 3, 3: 2, 4: 1, 5: 1})

# # Accessing count of a specific element
# print(counter_obj[1])
# Output: 4



# Counter class is part of the Python standard library, specifically in the collections module

# Example list of words
word_list = ["apple", "banana", "orange", "apple", "banana", "apple", "grape", "kiwi", "orange", "banana"]

# Using Counter to count word occurrences
word_counter = Counter(word_list)

# Accessing and printing word and count pairs
for word, count in word_counter.items():
    print(f'The word "{word}" appears {count} times.')
