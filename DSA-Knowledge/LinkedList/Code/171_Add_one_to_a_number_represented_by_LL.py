"""
LeetCode Link: https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
Problem Name: Add one to a number represented by LL
Description: Add 1 to the number represented by the linked list.

Folder: LinkedList
File: 171_Add_one_to_a_number_represented_by_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursively traverse to the end. Add carry as we backtrack.
# Time Complexity: O(N)
# Space Complexity: O(N) recursion stack
def optimal_solution(head: ListNode) -> ListNode:
    def helper(node):
        if not node:
            return 1 # carry to add
        carry = helper(node.next)
        node.val += carry
        if node.val >= 10:
            node.val = 0
            return 1
        return 0

    carry = helper(head)
    if carry:
        new_head = ListNode(1)
        new_head.next = head
        return new_head
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(4, ListNode(5, ListNode(9)))
    res = optimal_solution(head) # 459 + 1 = 460
    assert res.val == 4
    assert res.next.val == 6
    assert res.next.next.val == 0
    print("Done.")
