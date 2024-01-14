# here an example of comman words

vec1 = {'apple': 3, 'banana': 2, 'orange': 1}
vec2 = {'apple': 1, 'banana': 4, 'grape': 2}

# After Step 1, intersection = {'apple', 'banana'}
# After Step 2, matchWords = {'apple': 1, 'banana': 2}

# Find the common words between the two sets

print(f'Keys of vec1: {vec1.keys()}') # returns view object
print(f'Keys of vec2: {vec2.keys()}') # returns view object

# here we convert them to a list

# vec1
keys_list1 = set(vec1.keys())
print(keys_list1)
# vec2
keys_list2 = set(vec2.keys())
print(keys_list2)

# reminder sets doesn't accept duplicates that's why we're using them!


common_words = keys_list1 & keys_list2
print("Common words:", common_words)

