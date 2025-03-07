"""
Given a list of integers, find the second largest unique number in the list.
Example 0:
    Input: [5, 1, 2, 1, 3, 5, 2, 4]
    Output: 4

Example 1:
    Input: [10, 20, 30, 40]
    Output: 30

Example 2:
    Input: [7, 7, 7, 7]
    Output: None

Example 3:
    Input: [9, 8, 10, 10, 8, 9, 7]
    Output: 9
"""

def second_largest_unique(lst):
    unique_num = list(set(lst))

    if len(unique_num) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')

    for num in unique_num:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest

print("Testcase 1: [5, 1, 2, 1, 3, 5, 2, 4]\nOutput: ",second_largest_unique([5, 1, 2, 1, 3, 5, 2, 4]))
print("Testcase 2: [10, 20, 30, 40]\nOutput: ",second_largest_unique([10, 20, 30, 40]))
print("Testcase 3: [7, 7, 7, 7]\nOutput: ",second_largest_unique([7, 7, 7, 7]))
print("Testcase 4: [9, 8, 10, 10, 8, 9, 7]\nOutput: ",second_largest_unique([9, 8, 10, 10, 8, 9, 7]))