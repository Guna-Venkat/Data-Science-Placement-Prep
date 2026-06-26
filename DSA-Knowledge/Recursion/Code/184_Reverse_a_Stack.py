"""
LeetCode Link: https://www.geeksforgeeks.org/problems/reverse-a-stack/1
Problem Name: Reverse a Stack
Description: Reverse a stack recursively without loops.

Folder: Recursion
File: 184_Reverse_a_Stack.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Pop top, recursively reverse remaining stack, then insert popped element at bottom.
# Time Complexity: O(N^2)
# Space Complexity: O(N) recursion stack
def insert_at_bottom(stack: list[int], val: int):
    if not stack:
        stack.append(val)
        return
    temp = stack.pop()
    insert_at_bottom(stack, val)
    stack.append(temp)

def optimal_solution(stack: list[int]) -> list[int]:
    if not stack:
        return stack
    temp = stack.pop()
    optimal_solution(stack)
    insert_at_bottom(stack, temp)
    return stack

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 2, 1]) == [1, 2, 3] # reversed stack representation
    print("Done.")
