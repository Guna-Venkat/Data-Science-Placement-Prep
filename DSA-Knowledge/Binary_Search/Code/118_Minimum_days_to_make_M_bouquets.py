"""
LeetCode Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
Problem Name: Minimum Days to Make M Bouquets
Description: Find minimum days to make m bouquets using k adjacent flowers.

Folder: Binary_Search
File: 118_Minimum_days_to_make_M_bouquets.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on days. Range is [min(bloomDay), max(bloomDay)].
# Time Complexity: O(N * log(max(bloomDay)))
# Space Complexity: O(1)
def optimal_solution(bloomDay: list[int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1
        
    def can_make(days):
        bouquets = 0
        flowers = 0
        for b in bloomDay:
            if b <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    low, high = min(bloomDay), max(bloomDay)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if can_make(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 10, 2, 9, 3, 8, 4, 7], 3, 2), 9),
        (([1, 10, 3, 10, 2], 3, 2), -1)
    ]
    for idx, ((bloomDay, m, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(bloomDay, m, k) == expected, f"Test case {idx} failed"
    print("Done.")
