"""
LeetCode Link: https://leetcode.com/problems/linked-list-cycle/
Problem Name: Linked List Cycle
Description: Detect if a linked list contains a loop/cycle.

Folder: LinkedList
File: 161_Detect_a_loop_in_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Tortoise and Hare. If there is a cycle, slow and fast pointers will meet.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head # loop back to head
    assert optimal_solution(head) == True
    print("Done.")
