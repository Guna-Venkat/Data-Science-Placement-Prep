"""
LeetCode Link: https://leetcode.com/problems/majority-element-ii/
Problem Name: Majority Element II (> N/3)
Description: Find all elements that appear more than N/3 times.

Folder: Arrays
File: 091_Majority_Element_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Extended Boyer-Moore Voting Algorithm. There can be at most 2 majority elements.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    if not nums:
        return []
        
    cand1, cand2 = None, None
    count1, count2 = 0, 0
    
    for x in nums:
        if x == cand1:
            count1 += 1
        elif x == cand2:
            count2 += 1
        elif count1 == 0:
            cand1 = x
            count1 = 1
        elif count2 == 0:
            cand2 = x
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
            
    # Verify candidates
    res = []
    n = len(nums)
    if nums.count(cand1) > n // 3:
        res.append(cand1)
    if cand2 != cand1 and nums.count(cand2) > n // 3:
        res.append(cand2)
        
    return sorted(res)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 2, 3], [3]),
        ([1, 2], [1, 2])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
