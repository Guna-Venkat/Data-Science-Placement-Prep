import os

SOLUTIONS = {
    "297_Introduction_to_Trees.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-trees/1
Problem Name: Introduction to Trees
Description: Given level i of a binary tree, find the maximum number of nodes possible at that level.

Folder: Binary_Trees
File: 297_Introduction_to_Trees.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Number of nodes at level i is 2^(i-1) if level is 1-indexed.
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(i: int) -> int:
    if i <= 0:
        return 0
    return 2 ** (i - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(5) == 16
    assert optimal_solution(1) == 1
    print("Done.")
""",

    "298_Binary_Tree_Representation_in_Java.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/binary-tree-representation/1
Problem Name: Binary Tree Representation
Description: Build a binary tree representation. Return root.

Folder: Binary_Trees
File: 298_Binary_Tree_Representation_in_Java.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(arr: list[int]) -> TreeNode:
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        curr = queue.pop(0)
        if i < len(arr):
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
            i += 1
        if i < len(arr):
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
            i += 1
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = optimal_solution([1, 2, 3, 4, 5])
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    print("Done.")
""",

    "299_Pre_Post_Inorder_in_one_traversal.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/tree-traversals_981269
Problem Name: Preorder, Inorder, and Postorder in One Traversal
Description: Return pre, in, and post order traversals of a tree in a single DFS traversal.

Folder: Binary_Trees
File: 299_Pre_Post_Inorder_in_one_traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode) -> tuple[list[int], list[int], list[int]]:
    pre_order = []
    in_order = []
    post_order = []
    
    def dfs(node):
        if not node:
            return
        pre_order.append(node.val)
        dfs(node.left)
        in_order.append(node.val)
        dfs(node.right)
        post_order.append(node.val)

    dfs(root)
    return pre_order, in_order, post_order

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    pre, ino, post = optimal_solution(root)
    assert pre == [1, 2, 3]
    assert ino == [2, 1, 3]
    assert post == [2, 3, 1]
    print("Done.")
""",

    "300_Preorder_Traversal.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Problem Name: Binary Tree Preorder Traversal
Description: Recursive preorder traversal.

Folder: Binary_Trees
File: 300_Preorder_Traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    def preorder(node):
        if not node:
            return
        res.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 2, 3]
    print("Done.")
""",

    "301_Inorder_Traversal_of_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Problem Name: Binary Tree Inorder Traversal
Description: Recursive inorder traversal.

Folder: Binary_Trees
File: 301_Inorder_Traversal_of_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 3, 2]
    print("Done.")
""",

    "302_Postorder_Traversal.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Problem Name: Binary Tree Postorder Traversal
Description: Recursive postorder traversal.

Folder: Binary_Trees
File: 302_Postorder_Traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        res.append(node.val)
    postorder(root)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [3, 2, 1]
    print("Done.")
""",

    "303_Level_Order_Traversal.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
Problem Name: Binary Tree Level Order Traversal
Description: Level order (BFS) traversal of a binary tree.

Folder: Binary_Trees
File: 303_Level_Order_Traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == [[3], [9, 20], [15, 7]]
    print("Done.")
""",

    "304_Iterative_Preorder_Traversal_of_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Problem Name: Iterative Preorder Traversal
Description: Preorder traversal using stack.

Folder: Binary_Trees
File: 304_Iterative_Preorder_Traversal_of_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H) stack space
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 2, 3]
    print("Done.")
""",

    "305_Iterative_Inorder_Traversal_of_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Problem Name: Iterative Inorder Traversal
Description: Inorder traversal using stack.

Folder: Binary_Trees
File: 305_Iterative_Inorder_Traversal_of_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H) stack space
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 3, 2]
    print("Done.")
""",

    "306_Post_order_Traversal_of_Binary_Tree_using_2_stack.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Problem Name: Iterative Postorder Traversal using 2 Stacks
Description: Postorder traversal using two stacks.

Folder: Binary_Trees
File: 306_Post_order_Traversal_of_Binary_Tree_using_2_stack.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Push root to stack1. Pop stack1, push to stack2.
# Push left child, then right child to stack1.
# Pop all from stack2.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    s1 = [root]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left: s1.append(node.left)
        if node.right: s1.append(node.right)
    while s2:
        res.append(s2.pop().val)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [3, 2, 1]
    print("Done.")
""",

    "307_Post_order_Traversal_of_Binary_Tree_using_1_stack.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Problem Name: Iterative Postorder Traversal using 1 Stack
Description: Postorder traversal using a single stack.

Folder: Binary_Trees
File: 307_Post_order_Traversal_of_Binary_Tree_using_1_stack.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    stack = []
    curr = root
    last_visited = None
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        peek_node = stack[-1]
        if peek_node.right and last_visited != peek_node.right:
            curr = peek_node.right
        else:
            res.append(peek_node.val)
            last_visited = stack.pop()
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [3, 2, 1]
    print("Done.")
""",

    "308_Preorder_Inorder_and_Postorder_Traversal_in_one_Traversal.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/tree-traversals_981269
Problem Name: Tree traversals in one traversal iterative
Description: Iterative pre, in, and post order traversal in one traversal using a single stack storing tuples of (node, state).

Folder: Binary_Trees
File: 308_Preorder_Inorder_and_Postorder_Traversal_in_one_Traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H) stack space
def optimal_solution(root: TreeNode) -> tuple[list[int], list[int], list[int]]:
    if not root:
        return [], [], []
        
    pre = []
    ino = []
    post = []
    stack = [[root, 1]] # 1: pre, 2: in, 3: post
    
    while stack:
        it = stack[-1]
        node, state = it[0], it[1]
        if state == 1:
            pre.append(node.val)
            it[1] += 1
            if node.left:
                stack.append([node.left, 1])
        elif state == 2:
            ino.append(node.val)
            it[1] += 1
            if node.right:
                stack.append([node.right, 1])
        else:
            post.append(node.val)
            stack.pop()
            
    return pre, ino, post

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    pre, ino, post = optimal_solution(root)
    assert pre == [1, 2, 3]
    assert ino == [2, 1, 3]
    assert post == [2, 3, 1]
    print("Done.")
""",

    "309_Maximum_Depth_in_BT.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Problem Name: Maximum Depth of Binary Tree
Description: Find the maximum depth of a binary tree.

Folder: Binary_Trees
File: 309_Maximum_Depth_in_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(optimal_solution(root.left), optimal_solution(root.right))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == 3
    print("Done.")
""",

    "310_Check_for_balanced_binary_tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/balanced-binary-tree/
Problem Name: Balanced Binary Tree
Description: Check if a binary tree is height-balanced (height difference of left and right subtrees <= 1).

Folder: Binary_Trees
File: 310_Check_for_balanced_binary_tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Bottom-up height check. Return -1 if unbalanced, otherwise return tree height.
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> bool:
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1: return -1
        right = check(node.right)
        if right == -1: return -1
        
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == True
    
    unbalanced = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert optimal_solution(unbalanced) == False
    print("Done.")
""",

    "311_Diameter_of_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/diameter-of-binary-tree/
Problem Name: Diameter of Binary Tree
Description: Find the length of the longest path between any two nodes.

Folder: Binary_Trees
File: 311_Diameter_of_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Return height, update global max diameter with (left_height + right_height).
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    diameter = 0
    
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert optimal_solution(root) == 3
    print("Done.")
""",

    "312_Maximum_path_sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Problem Name: Binary Tree Maximum Path Sum
Description: Find the maximum path sum of any non-empty path.

Folder: Binary_Trees
File: 312_Maximum_path_sum.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: DFS function returns maximum path sum starting from node going down.
# Ignore negative path sums. Update max sum with (left + right + node.val).
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    max_sum = -float('inf')
    
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        max_sum = max(max_sum, left + right + node.val)
        return node.val + max(left, right)

    dfs(root)
    return max_sum

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == 42
    print("Done.")
""",

    "313_Check_if_two_trees_are_identical_or_not.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/same-tree/
Problem Name: Same Tree
Description: Check if two binary trees are identical.

Folder: Binary_Trees
File: 313_Check_if_two_trees_are_identical_or_not.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return optimal_solution(p.left, q.left) and optimal_solution(p.right, q.right)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert optimal_solution(t1, t2) == True
    print("Done.")
""",

    "314_Zig_Zag_or_Spiral_Traversal.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Problem Name: Binary Tree Zigzag Level Order Traversal
Description: Level order traversal in spiral form.

Folder: Binary_Trees
File: 314_Zig_Zag_or_Spiral_Traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    result = []
    queue = [root]
    left_to_right = True
    while queue:
        level_size = len(queue)
        level = [0] * level_size
        for i in range(level_size):
            node = queue.pop(0)
            idx = i if left_to_right else (level_size - 1 - i)
            level[idx] = node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
        left_to_right = not left_to_right
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == [[3], [20, 9], [15, 7]]
    print("Done.")
""",

    "315_Boundary_Traversal.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
Problem Name: Boundary Traversal of Binary Tree
Description: Return boundary elements of a binary tree in anti-clockwise order.

Folder: Binary_Trees
File: 315_Boundary_Traversal.py
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
# 1. Left boundary (excluding leaves).
# 2. Leaf nodes.
# 3. Right boundary in reverse (excluding leaves).
# Time Complexity: O(N)
# Space Complexity: O(H) stack depth
def is_leaf(node):
    return not node.left and not node.right

def add_left_boundary(root, res):
    curr = root.left
    while curr:
        if not is_leaf(curr):
            res.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def add_leaves(node, res):
    if not node:
        return
    if is_leaf(node):
        res.append(node.val)
        return
    add_leaves(node.left, res)
    add_leaves(node.right, res)

def add_right_boundary(root, res):
    curr = root.right
    temp = []
    while curr:
        if not is_leaf(curr):
            temp.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    res.extend(temp[::-1])

def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    if not is_leaf(root):
        res.append(root.val)
    add_left_boundary(root, res)
    add_leaves(root, res)
    add_right_boundary(root, res)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4)))
    # root (1) -> left boundary (none) -> leaves (3, 4) -> right boundary (2)
    assert optimal_solution(root) == [1, 3, 4, 2]
    print("Done.")
""",

    "316_Vertical_Order_Traversal.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Problem Name: Vertical Order Traversal of a Binary Tree
Description: Vertical level order traversal (sorted by column, level, then value).

Folder: Binary_Trees
File: 316_Vertical_Order_Traversal.py
\"\"\"

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep column and row indices. Sort values of nodes at same coordinates.
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    nodes = collections.defaultdict(list)
    # BFS
    queue = [(root, 0, 0)] # node, col, row
    while queue:
        node, col, row = queue.pop(0)
        nodes[col].append((row, node.val))
        if node.left: queue.append((node.left, col - 1, row + 1))
        if node.right: queue.append((node.right, col + 1, row + 1))
        
    result = []
    for col in sorted(nodes.keys()):
        # Sort by row index first, then by node value
        column_nodes = sorted(nodes[col], key=lambda x: (x[0], x[1]))
        result.append([val for row, val in column_nodes])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == [[9], [3, 15], [20], [7]]
    print("Done.")
""",

    "317_Top_View_of_BT.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
Problem Name: Top View of Binary Tree
Description: Print top view of a binary tree.

Folder: Binary_Trees
File: 317_Top_View_of_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of horizontal distance. Record first node visited at each distance using BFS.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    top_map = {} # col -> val
    # queue contains (node, col)
    queue = [(root, 0)]
    while queue:
        node, col = queue.pop(0)
        if col not in top_map:
            top_map[col] = node.val
        if node.left: queue.append((node.left, col - 1))
        if node.right: queue.append((node.right, col + 1))
        
    return [top_map[col] for col in sorted(top_map.keys())]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(6)))
    assert optimal_solution(root) == [2, 1, 3, 6]
    print("Done.")
""",

    "318_Bottom_view_of_BT.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
Problem Name: Bottom View of Binary Tree
Description: Print bottom view of a binary tree.

Folder: Binary_Trees
File: 318_Bottom_view_of_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of horizontal distance. Record last node visited at each distance using BFS.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    bottom_map = {} # col -> val
    queue = [(root, 0)]
    while queue:
        node, col = queue.pop(0)
        bottom_map[col] = node.val
        if node.left: queue.append((node.left, col - 1))
        if node.right: queue.append((node.right, col + 1))
        
    return [bottom_map[col] for col in sorted(bottom_map.keys())]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(6)))
    assert optimal_solution(root) == [2, 5, 3, 6]
    print("Done.")
""",

    "319_RightLeft_View_of_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-right-side-view/
Problem Name: Right and Left View of Binary Tree
Description: Return right and left views of binary tree.

Folder: Binary_Trees
File: 319_RightLeft_View_of_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursive DFS keeping track of level. First node visited at that level in Root-Right-Left
# is right view; Root-Left-Right is left view.
# Time Complexity: O(N)
# Space Complexity: O(H)
def right_view(root: TreeNode) -> list[int]:
    res = []
    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    dfs(root, 0)
    return res

def left_view(root: TreeNode) -> list[int]:
    res = []
    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    dfs(root, 0)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_view(root) == [1, 3, 4]
    assert left_view(root) == [1, 2, 5]
    print("Done.")
""",

    "320_Symmetric_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/symmetric-tree/
Problem Name: Symmetric Tree
Description: Check if a binary tree is symmetric (mirror image of itself).

Folder: Binary_Trees
File: 320_Symmetric_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> bool:
    if not root:
        return True
        
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and 
                is_mirror(t1.left, t2.right) and 
                is_mirror(t1.right, t2.left))

    return is_mirror(root.left, root.right)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert optimal_solution(root) == True
    print("Done.")
""",

    "321_Print_root_to_leaf_path_in_BT.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1
Problem Name: Root to Leaf Paths
Description: Find all paths from root to leaf nodes.

Folder: Binary_Trees
File: 321_Print_root_to_leaf_path_in_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> list[list[int]]:
    result = []
    
    def dfs(node, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            result.append(list(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()

    dfs(root, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert optimal_solution(root) == [[1, 2, 4], [1, 2, 5], [1, 3]]
    print("Done.")
""",

    "322_LCA_in_BT.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Problem Name: Lowest Common Ancestor of a Binary Tree
Description: Find the LCA of two nodes p and q in a binary tree.

Folder: Binary_Trees
File: 322_LCA_in_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
        
    left = optimal_solution(root.left, p, q)
    right = optimal_solution(root.right, p, q)
    
    if left and right:
        return root
    return left or right

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    p = TreeNode(5)
    q = TreeNode(1)
    root = TreeNode(3, p, q)
    assert optimal_solution(root, p, q) == root
    print("Done.")
""",

    "323_Maximum_Width_of_BT.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
Problem Name: Maximum Width of Binary Tree
Description: Find the maximum width of a binary tree. Width is number of nodes in level between end nodes (including nulls).

Folder: Binary_Trees
File: 323_Maximum_Width_of_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Assign 0-based index to each node. For node at idx: left child is 2*idx, right is 2*idx + 1.
# Width of level is (last_idx - first_idx + 1).
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> int:
    if not root:
        return 0
    max_width = 0
    # queue holds (node, idx)
    queue = [(root, 0)]
    while queue:
        level_size = len(queue)
        min_idx = queue[0][1]
        first_idx = 0
        last_idx = 0
        for i in range(level_size):
            node, idx = queue.pop(0)
            curr_idx = idx - min_idx # prevent integer overflow
            if i == 0: first_idx = curr_idx
            if i == level_size - 1: last_idx = curr_idx
            if node.left: queue.append((node.left, 2 * curr_idx))
            if node.right: queue.append((node.right, 2 * curr_idx + 1))
        max_width = max(max_width, last_idx - first_idx + 1)
    return max_width

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    assert optimal_solution(root) == 4
    print("Done.")
""",

    "324_Children_Sum_Property_in_Binary_Tree.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/childrensumproperty_790775
Problem Name: Children Sum Property in Binary Tree
Description: Convert a binary tree such that each node's value equals sum of children's values. Incrementing only.

Folder: Binary_Trees
File: 324_Children_Sum_Property_in_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode):
    if not root or (not root.left and not root.right):
        return
        
    child_sum = 0
    if root.left: child_sum += root.left.val
    if root.right: child_sum += root.right.val
    
    if child_sum >= root.val:
        root.val = child_sum
    else:
        # propagate parent's value down to prevent node deficit
        if root.left: root.left.val = root.val
        if root.right: root.right.val = root.val
        
    optimal_solution(root.left)
    optimal_solution(root.right)
    
    total = 0
    if root.left: total += root.left.val
    if root.right: total += root.right.val
    if root.left or root.right:
        root.val = total

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(2, TreeNode(35, TreeNode(2), TreeNode(3)), TreeNode(10, TreeNode(5), TreeNode(2)))
    optimal_solution(root)
    # verify root val equals children sum
    assert root.val == root.left.val + root.right.val
    print("Done.")
""",

    "325_Print_all_nodes_at_a_distance_of_K_in_BT.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
Problem Name: All Nodes Distance K in Binary Tree
Description: Find all nodes at distance K from a target node.

Folder: Binary_Trees
File: 325_Print_all_nodes_at_a_distance_of_K_in_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep parent pointers. Run BFS from target in 3 directions (left, right, parent).
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    parents = {}
    
    # 1. Map parent pointers
    def map_parents(node, parent=None):
        if not node:
            return
        parents[node] = parent
        map_parents(node.left, node)
        map_parents(node.right, node)
        
    map_parents(root)
    
    # 2. BFS from target
    queue = [(target, 0)]
    visited = {target}
    result = []
    
    while queue:
        node, dist = queue.pop(0)
        if dist == k:
            result.append(node.val)
            continue
            
        for neighbor in (node.left, node.right, parents[node]):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
    
    res = optimal_solution(root, target, 2)
    assert sorted(res) == sorted([7, 4, 1])
    print("Done.")
""",

    "326_Minimum_time_taken_to_burn_the_BT_from_a_given_Node.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/burning-tree/1
Problem Name: Burning Tree
Description: Find the minimum time to burn the entire tree starting from a target node.

Folder: Binary_Trees
File: 326_Minimum_time_taken_to_burn_the_BT_from_a_given_Node.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: DFS/BFS keeping parents map. Run BFS level-by-level from target.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode, target_val: int) -> int:
    parents = {}
    target_node = None
    
    def find_and_map(node, parent=None):
        nonlocal target_node
        if not node:
            return
        if node.val == target_val:
            target_node = node
        parents[node] = parent
        find_and_map(node.left, node)
        find_and_map(node.right, node)

    find_and_map(root)
    
    # BFS
    queue = [(target_node, 0)]
    visited = {target_node}
    max_time = 0
    
    while queue:
        node, time = queue.pop(0)
        max_time = max(max_time, time)
        
        for neighbor in (node.left, node.right, parents[node]):
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, time + 1))
                
    return max_time

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    target = TreeNode(8)
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, target))
    assert optimal_solution(root, 8) == 3
    print("Done.")
""",

    "327_Count_total_nodes_in_a_complete_BT.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/count-complete-tree-nodes/
Problem Name: Count Complete Tree Nodes
Description: Count nodes in a complete binary tree in less than O(N) time.

Folder: Binary_Trees
File: 327_Count_total_nodes_in_a_complete_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If left height equals right height, tree is perfect: count is 2^height - 1.
# Else recurse left and right.
# Time Complexity: O((log N)^2)
# Space Complexity: O(log N)
def optimal_solution(root: TreeNode) -> int:
    if not root:
        return 0
        
    def get_left_height(node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def get_right_height(node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h

    lh = get_left_height(root)
    rh = get_right_height(root)
    
    if lh == rh:
        return (1 << lh) - 1
        
    return 1 + optimal_solution(root.left) + optimal_solution(root.right)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert optimal_solution(root) == 6
    print("Done.")
""",

    "328_Requirements_needed_to_construct_a_unique_BT.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/unique-binary-tree-requirements/1
Problem Name: Unique Binary Tree Requirements
Description: Given two traversals, determine if they can form a unique binary tree.

Folder: Binary_Trees
File: 328_Requirements_needed_to_construct_a_unique_BT.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: A unique binary tree can be constructed if one traversal is INORDER, 
# and the other is either PREORDER or POSTORDER.
# Code representation: 1 = Preorder, 2 = Inorder, 3 = Postorder.
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(t1: int, t2: int) -> bool:
    # 2 represents Inorder. We need Inorder along with Preorder (1) or Postorder (3)
    if (t1 == 2 and t2 == 1) or (t1 == 1 and t2 == 2):
        return True
    if (t1 == 2 and t2 == 3) or (t1 == 3 and t2 == 2):
        return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(2, 1) == True
    assert optimal_solution(1, 3) == False
    print("Done.")
""",

    "329_Construct_a_BT_from_Preorder_and_Inorder.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Problem Name: Construct Binary Tree from Preorder and Inorder Traversal
Description: Construct binary tree from preorder and inorder arrays.

Folder: Binary_Trees
File: 329_Construct_a_BT_from_Preorder_and_Inorder.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Preorder first element is root. Find its position in Inorder to split left/right subtrees.
# Time Complexity: O(N)
# Space Complexity: O(N) mapping
def optimal_solution(preorder: list[int], inorder: list[int]) -> TreeNode:
    in_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0
    
    def build(in_start, in_end):
        nonlocal pre_idx
        if in_start > in_end:
            return None
            
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)
        pre_idx += 1
        
        root_idx = in_map[root_val]
        root.left = build(in_start, root_idx - 1)
        root.right = build(root_idx + 1, in_end)
        return root

    return build(0, len(inorder) - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    root = optimal_solution(pre, ino)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    print("Done.")
""",

    "330_Construct_the_Binary_Tree_from_Postorder_and_Inorder_Traversal.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Problem Name: Construct Binary Tree from Inorder and Postorder Traversal
Description: Construct binary tree from postorder and inorder arrays.

Folder: Binary_Trees
File: 330_Construct_the_Binary_Tree_from_Postorder_and_Inorder_Traversal.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Postorder last element is root. Traversed backward: build right child first, then left.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(inorder: list[int], postorder: list[int]) -> TreeNode:
    in_map = {val: idx for idx, val in enumerate(inorder)}
    post_idx = len(postorder) - 1
    
    def build(in_start, in_end):
        nonlocal post_idx
        if in_start > in_end:
            return None
            
        root_val = postorder[post_idx]
        root = TreeNode(root_val)
        post_idx -= 1
        
        root_idx = in_map[root_val]
        root.right = build(root_idx + 1, in_end)
        root.left = build(in_start, root_idx - 1)
        return root

    return build(0, len(inorder) - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    ino = [9, 3, 15, 20, 7]
    post = [9, 15, 7, 20, 3]
    root = optimal_solution(ino, post)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    print("Done.")
""",

    "331_Serialize_and_De_serialize_BT.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Problem Name: Serialize and Deserialize Binary Tree
Description: Convert binary tree to string and back.

Folder: Binary_Trees
File: 331_Serialize_and_De_serialize_BT.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N)
class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "#"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(",")
        idx = 0
        
        def build():
            nonlocal idx
            if vals[idx] == "#":
                idx += 1
                return None
            root = TreeNode(int(vals[idx]))
            idx += 1
            root.left = build()
            root.right = build()
            return root
            
        return build()

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    codec = Codec()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert deserialized.val == 1
    assert deserialized.left.val == 2
    assert deserialized.right.val == 3
    print("Done.")
""",

    "332_Morris_Preorder_Traversal_of_a_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Problem Name: Morris Preorder Traversal
Description: Preorder traversal in O(1) space.

Folder: Binary_Trees
File: 332_Morris_Preorder_Traversal_of_a_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Morris traversal establishes temporary links (threads) from rightmost node 
# of left subtree back to the current node.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
                
            if not prev.right:
                res.append(curr.val) # Preorder: record node before moving left
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 2, 3]
    print("Done.")
""",

    "333_Morris_Inorder_Traversal_of_a_Binary_Tree.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Problem Name: Morris Inorder Traversal
Description: Inorder traversal in O(1) space.

Folder: Binary_Trees
File: 333_Morris_Inorder_Traversal_of_a_Binary_Tree.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
                
            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                res.append(curr.val) # Inorder: record node when backtracking
                curr = curr.right
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 3, 2]
    print("Done.")
""",

    "334_Flatten_Binary_Tree_to_Linked_List.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Problem Name: Flatten Binary Tree to Linked List
Description: Flatten a binary tree to a singly linked list in-place.

Folder: Binary_Trees
File: 334_Flatten_Binary_Tree_to_Linked_List.py
\"\"\"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Traverse reverse postorder (Right, Left, Root) and track prev.
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode):
    prev = None
    
    def dfs(node):
        nonlocal prev
        if not node:
            return
        dfs(node.right)
        dfs(node.left)
        node.right = prev
        node.left = None
        prev = node

    dfs(root)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    optimal_solution(root)
    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3
    print("Done.")
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "Binary_Trees", "Code")
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
        
    print("All Binary Trees code solutions populated successfully!")

if __name__ == "__main__":
    main()
