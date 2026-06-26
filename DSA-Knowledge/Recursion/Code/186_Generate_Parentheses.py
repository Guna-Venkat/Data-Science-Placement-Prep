"""
LeetCode Link: https://leetcode.com/problems/generate-parentheses/
Problem Name: Generate Parentheses
Description: Generate all combinations of well-formed parentheses.

Folder: Recursion
File: 186_Generate_Parentheses.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of open and close counts. Can add '(' if open < n.
# Can add ')' if close < open.
# Time Complexity: O(4^n / sqrt(n)) Catalan number count
# Space Complexity: O(n) recursion stack
def optimal_solution(n: int) -> list[str]:
    result = []
    
    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            result.append(curr)
            return
            
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert sorted(optimal_solution(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    print("Done.")
