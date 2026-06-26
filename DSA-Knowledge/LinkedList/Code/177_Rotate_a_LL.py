"""
LeetCode Link: https://leetcode.com/problems/rotate-list/
Problem Name: Rotate List
Description: Rotate the linked list to the right by k places.

Folder: LinkedList
File: 177_Rotate_a_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Join the tail of the list to the head to form a circular list.
# Then break the list after N - (k % N) elements.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head
        
    # Find length and tail node
    length = 1
    curr = head
    while curr.next:
        length += 1
        curr = curr.next
        
    curr.next = head # Make it circular
    
    k = k % length
    steps_to_new_tail = length - k
    
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head, 2) # (4->5->1->2->3)
    assert res.val == 4
    assert res.next.val == 5
    print("Done.")
