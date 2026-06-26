"""
LeetCode Link: https://leetcode.com/problems/merge-intervals/
Problem Name: Merge Intervals
Description: Merge overlapping intervals.

Folder: Arrays
File: 096_Merge_Overlapping_Subintervals.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort intervals by start value. Iterate and merge overlapping.
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def optimal_solution(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
            
    return merged

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
