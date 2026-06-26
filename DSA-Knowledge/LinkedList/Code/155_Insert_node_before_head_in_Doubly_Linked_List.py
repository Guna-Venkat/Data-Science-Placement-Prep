"""
LeetCode Link: https://www.geeksforgeeks.org/problems/doubly-linked-list-insertion-at-given-position/1
Problem Name: Insert node before head in Doubly Linked List
Description: Insert a new node before the head of a doubly linked list.

Folder: LinkedList
File: 155_Insert_node_before_head_in_Doubly_Linked_List.py
"""

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode, val: int) -> DLLNode:
    new_node = DLLNode(val)
    if not head:
        return new_node
    new_node.next = head
    head.prev = new_node
    return new_node

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(2)
    new_head = optimal_solution(head, 1)
    assert new_head.val == 1
    assert new_head.next.val == 2
    assert new_head.next.prev.val == 1
    print("Done.")
