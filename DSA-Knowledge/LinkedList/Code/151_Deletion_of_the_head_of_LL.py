"""
LeetCode Link: https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1
Problem Name: Deletion of the head of LL
Description: Delete the head node of a singly linked list.

Folder: LinkedList
File: 151_Deletion_of_the_head_of_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head:
        return None
    return head.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3)))
    new_head = optimal_solution(head)
    assert new_head.val == 2
    print("Done.")
