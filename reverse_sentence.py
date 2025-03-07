"""
Reverse the words in the given sentence without reversing the characters in each word.
Example 0:
    Input: "Hello world this is Python"
    Output: "Python is this world Hello"

Example 1:
    Input: "Keep learning everyday and implement it on daily basis"
    Output: "basis daily on it implement and everyday learning Keep"
"""

def reverse_word(sentence):
    words = sentence.split()

    reversed_words = words[::-1]
    return " ".join(reversed_words)

print("Testcase 1: Hello world this is Python\nOutput: ",reverse_word("Hello world this is Python"))
print("\nTestcase 2: Keep learning everyday and implement it on daily basis\nOutput: ",reverse_word("Keep learning everyday and implement it on daily basis"))