"""
LeetCode Link: https://leetcode.com/problems/assign-cookies/
Problem Name: Assign Cookies (Greedy/DP)
Description: Maximize content children given greed factor and cookie sizes.

Folder: Dynamic_Programming
File: 421_Assign_Cookies_DP.py
"""

# ============================================
# OPTIMAL APPROACH (Greedy)
# ============================================
# Time Complexity: O(N log N + M log M)
# Space Complexity: O(1)
def optimal_solution(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    child = 0
    cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3], [1, 1]) == 1
    assert optimal_solution([1, 2], [1, 2, 3]) == 2
    print("Done.")
