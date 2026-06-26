"""
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1
Problem Name: Introduction to Singly LinkedList
Description: Convert an array of integers to a singly linked list and return the head.

Folder: LinkedList
File: 149_Introduction_to_Singly_LinkedList.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N) for list creation
def optimal_solution(arr: list[int]) -> ListNode:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = optimal_solution([1, 2, 3, 4, 5])
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.next.next.val == 5
    print("Done.")
