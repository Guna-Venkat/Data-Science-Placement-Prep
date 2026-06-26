"""
LeetCode Link: https://www.geeksforgeeks.org/problems/unique-binary-tree-requirements/1
Problem Name: Unique Binary Tree Requirements
Description: Given two traversals, determine if they can form a unique binary tree.

Folder: Binary_Trees
File: 328_Requirements_needed_to_construct_a_unique_BT.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: A unique binary tree can be constructed if one traversal is INORDER, 
# and the other is either PREORDER or POSTORDER.
# Code representation: 1 = Preorder, 2 = Inorder, 3 = Postorder.
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(t1: int, t2: int) -> bool:
    # 2 represents Inorder. We need Inorder along with Preorder (1) or Postorder (3)
    if (t1 == 2 and t2 == 1) or (t1 == 1 and t2 == 2):
        return True
    if (t1 == 2 and t2 == 3) or (t1 == 3 and t2 == 2):
        return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(2, 1) == True
    assert optimal_solution(1, 3) == False
    print("Done.")
