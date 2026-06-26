"""
LeetCode Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Problem Name: Remove Nth Node From End of List
Description: Remove the Nth node from the end of the list and return its head.

Folder: LinkedList
File: 166_Remove_Nth_node_from_the_back_of_the_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Fast pointer moves N steps first. Then move both fast and slow until fast reaches end.
# Slow will point to the node just before the target node to delete.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    
    for _ in range(n):
        fast = fast.next
        
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    return dummy.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head, 2) # deletes 4
    assert res.next.next.next.val == 5
    print("Done.")
