"""
LeetCode Link: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
Problem Name: Find pairs with given sum in sorted DLL
Description: Find all pairs in a sorted doubly linked list whose sum is equal to target.

Folder: LinkedList
File: 174_Find_Pairs_with_Given_Sum_in_Doubly_Linked_List.py
"""

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Two pointer approach. One starting at head, other at tail.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode, target: int) -> list[tuple[int, int]]:
    if not head:
        return []
        
    tail = head
    while tail.next:
        tail = tail.next
        
    pairs = []
    l, r = head, tail
    while l != r and r.next != l:
        curr_sum = l.val + r.val
        if curr_sum == target:
            pairs.append((l.val, r.val))
            l = l.next
            r = r.prev
        elif curr_sum < target:
            l = l.next
        else:
            r = r.prev
            
    return pairs

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(2, prev=head)
    head.next.next = DLLNode(4, prev=head.next)
    head.next.next.next = DLLNode(5, prev=head.next.next)
    head.next.next.next.next = DLLNode(6, prev=head.next.next.next)
    
    assert optimal_solution(head, 7) == [(1, 6), (2, 5)]
    print("Done.")
