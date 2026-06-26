"""
LeetCode Link: https://leetcode.com/problems/reverse-linked-list/
Problem Name: Reverse Linked List (Recursive)
Description: Reverse a singly linked list in-place recursively.

Folder: LinkedList
File: 160_Reverse_a_LL_Recursive.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N) recursion stack
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    new_head = optimal_solution(head.next)
    head.next.next = head
    head.next = None
    return new_head

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
