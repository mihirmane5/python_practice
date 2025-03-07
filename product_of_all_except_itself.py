"""
Given a list of numbers, replace each number with its product of all the numbers in the list except itself.

Example 0:
    Input: [1, 2, 3, 4]
    Output: [24, 12, 8, 6]      for ->[1 = 2*3*4, 2 = 1*3*4, 3 = 1*2*4, 4 = 1*2*3]

Example 0:
    Input: [5, 6, 7]
    Output: [42, 35, 30]      for ->[5 = 6*7, 6 = 5*7, 7 = 5*6]
"""

def product_except_itself(lst):
    total_product = 1
    for num in lst:
        total_product *= num
    
    result = []

    for num in lst:
        result.append(total_product // num)
    return result

print("Testcase 1: [1, 2, 3, 4]\nOutput: ",product_except_itself([1, 2, 3, 4]))
print("\nTestcase 2: [5, 6, 7]\nOutput: ",product_except_itself([5, 6, 7]))
print("\nTestcase 3: [2, 5, 8, 6]\nOutput: ",product_except_itself([2, 5, 8, 6]))