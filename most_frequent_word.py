"""
Given a sentence as input, find the most frequent word in a sentence.
Example 0:
    Input:
    sentence = "apple banana apple grape banana orange apple"
    Output = 'apple'            (appears 3 times, the most)

Example 1:
    Input:
    sentence = "dog cat dog fish cat dog"
    Output = 'dog'              (appears 3 times, the most)
"""
def most_frequent_word(sentence):
    word_count = {}
    words = sentence.split()
    max_word = None
    max_count = 0

    for word in words:
        word_count[word] = word_count.get(word, 0)+1

        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word
    return max_word

print(most_frequent_word("apple banana apple grape banana orange apple"))
print(most_frequent_word("dog cat dog fish cat dog"))