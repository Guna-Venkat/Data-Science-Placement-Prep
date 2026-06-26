"""
LeetCode Link: https://leetcode.com/problems/sort-list/
Problem Name: Sort List
Description: Sort a linked list in O(N log N) time using constant space complexity.

Folder: LinkedList
File: 168_Sort_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Merge Sort.
# Time Complexity: O(N log N)
# Space Complexity: O(log N) stack depth
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
        
    # Split list into two halves
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = None # break the link
    
    left = optimal_solution(head)
    right = optimal_solution(slow)
    
    return merge_two_lists(left, right)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    res = optimal_solution(head)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    print("Done.")
