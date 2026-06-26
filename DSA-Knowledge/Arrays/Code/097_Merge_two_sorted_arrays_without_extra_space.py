"""
LeetCode Link: https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
Problem Name: Merge Two Sorted Arrays Without Extra Space
Description: Merge elements of two sorted arrays A and B into both A and B sorted in-place.

Folder: Arrays
File: 097_Merge_two_sorted_arrays_without_extra_space.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use Gap Method (Shell Sort based) to compare and swap elements at distance 'gap'.
# Time Complexity: O((N + M) log(N + M))
# Space Complexity: O(1)
def optimal_solution(arr1: list[int], arr2: list[int]) -> tuple[list[int], list[int]]:
    n, m = len(arr1), len(arr2)
    length = n + m
    gap = (length // 2) + (length % 2)
    
    def get_val(idx):
        if idx < n:
            return arr1[idx]
        return arr2[idx - n]
        
    def set_val(idx, val):
        if idx < n:
            arr1[idx] = val
        else:
            arr2[idx - n] = val
            
    while gap > 0:
        l = 0
        r = gap
        while r < length:
            if get_val(l) > get_val(r):
                temp = get_val(l)
                set_val(l, get_val(r))
                set_val(r, temp)
            l += 1
            r += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
        
    return arr1, arr2

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    arr1, arr2 = [1, 3, 5, 7], [0, 2, 6, 8, 9]
    res1, res2 = optimal_solution(arr1[:], arr2[:])
    assert res1 == [0, 1, 2, 3] and res2 == [5, 6, 7, 8, 9], "Test failed"
    
    print("Done.")
