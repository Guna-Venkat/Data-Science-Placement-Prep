"""
LeetCode Link: https://leetcode.com/problems/middle-of-the-linked-list/
Problem Name: Middle of the Linked List
Description: Find the middle node of a singly linked list. Return the second middle if even.

Folder: LinkedList
File: 158_Middle_of_a_LinkedList_TortoiseHare_Method.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Tortoise moves 1 step; Hare moves 2 steps.
# When Hare reaches end, Tortoise will be at the middle.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert optimal_solution(head).val == 3
    print("Done.")
