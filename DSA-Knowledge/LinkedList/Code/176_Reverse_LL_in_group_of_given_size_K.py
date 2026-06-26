"""
LeetCode Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
Problem Name: Reverse Nodes in k-Group
Description: Reverse nodes of a linked list k at a time.

Folder: LinkedList
File: 176_Reverse_LL_in_group_of_given_size_K.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Verify k nodes exist before reversing. Reverse them recursively or iteratively.
# Time Complexity: O(N)
# Space Complexity: O(N/K) recursion stack
def optimal_solution(head: ListNode, k: int) -> ListNode:
    # Check if there are k nodes left
    curr = head
    for _ in range(k):
        if not curr:
            return head
        curr = curr.next
        
    # Reverse k nodes
    prev = None
    curr = head
    for _ in range(k):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    head.next = optimal_solution(curr, k)
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head, 2) # (2->1->4->3->5)
    assert res.val == 2
    assert res.next.val == 1
    assert res.next.next.val == 4
    print("Done.")
