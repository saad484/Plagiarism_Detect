import re

# Define the regular expression pattern
WORD = re.compile(r'\w+')

# Example string
text = "This is an example sentence with some words."

# Use the regular expression to find all words in the string
matches = WORD.findall(text)

# Print the matched words
print(matches)