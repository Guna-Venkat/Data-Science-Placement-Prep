import os

SOLUTIONS = {
    "149_Introduction_to_Singly_LinkedList.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1
Problem Name: Introduction to Singly LinkedList
Description: Convert an array of integers to a singly linked list and return the head.

Folder: LinkedList
File: 149_Introduction_to_Singly_LinkedList.py
\"\"\"

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
""",

    "150_Insertion_at_the_head_of_Linked_List.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/linked-list-insertion/1
Problem Name: Insertion at the head of Linked List
Description: Insert a node with value X at the head of a linked list.

Folder: LinkedList
File: 150_Insertion_at_the_head_of_Linked_List.py
\"\"\"

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
""",

    "151_Deletion_of_the_head_of_LL.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1
Problem Name: Deletion of the head of LL
Description: Delete the head node of a singly linked list.

Folder: LinkedList
File: 151_Deletion_of_the_head_of_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head:
        return None
    return head.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3)))
    new_head = optimal_solution(head)
    assert new_head.val == 2
    print("Done.")
""",

    "152_Find_the_length_of_the_Linked_List.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1
Problem Name: Length of the Linked List
Description: Find the number of nodes in a linked list.

Folder: LinkedList
File: 152_Find_the_length_of_the_Linked_List.py
\"\"\"

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
""",

    "153_Search_in_Linked_List.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1
Problem Name: Search in Linked List
Description: Return True if a node with value X exists in the linked list, else False.

Folder: LinkedList
File: 153_Search_in_Linked_List.py
\"\"\"

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
""",

    "154_Introduction_to_Doubly_LL.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1
Problem Name: Introduction to Doubly LL
Description: Convert an array of integers to a doubly linked list and return the head.

Folder: LinkedList
File: 154_Introduction_to_Doubly_LL.py
\"\"\"

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
""",

    "155_Insert_node_before_head_in_Doubly_Linked_List.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/doubly-linked-list-insertion-at-given-position/1
Problem Name: Insert node before head in Doubly Linked List
Description: Insert a new node before the head of a doubly linked list.

Folder: LinkedList
File: 155_Insert_node_before_head_in_Doubly_Linked_List.py
\"\"\"

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
""",

    "156_Delete_head_of_Doubly_Linked_List.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1
Problem Name: Delete head of Doubly Linked List
Description: Delete the head node of a doubly linked list.

Folder: LinkedList
File: 156_Delete_head_of_Doubly_Linked_List.py
\"\"\"

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
def optimal_solution(head: DLLNode) -> DLLNode:
    if not head or not head.next:
        return None
    new_head = head.next
    new_head.prev = None
    return new_head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(2, prev=head)
    
    new_head = optimal_solution(head)
    assert new_head.val == 2
    assert new_head.prev is None
    print("Done.")
""",

    "157_Reverse_a_Doubly_Linked_List.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
Problem Name: Reverse a Doubly Linked List
Description: Reverse a doubly linked list in place.

Folder: LinkedList
File: 157_Reverse_a_Doubly_Linked_List.py
\"\"\"

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: For each node, swap the prev and next pointers.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode) -> DLLNode:
    if not head or not head.next:
        return head
    
    curr = head
    last = None
    while curr:
        # Swap
        last = curr.prev
        curr.prev = curr.next
        curr.next = last
        # Move to next node (which is now stored in curr.prev)
        curr = curr.prev
        
    return last.prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(2, prev=head)
    head.next.next = DLLNode(3, prev=head.next)
    
    rev = optimal_solution(head)
    assert rev.val == 3
    assert rev.next.val == 2
    print("Done.")
""",

    "158_Middle_of_a_LinkedList_TortoiseHare_Method.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/middle-of-the-linked-list/
Problem Name: Middle of the Linked List
Description: Find the middle node of a singly linked list. Return the second middle if even.

Folder: LinkedList
File: 158_Middle_of_a_LinkedList_TortoiseHare_Method.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Tortoise moves 1 step; Hare moves 2 steps.
# When Hare reaches end, Tortoise will be at the middle.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert optimal_solution(head).val == 3
    print("Done.")
""",

    "159_Reverse_a_LinkedList_Iterative.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/reverse-linked-list/
Problem Name: Reverse Linked List (Iterative)
Description: Reverse a singly linked list in-place iteratively.

Folder: LinkedList
File: 159_Reverse_a_LinkedList_Iterative.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Maintain three pointers: prev, curr, temp.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3)))
    rev = optimal_solution(head)
    assert rev.val == 3
    assert rev.next.val == 2
    print("Done.")
""",

    "160_Reverse_a_LL_Recursive.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/reverse-linked-list/
Problem Name: Reverse Linked List (Recursive)
Description: Reverse a singly linked list in-place recursively.

Folder: LinkedList
File: 160_Reverse_a_LL_Recursive.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N) recursion stack
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    new_head = optimal_solution(head.next)
    head.next.next = head
    head.next = None
    return new_head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3)))
    rev = optimal_solution(head)
    assert rev.val == 3
    assert rev.next.val == 2
    print("Done.")
""",

    "161_Detect_a_loop_in_LL.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/linked-list-cycle/
Problem Name: Linked List Cycle
Description: Detect if a linked list contains a loop/cycle.

Folder: LinkedList
File: 161_Detect_a_loop_in_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Tortoise and Hare. If there is a cycle, slow and fast pointers will meet.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head # loop back to head
    assert optimal_solution(head) == True
    print("Done.")
""",

    "162_Find_the_starting_point_in_LL.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/linked-list-cycle-ii/
Problem Name: Find starting point of loop in Linked List
Description: Find the node where the cycle begins. Return None if no cycle.

Folder: LinkedList
File: 162_Find_the_starting_point_in_LL.py
\"\"\"

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
""",

    "163_Length_of_loop_in_LL.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/find-length-of-loop/1
Problem Name: Find Length of Loop in Linked List
Description: Find the number of nodes inside the loop of a linked list.

Folder: LinkedList
File: 163_Length_of_loop_in_LL.py
\"\"\"

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
""",

    "164_Check_if_LL_is_palindrome_or_not.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/palindrome-linked-list/
Problem Name: Palindrome Linked List
Description: Check if a singly linked list is a palindrome.

Folder: LinkedList
File: 164_Check_if_LL_is_palindrome_or_not.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Find middle, reverse second half, compare both halves. Restore list if needed.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> bool:
    if not head or not head.next:
        return True
        
    # Find middle
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    # Reverse second half
    def reverse(node):
        prev = None
        curr = node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    second_head = reverse(slow.next)
    
    # Compare
    first = head
    second = second_head
    is_palindrome = True
    while second:
        if first.val != second.val:
            is_palindrome = False
            break
        first = first.next
        second = second.next
        
    # Restore (optional but good practice)
    slow.next = reverse(second_head)
    
    return is_palindrome

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert optimal_solution(head) == True
    
    head2 = ListNode(1, ListNode(2, ListNode(3)))
    assert optimal_solution(head2) == False
    print("Done.")
""",

    "165_Segregate_odd_and_even_nodes_in_Linked_List.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/odd-even-linked-list/
Problem Name: Odd Even Linked List
Description: Group all odd-indexed nodes together followed by the even-indexed nodes.

Folder: LinkedList
File: 165_Segregate_odd_and_even_nodes_in_Linked_List.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Maintain odd and even pointers. Link odd next to even.next, etc.
# Connect end of odd list to head of even list.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
        
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
        
    odd.next = even_head
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head)
    assert res.val == 1
    assert res.next.val == 3
    assert res.next.next.val == 5
    assert res.next.next.next.val == 2
    print("Done.")
""",

    "166_Remove_Nth_node_from_the_back_of_the_LL.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Problem Name: Remove Nth Node From End of List
Description: Remove the Nth node from the end of the list and return its head.

Folder: LinkedList
File: 166_Remove_Nth_node_from_the_back_of_the_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Fast pointer moves N steps first. Then move both fast and slow until fast reaches end.
# Slow will point to the node just before the target node to delete.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy
    
    for _ in range(n):
        fast = fast.next
        
    while fast.next:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    return dummy.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head, 2) # deletes 4
    assert res.next.next.next.val == 5
    print("Done.")
""",

    "167_Delete_the_middle_node_in_LL.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
Problem Name: Delete the Middle Node of a Linked List
Description: Delete the middle node of a linked list and return the modified head.

Folder: LinkedList
File: 167_Delete_the_middle_node_in_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Tortoise and Hare with a pointer tracking the node before slow.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
        
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = slow.next
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res = optimal_solution(head) # deletes 3
    assert res.next.next.val == 4
    print("Done.")
""",

    "168_Sort_LL.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/sort-list/
Problem Name: Sort List
Description: Sort a linked list in O(N log N) time using constant space complexity.

Folder: LinkedList
File: 168_Sort_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Merge Sort.
# Time Complexity: O(N log N)
# Space Complexity: O(log N) stack depth
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
        
    # Split list into two halves
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    prev.next = None # break the link
    
    left = optimal_solution(head)
    right = optimal_solution(slow)
    
    return merge_two_lists(left, right)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    res = optimal_solution(head)
    assert res.val == 1
    assert res.next.val == 2
    assert res.next.next.val == 3
    print("Done.")
""",

    "169_Sort_a_Linked_List_of_0s_1s_and_2s.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
Problem Name: Sort a Linked List of 0s, 1s, and 2s
Description: Sort a linked list of 0s, 1s, and 2s by changing links.

Folder: LinkedList
File: 169_Sort_a_Linked_List_of_0s_1s_and_2s.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Create three dummy lists for 0s, 1s, and 2s. Traverse and link nodes accordingly.
# Merge the three lists.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
        
    dummy0, dummy1, dummy2 = ListNode(0), ListNode(0), ListNode(0)
    p0, p1, p2 = dummy0, dummy1, dummy2
    
    curr = head
    while curr:
        if curr.val == 0:
            p0.next = curr
            p0 = p0.next
        elif curr.val == 1:
            p1.next = curr
            p1 = p1.next
        else:
            p2.next = curr
            p2 = p2.next
        curr = curr.next
        
    # Link lists
    p0.next = dummy1.next if dummy1.next else dummy2.next
    p1.next = dummy2.next
    p2.next = None
    
    return dummy0.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(0, ListNode(2, ListNode(1, ListNode(0))))))
    res = optimal_solution(head)
    assert res.val == 0
    assert res.next.val == 0
    assert res.next.next.val == 1
    print("Done.")
""",

    "170_Find_the_intersection_point_of_Y_LL.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
Problem Name: Intersection of Two Linked Lists
Description: Find the node where two singly linked lists intersect.

Folder: LinkedList
File: 170_Find_the_intersection_point_of_Y_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Initialize two pointers at heads. Move each pointer 1 step. 
# If one reaches None, redirect to the head of the other list. They will meet at intersection point.
# Time Complexity: O(N + M)
# Space Complexity: O(1)
def optimal_solution(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    intersect = ListNode(8, ListNode(4, ListNode(5)))
    headA = ListNode(4, ListNode(1, intersect))
    headB = ListNode(5, ListNode(0, ListNode(1, intersect)))
    
    res = optimal_solution(headA, headB)
    assert res is not None and res.val == 8
    print("Done.")
""",

    "171_Add_one_to_a_number_represented_by_LL.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
Problem Name: Add one to a number represented by LL
Description: Add 1 to the number represented by the linked list.

Folder: LinkedList
File: 171_Add_one_to_a_number_represented_by_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursively traverse to the end. Add carry as we backtrack.
# Time Complexity: O(N)
# Space Complexity: O(N) recursion stack
def optimal_solution(head: ListNode) -> ListNode:
    def helper(node):
        if not node:
            return 1 # carry to add
        carry = helper(node.next)
        node.val += carry
        if node.val >= 10:
            node.val = 0
            return 1
        return 0

    carry = helper(head)
    if carry:
        new_head = ListNode(1)
        new_head.next = head
        return new_head
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(4, ListNode(5, ListNode(9)))
    res = optimal_solution(head) # 459 + 1 = 460
    assert res.val == 4
    assert res.next.val == 6
    assert res.next.next.val == 0
    print("Done.")
""",

    "172_Add_two_numbers_in_Linked_List.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/add-two-numbers/
Problem Name: Add Two Numbers
Description: Add two numbers represented by two linked lists (digits stored in reverse order).

Folder: LinkedList
File: 172_Add_two_numbers_in_Linked_List.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(max(N, M))
# Space Complexity: O(max(N, M)) for new list
def optimal_solution(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    l1 = ListNode(2, ListNode(4, ListNode(3))) # 342
    l2 = ListNode(5, ListNode(6, ListNode(4))) # 465
    res = optimal_solution(l1, l2) # 807 (7 -> 0 -> 8)
    assert res.val == 7
    assert res.next.val == 0
    assert res.next.next.val == 8
    print("Done.")
""",

    "173_Delete_all_occurrences_of_a_key_in_DLL.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1
Problem Name: Delete all occurrences of a key in DLL
Description: Delete all nodes with key X from a Doubly Linked List.

Folder: LinkedList
File: 173_Delete_all_occurrences_of_a_key_in_DLL.py
\"\"\"

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode, x: int) -> DLLNode:
    curr = head
    while curr:
        if curr.val == x:
            if curr == head:
                head = head.next
                if head:
                    head.prev = None
            else:
                if curr.next:
                    curr.next.prev = curr.prev
                if curr.prev:
                    curr.prev.next = curr.next
        curr = curr.next
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(2)
    head.next = DLLNode(2, prev=head)
    head.next.next = DLLNode(10, prev=head.next)
    head.next.next.next = DLLNode(2, prev=head.next.next)
    
    new_head = optimal_solution(head, 2) # leaves only 10
    assert new_head.val == 10
    assert new_head.next is None
    print("Done.")
""",

    "174_Find_Pairs_with_Given_Sum_in_Doubly_Linked_List.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
Problem Name: Find pairs with given sum in sorted DLL
Description: Find all pairs in a sorted doubly linked list whose sum is equal to target.

Folder: LinkedList
File: 174_Find_Pairs_with_Given_Sum_in_Doubly_Linked_List.py
\"\"\"

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Two pointer approach. One starting at head, other at tail.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode, target: int) -> list[tuple[int, int]]:
    if not head:
        return []
        
    tail = head
    while tail.next:
        tail = tail.next
        
    pairs = []
    l, r = head, tail
    while l != r and r.next != l:
        curr_sum = l.val + r.val
        if curr_sum == target:
            pairs.append((l.val, r.val))
            l = l.next
            r = r.prev
        elif curr_sum < target:
            l = l.next
        else:
            r = r.prev
            
    return pairs

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(2, prev=head)
    head.next.next = DLLNode(4, prev=head.next)
    head.next.next.next = DLLNode(5, prev=head.next.next)
    head.next.next.next.next = DLLNode(6, prev=head.next.next.next)
    
    assert optimal_solution(head, 7) == [(1, 6), (2, 5)]
    print("Done.")
""",

    "175_Remove_duplicates_from_sorted_DLL.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1
Problem Name: Remove duplicates from sorted DLL
Description: Remove duplicates from a sorted doubly linked list in place.

Folder: LinkedList
File: 175_Remove_duplicates_from_sorted_DLL.py
\"\"\"

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: DLLNode) -> DLLNode:
    if not head:
        return None
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            # remove curr.next
            next_node = curr.next.next
            curr.next = next_node
            if next_node:
                next_node.prev = curr
        else:
            curr = curr.next
    return head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = DLLNode(1)
    head.next = DLLNode(1, prev=head)
    head.next.next = DLLNode(2, prev=head.next)
    
    new_head = optimal_solution(head)
    assert new_head.val == 1
    assert new_head.next.val == 2
    print("Done.")
""",

    "176_Reverse_LL_in_group_of_given_size_K.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
Problem Name: Reverse Nodes in k-Group
Description: Reverse nodes of a linked list k at a time.

Folder: LinkedList
File: 176_Reverse_LL_in_group_of_given_size_K.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Verify k nodes exist before reversing. Reverse them recursively or iteratively.
# Time Complexity: O(N)
# Space Complexity: O(N/K) recursion stack
def optimal_solution(head: ListNode, k: int) -> ListNode:
    # Check if there are k nodes left
    curr = head
    for _ in range(k):
        if not curr:
            return head
        curr = curr.next
        
    # Reverse k nodes
    prev = None
    curr = head
    for _ in range(k):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    head.next = optimal_solution(curr, k)
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head, 2) # (2->1->4->3->5)
    assert res.val == 2
    assert res.next.val == 1
    assert res.next.next.val == 4
    print("Done.")
""",

    "177_Rotate_a_LL.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/rotate-list/
Problem Name: Rotate List
Description: Rotate the linked list to the right by k places.

Folder: LinkedList
File: 177_Rotate_a_LL.py
\"\"\"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Join the tail of the list to the head to form a circular list.
# Then break the list after N - (k % N) elements.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head
        
    # Find length and tail node
    length = 1
    curr = head
    while curr.next:
        length += 1
        curr = curr.next
        
    curr.next = head # Make it circular
    
    k = k % length
    steps_to_new_tail = length - k
    
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = optimal_solution(head, 2) # (4->5->1->2->3)
    assert res.val == 4
    assert res.next.val == 5
    print("Done.")
""",

    "178_Flattening_of_LL.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
Problem Name: Flattening a Linked List
Description: Flatten a multi-level linked list where each node has a next and a bottom/child pointer.

Folder: LinkedList
File: 178_Flattening_of_LL.py
\"\"\"

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
""",

    "179_Clone_a_LL_with_random_and_next_pointer.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/copy-list-with-random-pointer/
Problem Name: Copy List with Random Pointer
Description: Deep copy a linked list where each node has a next and random pointer.

Folder: LinkedList
File: 179_Clone_a_LL_with_random_and_next_pointer.py
\"\"\"

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
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "LinkedList", "Code")
    os.makedirs(target_dir, exist_ok=True)
    
    # Remove README.py if it exists
    readme_py = os.path.join(target_dir, "README.py")
    if os.path.exists(readme_py):
        os.remove(readme_py)
        print("Removed temporary README.py")
        
    for filename, code in SOLUTIONS.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Populated {filename}")
        
    print("All LinkedList code solutions populated successfully!")

if __name__ == "__main__":
    main()
