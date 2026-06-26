"""
LeetCode Link: https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1
Problem Name: Remove duplicates from sorted DLL
Description: Remove duplicates from a sorted doubly linked list in place.

Folder: LinkedList
File: 175_Remove_duplicates_from_sorted_DLL.py
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
def optimal_solution(head: DLLNode) -> DLLNode:
    if not head:
        return None
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            # remove curr.next
            next_node = curr.next.next
            curr.next = next_node
            if next_node:
                next_node.prev = curr
        else:
            curr = curr.next
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(1, prev=head)
    head.next.next = DLLNode(2, prev=head.next)
    
    new_head = optimal_solution(head)
    assert new_head.val == 1
    assert new_head.next.val == 2
    print("Done.")
