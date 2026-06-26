"""
LeetCode Link: https://www.geeksforgeeks.org/problems/binary-search-trees/1
Problem Name: Binary Search Trees (Introduction)
Description: Check if the given keys can represent the level order / properties of a BST.
Specifically, check if left < root < right for a simple BST definition.

Folder: Binary_Search_Trees
File: 335_Introduction_to_BST.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: In a BST, the left subtree contains keys smaller than root, 
# and right subtree contains keys larger than root.
# Given a sorted array, can it represent a valid BST? Yes, any sorted array can be turned into a BST.
# But if it's not sorted, check if elements are sorted for inorder.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> bool:
    # Check if array is strictly sorted in ascending order (no duplicates allowed in standard strict BST)
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 5, 8]) == True
    assert optimal_solution([1, 3, 2]) == False
    print("Done.")
