"""
LeetCode Link: https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
Problem Name: Search in Linked List
Description: Return True if a node with value X exists in the linked list, else False.

Folder: LinkedList
File: 153_Search_in_Linked_List.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode, x: int) -> bool:
    curr = head
    while curr:
        if curr.val == x:
            return True
        curr = curr.next
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert optimal_solution(head, 2) == True
    assert optimal_solution(head, 5) == False
    print("Done.")
