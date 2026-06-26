"""
LeetCode Link: https://www.codingninjas.com/studio/problems/partitions-with-given-difference_3751628
Problem Name: Partitions with Given Difference
Description: Count partitions s1 and s2 such that s1 - s2 = D and s1 >= s2.

Folder: Dynamic_Programming
File: 420_Count_partitions_with_given_difference.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: s1 + s2 = total, s1 - s2 = diff => 2*s1 = total + diff => s1 = (total + diff) / 2.
# Target is s1.
# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
def optimal_solution(arr: list[int], diff: int) -> int:
    total = sum(arr)
    if (total + diff) % 2 != 0 or total < diff:
        return 0
    target = (total + diff) // 2
    
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in arr:
        for t in range(target, num - 1, -1):
            dp[t] += dp[t - num]
    return dp[target]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([5, 2, 6, 4], 3) == 1
    print("Done.")
