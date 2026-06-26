"""
LeetCode Link: https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1
Problem Name: Delete head of Doubly Linked List
Description: Delete the head node of a doubly linked list.

Folder: LinkedList
File: 156_Delete_head_of_Doubly_Linked_List.py
"""

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode) -> DLLNode:
    if not head or not head.next:
        return None
    new_head = head.next
    new_head.prev = None
    return new_head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(2, prev=head)
    
    new_head = optimal_solution(head)
    assert new_head.val == 2
    assert new_head.prev is None
    print("Done.")
