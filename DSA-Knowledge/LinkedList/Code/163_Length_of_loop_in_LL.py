"""
LeetCode Link: https://www.geeksforgeeks.org/problems/find-length-of-loop/1
Problem Name: Find Length of Loop in Linked List
Description: Find the number of nodes inside the loop of a linked list.

Folder: LinkedList
File: 163_Length_of_loop_in_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Once slow meets fast, hold fast in place and move slow count steps until it meets fast again.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Count length of loop
            count = 1
            slow = slow.next
            while slow != fast:
                count += 1
                slow = slow.next
            return count
    return 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 # Loop length is 3 (2 -> 3 -> 4 -> 2)
    
    assert optimal_solution(head) == 3
    print("Done.")
