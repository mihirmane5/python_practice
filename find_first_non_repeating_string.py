"""
Given a sentence as input, find the first non-repeating string in a sentence.
Example 0:
    Input:
    sentence = "apple banana apple grape orange"
    Output = 'grape'

Example 1:
    Input:
    sentence = "dog cat dog fish cat bird"
    Output = 'fish'
"""

def find_unique_string(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        word_count[word] = word_count.get(word, 0)+1

    for word in words:
        if word_count[word] == 1:
            return word
    return None

print(find_unique_string("apple banana apple grape orange"))
print(find_unique_string("dog cat dog fish cat bird"))