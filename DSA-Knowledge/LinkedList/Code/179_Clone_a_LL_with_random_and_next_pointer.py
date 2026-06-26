"""
LeetCode Link: https://leetcode.com/problems/copy-list-with-random-pointer/
Problem Name: Copy List with Random Pointer
Description: Deep copy a linked list where each node has a next and random pointer.

Folder: LinkedList
File: 179_Clone_a_LL_with_random_and_next_pointer.py
"""

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# 1. Create duplicate node next to each original node: A -> A' -> B -> B'
# 2. Assign random pointers: node.next.random = node.random.next (if exists)
# 3. Separate original and cloned lists.
# Time Complexity: O(N)
# Space Complexity: O(1) auxiliary space (excluding clone allocation)
def optimal_solution(head: ListNode) -> ListNode:
    if not head:
        return None
        
    # Step 1: Duplicate nodes
    curr = head
    while curr:
        temp = curr.next
        curr.next = ListNode(curr.val, next=temp)
        curr = temp
        
    # Step 2: Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
        
    # Step 3: Separate lists
    dummy = ListNode(0)
    copy_curr = dummy
    curr = head
    while curr:
        temp = curr.next.next
        
        # Link copy
        copy_curr.next = curr.next
        copy_curr = copy_curr.next
        
        # Restore original
        curr.next = temp
        curr = temp
        
    return dummy.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n1.random = n2 # 1's random is 2
    n2.random = n2 # 2's random is 2
    
    clone = optimal_solution(n1)
    assert clone.val == 1
    assert clone.next.val == 2
    assert clone.random.val == 2
    print("Done.")
