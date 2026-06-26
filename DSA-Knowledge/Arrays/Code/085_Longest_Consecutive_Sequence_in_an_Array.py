"""
LeetCode Link: https://leetcode.com/problems/longest-consecutive-sequence/
Problem Name: Longest Consecutive Sequence
Description: Find length of longest consecutive elements sequence.

Folder: Arrays
File: 085_Longest_Consecutive_Sequence_in_an_Array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Put all numbers in Set. Traverse numbers, start count only if num-1 is not in Set.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    num_set = set(nums)
    max_streak = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            curr_num = num
            curr_streak = 1
            
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_streak += 1
                
            max_streak = max(max_streak, curr_streak)
            
    return max_streak

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
