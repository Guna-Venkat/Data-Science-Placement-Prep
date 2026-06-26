"""
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1
Problem Name: Introduction to Doubly LL
Description: Convert an array of integers to a doubly linked list and return the head.

Folder: LinkedList
File: 154_Introduction_to_Doubly_LL.py
"""

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N) for DLL creation
def optimal_solution(arr: list[int]) -> DLLNode:
    if not arr:
        return None
    head = DLLNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        temp = DLLNode(arr[i])
        curr.next = temp
        temp.prev = curr
        curr = temp
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = optimal_solution([1, 2, 3])
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.prev.val == 1
    print("Done.")
