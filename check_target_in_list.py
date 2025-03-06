"""
Given a list of 'n' numbers, write a function to check if a target number exists in the list.
Example 0:
    Input:
    arr = [1, 3, 7, 9, 2]
    target = 11
    Output:
    True

Example 1:
    Input:
    arr = [2, 5, 7, 8, 9, 0, 1]
    target = 17
"""

def find_target(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return True
        seen.add(num)
    return False

print(find_target([1, 3, 7, 9, 2], 11))
print(find_target([2, 5, 7, 8, 9, 0, 1], 17))