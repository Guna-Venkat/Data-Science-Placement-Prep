"""
LeetCode Link: https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1
Problem Name: Delete all occurrences of a key in DLL
Description: Delete all nodes with key X from a Doubly Linked List.

Folder: LinkedList
File: 173_Delete_all_occurrences_of_a_key_in_DLL.py
"""

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode, x: int) -> DLLNode:
    curr = head
    while curr:
        if curr.val == x:
            if curr == head:
                head = head.next
                if head:
                    head.prev = None
            else:
                if curr.next:
                    curr.next.prev = curr.prev
                if curr.prev:
                    curr.prev.next = curr.next
        curr = curr.next
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(2)
    head.next = DLLNode(2, prev=head)
    head.next.next = DLLNode(10, prev=head.next)
    head.next.next.next = DLLNode(2, prev=head.next.next)
    
    new_head = optimal_solution(head, 2) # leaves only 10
    assert new_head.val == 10
    assert new_head.next is None
    print("Done.")
