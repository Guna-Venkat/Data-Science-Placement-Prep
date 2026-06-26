"""
LeetCode Link: https://leetcode.com/problems/add-two-numbers/
Problem Name: Add Two Numbers
Description: Add two numbers represented by two linked lists (digits stored in reverse order).

Folder: LinkedList
File: 172_Add_two_numbers_in_Linked_List.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(max(N, M))
# Space Complexity: O(max(N, M)) for new list
def optimal_solution(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    l1 = ListNode(2, ListNode(4, ListNode(3))) # 342
    l2 = ListNode(5, ListNode(6, ListNode(4))) # 465
    res = optimal_solution(l1, l2) # 807 (7 -> 0 -> 8)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8
    print("Done.")
