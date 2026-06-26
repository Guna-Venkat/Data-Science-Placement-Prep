"""
LeetCode Link: https://leetcode.com/problems/odd-even-linked-list/
Problem Name: Odd Even Linked List
Description: Group all odd-indexed nodes together followed by the even-indexed nodes.

Folder: LinkedList
File: 165_Segregate_odd_and_even_nodes_in_Linked_List.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Maintain odd and even pointers. Link odd next to even.next, etc.
# Connect end of odd list to head of even list.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
        
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        
    odd.next = even_head
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head)
    assert res.val == 1
    assert res.next.val == 3
    assert res.next.next.val == 5
    assert res.next.next.next.val == 2
    print("Done.")
