"""
LeetCode Link: https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1
Problem Name: Length of the Linked List
Description: Find the number of nodes in a linked list.

Folder: LinkedList
File: 152_Find_the_length_of_the_Linked_List.py
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
def optimal_solution(head: ListNode) -> int:
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    return length

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert optimal_solution(head) == 3
    assert optimal_solution(None) == 0
    print("Done.")
