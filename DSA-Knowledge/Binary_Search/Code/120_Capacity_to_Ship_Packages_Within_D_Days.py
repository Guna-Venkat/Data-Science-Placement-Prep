"""
LeetCode Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Problem Name: Capacity to Ship Packages Within D Days
Description: Find minimum weight capacity to ship all packages in D days.

Folder: Binary_Search
File: 120_Capacity_to_Ship_Packages_Within_D_Days.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on capacity in range [max(weights), sum(weights)].
# Time Complexity: O(N * log(sum(weights) - max(weights)))
# Space Complexity: O(1)
def optimal_solution(weights: list[int], days: int) -> int:
    def can_ship(capacity):
        curr_weight = 0
        curr_days = 1
        for w in weights:
            if curr_weight + w > capacity:
                curr_days += 1
                curr_weight = w
            else:
                curr_weight += w
        return curr_days <= days

    low, high = max(weights), sum(weights)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_ship(mid):
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
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15),
        (([3, 2, 2, 4, 1, 4], 3), 6)
    ]
    for idx, ((weights, days), expected) in enumerate(test_cases, 1):
        assert optimal_solution(weights, days) == expected, f"Test case {idx} failed"
    print("Done.")
