"""
LeetCode Link: https://leetcode.com/problems/string-to-integer-atoi/
Problem Name: Recursive Implementation of atoi
Description: Convert a string to an integer recursively.

Folder: Recursion
File: 180_Recursive_Implementation_of_atoi.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N) recursion stack
def optimal_solution(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
        
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
        
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    def convert(idx, current_val):
        if idx >= len(s) or not s[idx].isdigit():
            return current_val
        digit = int(s[idx])
        new_val = current_val * 10 + digit
        # Overflow checks
        if sign * new_val > INT_MAX:
            return INT_MAX
        if sign * new_val < INT_MIN:
            return INT_MIN
        return convert(idx + 1, new_val)

    return sign * convert(0, 0)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("42") == 42
    assert optimal_solution("   -42") == -42
    assert optimal_solution("4193 with words") == 4193
    print("Done.")
