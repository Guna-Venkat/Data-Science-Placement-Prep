"""
LeetCode Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Problem Name: Delete the Middle Node of a Linked List
Description: Delete the middle node of a linked list and return the modified head.

Folder: LinkedList
File: 167_Delete_the_middle_node_in_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Tortoise and Hare with a pointer tracking the node before slow.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
        
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = slow.next
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res = optimal_solution(head) # deletes 3
    assert res.next.next.val == 4
    print("Done.")
