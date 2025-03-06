"""
Given a string as input, find the first non-repeating character in a string.
Example 0:
    Input:
    str = "swiss"
    Output = 'w'                    (since s repeats, but w is first unique character)

Example 1:
    Input:
    str = "aabbccde"
    Output = "d"                    (since a, b, c repeat, but d is the first unique character)
"""

def find_first_unique(str):
    char_count = {}

    for char in str:
        char_count[char] = char_count.get(char, 0)+1
    
    for char in str:
        if char_count[char] == 1:
            return char
    return None

print(find_first_unique("swiss"))
print(find_first_unique("aabbccde"))