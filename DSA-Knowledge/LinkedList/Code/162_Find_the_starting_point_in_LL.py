"""
LeetCode Link: https://leetcode.com/problems/linked-list-cycle-ii/
Problem Name: Find starting point of loop in Linked List
Description: Find the node where the cycle begins. Return None if no cycle.

Folder: LinkedList
File: 162_Find_the_starting_point_in_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# 1. Detect intersection point using Tortoise & Hare.
# 2. Reset slow pointer to head. Move both pointers at equal speed (1 step). 
#    They will meet at the starting point of the loop.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Cycle detected. Find start node.
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(3)
    loop_node = ListNode(2)
    head.next = loop_node
    loop_node.next = ListNode(0)
    loop_node.next.next = ListNode(-4)
    loop_node.next.next.next = loop_node # Loop points to node 2
    
    res = optimal_solution(head)
    assert res is not None and res.val == 2
    print("Done.")
