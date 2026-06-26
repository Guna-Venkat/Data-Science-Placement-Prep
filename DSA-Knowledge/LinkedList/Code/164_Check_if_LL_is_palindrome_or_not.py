"""
LeetCode Link: https://leetcode.com/problems/palindrome-linked-list/
Problem Name: Palindrome Linked List
Description: Check if a singly linked list is a palindrome.

Folder: LinkedList
File: 164_Check_if_LL_is_palindrome_or_not.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Find middle, reverse second half, compare both halves. Restore list if needed.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> bool:
    if not head or not head.next:
        return True
        
    # Find middle
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    # Reverse second half
    def reverse(node):
        prev = None
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    second_head = reverse(slow.next)
    
    # Compare
    first = head
    second = second_head
    is_palindrome = True
    while second:
        if first.val != second.val:
            is_palindrome = False
            break
        first = first.next
        second = second.next
        
    # Restore (optional but good practice)
    slow.next = reverse(second_head)
    
    return is_palindrome

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert optimal_solution(head) == True
    
    head2 = ListNode(1, ListNode(2, ListNode(3)))
    assert optimal_solution(head2) == False
    print("Done.")
