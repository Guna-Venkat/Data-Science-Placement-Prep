"""
LeetCode Link: https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
Problem Name: Flattening a Linked List
Description: Flatten a multi-level linked list where each node has a next and a bottom/child pointer.

Folder: LinkedList
File: 178_Flattening_of_LL.py
"""

class ListNode:
    def __init__(self, val=0, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursively flatten list by merging current list with flattened remaining list.
# Time Complexity: O(N * M) where N is number of columns, M is average height of column.
# Space Complexity: O(N) recursion stack depth
def merge(a, b):
    if not a: return b
    if not b: return a
    
    if a.val < b.val:
        result = a
        result.bottom = merge(a.bottom, b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)
    result.next = None
    return result

def optimal_solution(root: ListNode) -> ListNode:
    if not root or not root.next:
        return root
        
    # Flatten the remaining list first
    root.next = optimal_solution(root.next)
    
    # Merge current column with flattened remainder
    root = merge(root, root.next)
    
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    col1 = ListNode(5, bottom=ListNode(7, bottom=ListNode(8)))
    col2 = ListNode(10, bottom=ListNode(20))
    col1.next = col2
    
    res = optimal_solution(col1)
    assert res.val == 5
    assert res.bottom.val == 7
    assert res.bottom.bottom.val == 8
    assert res.bottom.bottom.bottom.val == 10
    print("Done.")
