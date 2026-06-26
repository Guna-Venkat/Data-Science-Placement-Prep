"""
LeetCode Link: https://leetcode.com/problems/count-good-numbers/
Problem Name: Count Good Numbers
Description: A digit string is good if digits at even indices are even, and prime at odd indices.
Count good strings of length n modulo 10^9 + 7.

Folder: Recursion
File: 182_Count_Good_Numbers.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Count of even positions = ceil(n/2), count of odd positions = floor(n/2).
# Choice at even = 5 (0, 2, 4, 6, 8). Choice at odd = 4 (2, 3, 5, 7).
# Calculate 5^even * 4^odd modulo 10^9 + 7.
# Time Complexity: O(log n)
# Space Complexity: O(log n) stack depth
def optimal_solution(n: int) -> int:
    MOD = 10**9 + 7
    
    def power(base, exp):
        if exp == 0:
            return 1
        half = power(base, exp // 2)
        ans = (half * half) % MOD
        if exp % 2 != 0:
            ans = (ans * base) % MOD
        return ans

    evens = (n + 1) // 2
    odds = n // 2
    return (power(5, evens) * power(4, odds)) % MOD

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(1) == 5
    assert optimal_solution(4) == 400
    assert optimal_solution(50) == 564908303
    print("Done.")
