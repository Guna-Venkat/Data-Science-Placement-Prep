"""
LeetCode Link: https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
Problem Name: Sort a Linked List of 0s, 1s, and 2s
Description: Sort a linked list of 0s, 1s, and 2s by changing links.

Folder: LinkedList
File: 169_Sort_a_Linked_List_of_0s_1s_and_2s.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Create three dummy lists for 0s, 1s, and 2s. Traverse and link nodes accordingly.
# Merge the three lists.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
        
    dummy0, dummy1, dummy2 = ListNode(0), ListNode(0), ListNode(0)
    p0, p1, p2 = dummy0, dummy1, dummy2
    
    curr = head
    while curr:
        if curr.val == 0:
            p0.next = curr
            p0 = p0.next
        elif curr.val == 1:
            p1.next = curr
            p1 = p1.next
        else:
            p2.next = curr
            p2 = p2.next
        curr = curr.next
        
    # Link lists
    p0.next = dummy1.next if dummy1.next else dummy2.next
    p1.next = dummy2.next
    p2.next = None
    
    return dummy0.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(0, ListNode(2, ListNode(1, ListNode(0))))))
    res = optimal_solution(head)
    assert res.val == 0
    assert res.next.val == 0
    assert res.next.next.val == 1
    print("Done.")
