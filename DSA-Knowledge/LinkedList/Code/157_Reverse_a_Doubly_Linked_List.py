"""
LeetCode Link: https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
Problem Name: Reverse a Doubly Linked List
Description: Reverse a doubly linked list in place.

Folder: LinkedList
File: 157_Reverse_a_Doubly_Linked_List.py
"""

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: For each node, swap the prev and next pointers.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode) -> DLLNode:
    if not head or not head.next:
        return head
    
    curr = head
    last = None
    while curr:
        # Swap
        last = curr.prev
        curr.prev = curr.next
        curr.next = last
        # Move to next node (which is now stored in curr.prev)
        curr = curr.prev
        
    return last.prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(2, prev=head)
    head.next.next = DLLNode(3, prev=head.next)
    
    rev = optimal_solution(head)
    assert rev.val == 3
    assert rev.next.val == 2
    print("Done.")
