"""
LeetCode Link: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
Problem Name: Leaders in an Array
Description: Find all elements that are greater than all elements to their right.

Folder: Arrays
File: 084_Leaders_in_an_Array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Scan from right to left, tracking maximum element seen so far.
# Time Complexity: O(N)
# Space Complexity: O(1) auxiliary (excluding result)
def optimal_solution(arr: list[int]) -> list[int]:
    n = len(arr)
    if n == 0:
        return []
    leaders = []
    max_val = arr[-1]
    leaders.append(max_val)
    
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_val:
            max_val = arr[i]
            leaders.append(max_val)
            
    leaders.reverse()
    return leaders

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([16, 17, 4, 3, 5, 2], [17, 5, 2]),
        ([1, 2, 3, 4, 5], [5])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
