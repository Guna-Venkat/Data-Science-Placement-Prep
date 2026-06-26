"""
LeetCode Link: https://leetcode.com/problems/rotate-array/
Problem Name: Rotate Array by K Places (Left variant)
Description: Left rotate the array by k steps.

Folder: Arrays
File: 067_Left_Rotate_Array_by_K_Places.py
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Store first k elements in a temp array, shift remaining elements left, copy temp back.
# Time Complexity: O(N)
# Space Complexity: O(k)
def brute_force_solution(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    temp = arr[:k]
    for i in range(n - k):
        arr[i] = arr[i + k]
    for i in range(k):
        arr[n - k + i] = temp[i]
    return arr

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Reverse first k, reverse remaining, then reverse the entire array.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    
    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)
    return arr

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 4, 5, 6, 7], 3), [4, 5, 6, 7, 1, 2, 3]),
        (([1, 2], 3), [2, 1])
    ]
    
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:], k) == expected, f"Test case {idx} failed"
        
    print("Done.")
