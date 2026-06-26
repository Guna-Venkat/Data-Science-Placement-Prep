"""
LeetCode Link: https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1
Problem Name: Boolean Parenthesization
Description: Count ways to parenthesize expression to evaluate to True.

Folder: Dynamic_Programming
File: 454_Different_Ways_to_Evaluate_a_Boolean_Expression.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(s: str) -> int:
    MOD = 1003
    n = len(s)
    memo = {}
    
    def solve(i, j, is_true):
        if i > j:
            return 0
        if i == j:
            if is_true:
                return 1 if s[i] == 'T' else 0
            else:
                return 1 if s[i] == 'F' else 0
                
        key = (i, j, is_true)
        if key in memo:
            return memo[key]
            
        ways = 0
        for k in range(i + 1, j, 2):
            lt = solve(i, k - 1, True)
            lf = solve(i, k - 1, False)
            rt = solve(k + 1, j, True)
            rf = solve(k + 1, j, False)
            
            op = s[k]
            if op == '&':
                if is_true:
                    ways += lt * rt
                else:
                    ways += lf * rt + lt * rf + lf * rf
            elif op == '|':
                if is_true:
                    ways += lt * rt + lf * rt + lt * rf
                else:
                    ways += lf * rf
            elif op == '^':
                if is_true:
                    ways += lt * rf + lf * rt
                else:
                    ways += lt * rt + lf * rf
                    
        memo[key] = ways % MOD
        return memo[key]

    return solve(0, n - 1, True)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("T|F^F") == 2
    print("Done.")
