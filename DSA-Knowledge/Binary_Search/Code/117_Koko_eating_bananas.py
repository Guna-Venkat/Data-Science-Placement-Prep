"""
LeetCode Link: https://leetcode.com/problems/koko-eating-bananas/
Problem Name: Koko Eating Bananas
Description: Find minimum integer speed K to eat all bananas in H hours.

Folder: Binary_Search
File: 117_Koko_eating_bananas.py
"""

import math

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on speed K. Search range is [1, max(piles)].
# Time Complexity: O(N * log(max(piles)))
# Space Complexity: O(1)
def optimal_solution(piles: list[int], h: int) -> int:
    def can_eat_all(speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h

    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_eat_all(mid):
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
        (([3, 6, 7, 11], 8), 4),
        (([30, 11, 23, 4, 20], 5), 30)
    ]
    for idx, ((piles, h), expected) in enumerate(test_cases, 1):
        assert optimal_solution(piles, h) == expected, f"Test case {idx} failed"
    print("Done.")
