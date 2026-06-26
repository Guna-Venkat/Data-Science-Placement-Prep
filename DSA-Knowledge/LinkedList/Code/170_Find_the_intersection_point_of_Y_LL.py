"""
LeetCode Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Problem Name: Intersection of Two Linked Lists
Description: Find the node where two singly linked lists intersect.

Folder: LinkedList
File: 170_Find_the_intersection_point_of_Y_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Initialize two pointers at heads. Move each pointer 1 step. 
# If one reaches None, redirect to the head of the other list. They will meet at intersection point.
# Time Complexity: O(N + M)
# Space Complexity: O(1)
def optimal_solution(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    intersect = ListNode(8, ListNode(4, ListNode(5)))
    headA = ListNode(4, ListNode(1, intersect))
    headB = ListNode(5, ListNode(0, ListNode(1, intersect)))
    
    res = optimal_solution(headA, headB)
    assert res is not None and res.val == 8
    print("Done.")
