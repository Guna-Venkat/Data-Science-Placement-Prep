"""
LeetCode Link: https://leetcode.com/problems/expression-add-operators/
Problem Name: Expression Add Operators
Description: Add operators (+, -, *) to digits to make value equal to target.

Folder: Recursion
File: 204_Expression_Add_Operators.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking. Track index, path expression, current total value, 
# and the value of the last computed term (vital to handle '*' order of operations).
# Time Complexity: O(4^N)
# Space Complexity: O(N)
def optimal_solution(num: str, target: int) -> list[str]:
    result = []
    
    def backtrack(idx, expr, curr_val, last_term):
        if idx == len(num):
            if curr_val == target:
                result.append("".join(expr))
            return
            
        for i in range(idx, len(num)):
            # Skip leading zeros
            if i > idx and num[idx] == "0":
                break
                
            part = num[idx:i+1]
            val = int(part)
            
            if idx == 0:
                backtrack(i + 1, [part], val, val)
            else:
                # Addition
                expr.append("+")
                expr.append(part)
                backtrack(i + 1, expr, curr_val + val, val)
                expr.pop(); expr.pop()
                
                # Subtraction
                expr.append("-")
                expr.append(part)
                backtrack(i + 1, expr, curr_val - val, -val)
                expr.pop(); expr.pop()
                
                # Multiplication
                expr.append("*")
                expr.append(part)
                backtrack(i + 1, expr, curr_val - last_term + (last_term * val), last_term * val)
                expr.pop(); expr.pop()

    backtrack(0, [], 0, 0)
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert sorted(optimal_solution("123", 6)) == sorted(["1+2+3", "1*2*3"])
    assert sorted(optimal_solution("232", 8)) == sorted(["2*3+2", "2+3*2"])
    print("Done.")
