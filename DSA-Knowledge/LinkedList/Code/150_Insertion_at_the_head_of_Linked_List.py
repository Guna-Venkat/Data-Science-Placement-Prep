"""
LeetCode Link: https://www.geeksforgeeks.org/problems/linked-list-insertion/1
Problem Name: Insertion at the head of Linked List
Description: Insert a node with value X at the head of a linked list.

Folder: LinkedList
File: 150_Insertion_at_the_head_of_Linked_List.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(head: ListNode, x: int) -> ListNode:
    new_node = ListNode(x)
    new_node.next = head
    return new_node

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(2)
    head.next = ListNode(3)
    
    new_head = optimal_solution(head, 1)
    assert new_head.val == 1
    assert new_head.next.val == 2
    print("Done.")
