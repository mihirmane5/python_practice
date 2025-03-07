"""
Given a list of integers, find the second smallest unique number in the list.
Example 0:
    Input: [5, 1, 2, 1, 3, 5, 2, 4]
    Output: 2

Example 1:
    Input: [7, 7, 7, 7]
    Output: None

Example 2:
    Input: [10, 20, 30, 40]
    Output: 20

Example 3:
    Input: [3, 1, 2, 2, 3, 1, 4, 5]
    Output: 2
"""

def second_smallest_unique(lst):
    unique_num = list(set(lst))

    if len(unique_num) < 2:                 # Step 1: Remove duplicates
        return None
    
    smallest = float('inf')                 # If only one unique number exists, no second smallest
    second_smallest = float('inf')

    for num in unique_num:
        if num < smallest:
            second_smallest = smallest      # Move previous smallest to second smallest
            smallest = num                  # Update the smallest
        elif num < second_smallest:
            second_smallest = num           # Update the second smallest
    return second_smallest

print("Testcase 1: [5, 1, 2, 1, 3, 5, 2, 4]\nOutput: ",second_smallest_unique([5, 1, 2, 1, 3, 5, 2, 4]))
print("Testcase 2: [7, 7, 7, 7]\nOutput: ",second_smallest_unique([7, 7, 7, 7]))
print("Testcase 3: [10, 20, 30, 40]\nOutput: ",second_smallest_unique([10, 20, 30, 40]))
print("Testcase 4: [3, 1, 2, 2, 3, 1, 4, 5]\nOutput: ",second_smallest_unique([3, 1, 2, 2, 3, 1, 4, 5]))