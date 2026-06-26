"""
LeetCode Link: https://www.geeksforgeeks.org/problems/sort-a-stack/1
Problem Name: Sort a Stack using Recursion
Description: Sort a stack of numbers using only recursion and no loops.

Folder: Recursion
File: 183_Sort_a_stack_using_recursion.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# 1. Pop top element, recursively sort remaining stack.
# 2. Insert popped element back into sorted stack in correct sorted position.
# Time Complexity: O(N^2)
# Space Complexity: O(N) recursion stack
def insert_sorted(stack: list[int], val: int):
    if not stack or stack[-1] <= val:
        stack.append(val)
        return
    temp = stack.pop()
    insert_sorted(stack, val)
    stack.append(temp)

def optimal_solution(stack: list[int]) -> list[int]:
    if not stack:
        return stack
    temp = stack.pop()
    optimal_solution(stack)
    insert_sorted(stack, temp)
    return stack

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 2, 1]) == [1, 2, 3]
    assert optimal_solution([11, 2, 32, 3, 41]) == [2, 3, 11, 32, 41]
    print("Done.")
