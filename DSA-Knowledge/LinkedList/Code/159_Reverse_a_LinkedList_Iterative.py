"""
LeetCode Link: https://leetcode.com/problems/reverse-linked-list/
Problem Name: Reverse Linked List (Iterative)
Description: Reverse a singly linked list in-place iteratively.

Folder: LinkedList
File: 159_Reverse_a_LinkedList_Iterative.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Maintain three pointers: prev, curr, temp.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3)))
    rev = optimal_solution(head)
    assert rev.val == 3
    assert rev.next.val == 2
    print("Done.")
