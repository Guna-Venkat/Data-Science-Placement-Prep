import os

SOLUTIONS = {
    "335_Introduction_to_BST.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/binary-search-trees/1
Problem Name: Binary Search Trees (Introduction)
Description: Check if the given keys can represent the level order / properties of a BST.
Specifically, check if left < root < right for a simple BST definition.

Folder: Binary_Search_Trees
File: 335_Introduction_to_BST.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: In a BST, the left subtree contains keys smaller than root, 
# and right subtree contains keys larger than root.
# Given a sorted array, can it represent a valid BST? Yes, any sorted array can be turned into a BST.
# But if it's not sorted, check if elements are sorted for inorder.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> bool:
    # Check if array is strictly sorted in ascending order (no duplicates allowed in standard strict BST)
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 5, 8]) == True
    assert optimal_solution([1, 3, 2]) == False
    print("Done.")
""",

    "336_Search_in_a_Binary_Search_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
Problem Name: Search in a Binary Search Tree
Description: Find the node in the BST that the node's value equals val and return that subtree.

Folder: Binary_Search_Trees
File: 336_Search_in_a_Binary_Search_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If val < root.val, search left; if val > root.val, search right.
# Time Complexity: O(H) where H is height of the tree.
# Space Complexity: O(1) iterative
def optimal_solution(root: TreeNode, val: int) -> TreeNode:
    curr = root
    while curr is not None and curr.val != val:
        if val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return curr

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # Tree:
    #      4
    #     / \
    #    2   7
    #   / \
    #  1   3
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)
    
    res = optimal_solution(root, 2)
    assert res is not None and res.val == 2
    assert res.left.val == 1
    
    res_none = optimal_solution(root, 5)
    assert res_none is None
    print("Done.")
""",

    "337_Find_Min_Max_in_BST.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1
Problem Name: Minimum and Maximum in BST
Description: Find the minimum and maximum elements in a BST.

Folder: Binary_Search_Trees
File: 337_Find_Min_Max_in_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep moving left to find the minimum; keep moving right to find the maximum.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_min(root: TreeNode) -> int:
    if root is None:
        return -1
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr.val

def find_max(root: TreeNode) -> int:
    if root is None:
        return -1
    curr = root
    while curr.right is not None:
        curr = curr.right
    return curr.val

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(1), TreeNode(4))
    root.right = TreeNode(8, TreeNode(6), TreeNode(9))
    
    assert find_min(root) == 1
    assert find_max(root) == 9
    print("Done.")
""",

    "338_Ceil_in_a_BST.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
Problem Name: Ceil in BST
Description: Find ceil of X (smallest node value >= X) in a BST.

Folder: Binary_Search_Trees
File: 338_Ceil_in_a_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If root.val >= X, root is a potential ceil. Move to left child.
# If root.val < X, move to right child.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_ceil(root: TreeNode, x: int) -> int:
    ceil = -1
    curr = root
    while curr:
        if curr.val == x:
            return curr.val
        if curr.val > x:
            ceil = curr.val
            curr = curr.left
        else:
            curr = curr.right
    return ceil

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(8)
    root.left = TreeNode(4, TreeNode(2), TreeNode(6))
    root.right = TreeNode(12, TreeNode(10), TreeNode(14))
    
    assert find_ceil(root, 11) == 12
    assert find_ceil(root, 3) == 4
    assert find_ceil(root, 15) == -1
    print("Done.")
""",

    "339_Floor_in_a_BST.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/floor-in-bst/1
Problem Name: Floor in BST
Description: Find floor of X (largest node value <= X) in a BST.

Folder: Binary_Search_Trees
File: 339_Floor_in_a_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If root.val <= X, root is a potential floor. Move to right child.
# If root.val > X, move to left child.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_floor(root: TreeNode, x: int) -> int:
    floor = -1
    curr = root
    while curr:
        if curr.val == x:
            return curr.val
        if curr.val < x:
            floor = curr.val
            curr = curr.right
        else:
            curr = curr.left
    return floor

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(8)
    root.left = TreeNode(4, TreeNode(2), TreeNode(6))
    root.right = TreeNode(12, TreeNode(10), TreeNode(14))
    
    assert find_floor(root, 11) == 10
    assert find_floor(root, 3) == 2
    assert find_floor(root, 1) == -1
    print("Done.")
""",

    "340_Insert_a_given_Node_in_BST.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
Problem Name: Insert into a Binary Search Tree
Description: Insert a value into the BST and return the root of the modified BST.

Folder: Binary_Search_Trees
File: 340_Insert_a_given_Node_in_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Move down the tree. If val < curr.val, go left; else go right.
# Insert at the first encountered None location.
# Time Complexity: O(H)
# Space Complexity: O(1)
def optimal_solution(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = TreeNode(val)
                break
            else:
                curr = curr.left
        else:
            if curr.right is None:
                curr.right = TreeNode(val)
                break
            else:
                curr = curr.right
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)
    
    new_root = optimal_solution(root, 5)
    assert new_root.right.left.val == 5
    print("Done.")
""",

    "341_Delete_a_Node_in_BST.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/delete-node-in-a-bst/
Problem Name: Delete Node in a BST
Description: Delete a node with the given key from the BST.

Folder: Binary_Search_Trees
File: 341_Delete_a_Node_in_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Search for the node. Once found:
# - If node has 0 or 1 child, replace with child.
# - If node has 2 children, find inorder successor (min of right child), 
#   replace node value with successor value, and delete successor.
# Time Complexity: O(H)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None
        
    if key < root.val:
        root.left = optimal_solution(root.left, key)
    elif key > root.val:
        root.right = optimal_solution(root.right, key)
    else:
        # Case 1 & 2: 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
            
        # Case 3: 2 children. Find min in right subtree.
        curr = root.right
        while curr.left:
            curr = curr.left
            
        root.val = curr.val
        root.right = optimal_solution(root.right, curr.val)
        
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6, None, TreeNode(7))
    
    new_root = optimal_solution(root, 3)
    # 3 is deleted, either 4 or 2 takes its place
    assert new_root.left.val == 4 or new_root.left.val == 2
    print("Done.")
""",

    "342_Find_Kth_smallest_largest_element_in_BST.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Problem Name: Kth Smallest/Largest Element in BST
Description: Find the Kth smallest and Kth largest elements in a BST.

Folder: Binary_Search_Trees
File: 342_Find_Kth_smallest_largest_element_in_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Inorder traversal goes in sorted order. We can run iterative inorder
# using a stack and count up to K.
# Time Complexity: O(N) worst-case
# Space Complexity: O(H) stack
def kth_smallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root
    count = 0
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right
    return -1

def get_node_count(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + get_node_count(root.left) + get_node_count(root.right)

def kth_largest(root: TreeNode, k: int) -> int:
    # Kth largest is (N - k + 1)th smallest
    n = get_node_count(root)
    return kth_smallest(root, n - k + 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6)
    
    assert kth_smallest(root, 1) == 2
    assert kth_smallest(root, 3) == 4
    assert kth_largest(root, 1) == 6
    print("Done.")
""",

    "343_Check_if_a_tree_is_BST_or_not.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/validate-binary-search-tree/
Problem Name: Validate Binary Search Tree
Description: Check if a binary tree is a valid BST.

Folder: Binary_Search_Trees
File: 343_Check_if_a_tree_is_BST_or_not.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Define a valid range [min_val, max_val] for each node.
# For left child, update max_val to node.val. For right child, update min_val to node.val.
# Time Complexity: O(N)
# Space Complexity: O(H) stack
def optimal_solution(root: TreeNode) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

    return validate(root, -float('inf'), float('inf'))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert optimal_solution(root) == True
    
    invalid = TreeNode(5)
    invalid.left = TreeNode(1)
    invalid.right = TreeNode(4, TreeNode(3), TreeNode(6))
    assert optimal_solution(invalid) == False
    print("Done.")
""",

    "344_LCA_in_BST.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Problem Name: Lowest Common Ancestor of a Binary Search Tree
Description: Find the LCA of two given nodes in the BST.

Folder: Binary_Search_Trees
File: 344_LCA_in_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Since it is a BST, if p and q are both smaller than root, LCA is in left subtree.
# If both are larger, LCA is in right subtree. Otherwise, root itself is the split point (LCA).
# Time Complexity: O(H)
# Space Complexity: O(1) iterative
def optimal_solution(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    p = TreeNode(2)
    q = TreeNode(8)
    root = TreeNode(6)
    root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    root.right = TreeNode(8, TreeNode(7), TreeNode(9))
    
    lca = optimal_solution(root, root.left, root.right)
    assert lca.val == 6
    print("Done.")
""",

    "345_Construct_BST_from_preorder_traversal.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
Problem Name: Construct BST from Preorder Traversal
Description: Construct a BST from its preorder traversal array.

Folder: Binary_Search_Trees
File: 345_Construct_BST_from_preorder_traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Move index pointers sequentially using an upper bound tracker.
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(preorder: list[int]) -> TreeNode:
    idx = 0
    
    def build(upper_bound):
        nonlocal idx
        if idx >= len(preorder) or preorder[idx] > upper_bound:
            return None
            
        root_val = preorder[idx]
        root = TreeNode(root_val)
        idx += 1
        
        root.left = build(root_val)
        root.right = build(upper_bound)
        return root

    return build(float('inf'))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([8, 5, 1, 7, 10, 12])
    assert res.val == 8
    assert res.left.val == 5
    assert res.left.right.val == 7
    print("Done.")
""",

    "346_Inorder_Successor_Predecessor_in_BST.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/predecessor-and-successor/1
Problem Name: Inorder Predecessor and Successor
Description: Find the inorder predecessor and successor of a given key in BST.

Folder: Binary_Search_Trees
File: 346_Inorder_Successor_Predecessor_in_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# - Successor: Smallest value strictly greater than key. If curr.val > key, 
#   curr is potential successor, move to left child. Else move to right.
# - Predecessor: Largest value strictly less than key. If curr.val < key,
#   curr is potential predecessor, move to right child. Else move to left.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_pre_suc(root: TreeNode, key: int) -> tuple[int, int]:
    pre = -1
    suc = -1
    
    # Successor search
    curr = root
    while curr:
        if curr.val > key:
            suc = curr.val
            curr = curr.left
        else:
            curr = curr.right
            
    # Predecessor search
    curr = root
    while curr:
        if curr.val < key:
            pre = curr.val
            curr = curr.right
        else:
            curr = curr.left
            
    return pre, suc

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(8)
    root.left = TreeNode(4, TreeNode(2), TreeNode(6))
    root.right = TreeNode(12, TreeNode(10), TreeNode(14))
    
    pre, suc = find_pre_suc(root, 8)
    assert pre == 6 and suc == 10
    print("Done.")
""",

    "347_Binary_Search_Tree_Iterator.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-search-tree-iterator/
Problem Name: BST Iterator
Description: Implement an iterator over a BST that represents in-order traversal.

Folder: Binary_Search_Trees
File: 347_Binary_Search_Tree_Iterator.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Initialize with stack, push all left children.
# next() pops element and pushes all left children of its right child.
# Time Complexity: O(1) amortized
# Space Complexity: O(H)
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_all_left(root)
        
    def _push_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_all_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15, TreeNode(9), TreeNode(20))
    
    iterator = BSTIterator(root)
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    print("Done.")
""",

    "348_Two_Sum_In_BST_or_Find_a_pair_with_given_sum_in_BST.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Problem Name: Two Sum IV - Input is a BST
Description: Find if there exist two elements in the BST such that their sum is equal to target.

Folder: Binary_Search_Trees
File: 348_Two_Sum_In_BST_or_Find_a_pair_with_given_sum_in_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Initialize two stacks for iterative traversals (next and before).
# Perform standard two-pointer search.
# Time Complexity: O(N)
# Space Complexity: O(H)
class BSTIterator:
    def __init__(self, root: TreeNode, is_reverse: bool):
        self.stack = []
        self.is_reverse = is_reverse
        self._push(root)
        
    def _push(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.is_reverse else node.left
            
    def next_val(self) -> int:
        node = self.stack.pop()
        self._push(node.left if self.is_reverse else node.right)
        return node.val

def find_target(root: TreeNode, k: int) -> bool:
    if not root:
        return False
    left_iter = BSTIterator(root, False)
    right_iter = BSTIterator(root, True)
    
    l = left_iter.next_val()
    r = right_iter.next_val()
    
    while l < r:
        curr_sum = l + r
        if curr_sum == k:
            return True
        elif curr_sum < k:
            l = left_iter.next_val()
        else:
            r = right_iter.next_val()
            
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6, None, TreeNode(7))
    
    assert find_target(root, 9) == True
    assert find_target(root, 28) == False
    print("Done.")
""",

    "349_Recover_BST.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/recover-binary-search-tree/
Problem Name: Recover Binary Search Tree
Description: Recover a BST where exactly two nodes were swapped.

Folder: Binary_Search_Trees
File: 349_Recover_BST.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Inorder traversal. Keep track of current, previous, and violating elements.
# Swap values of the two elements violating order.
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode) -> TreeNode:
    first = None
    middle = None
    last = None
    prev = TreeNode(-float('inf'))
    
    def inorder(node):
        nonlocal first, middle, last, prev
        if not node:
            return
            
        inorder(node.left)
        
        # Check violation
        if node.val < prev.val:
            if not first:
                first = prev
                middle = node
            else:
                last = node
                
        prev = node
        inorder(node.right)

    inorder(root)
    
    if first and last:
        first.val, last.val = last.val, first.val
    elif first and middle:
        first.val, middle.val = middle.val, first.val
        
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # Swapped 1 and 3 in standard BST [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(3, None, TreeNode(2))
    
    recovered = optimal_solution(root)
    assert recovered.val == 3
    assert recovered.left.val == 1
    print("Done.")
""",

    "350_Largest_BST_in_Binary_Tree.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/largest-bst/1
Problem Name: Largest BST in Binary Tree
Description: Given a Binary Tree, find the size of the largest subtree which is a BST.

Folder: Binary_Search_Trees
File: 350_Largest_BST_in_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Postorder traversal. Return (is_bst, size, min_val, max_val) from child nodes.
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    def dfs(node):
        # returns: (is_bst, size, min_val, max_val)
        if not node:
            return True, 0, float('inf'), -float('inf')
            
        left_is_bst, left_size, left_min, left_max = dfs(node.left)
        right_is_bst, right_size, right_min, right_max = dfs(node.right)
        
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            curr_size = 1 + left_size + right_size
            curr_min = min(node.val, left_min)
            curr_max = max(node.val, right_max)
            return True, curr_size, curr_min, curr_max
            
        return False, max(left_size, right_size), -float('inf'), float('inf')

    return dfs(root)[1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(4) # invalid BST on right subtree
    
    # Left subtree is a BST of size 3 (nodes 1, 2, 3)
    assert optimal_solution(root) == 3
    print("Done.")
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "Binary_Search_Trees", "Code")
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
        
    print("All BST code solutions populated successfully!")

if __name__ == "__main__":
    main()
