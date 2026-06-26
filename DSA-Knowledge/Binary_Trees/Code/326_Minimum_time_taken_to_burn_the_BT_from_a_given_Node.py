"""
LeetCode Link: https://www.geeksforgeeks.org/problems/burning-tree/1
Problem Name: Burning Tree
Description: Find the minimum time to burn the entire tree starting from a target node.

Folder: Binary_Trees
File: 326_Minimum_time_taken_to_burn_the_BT_from_a_given_Node.py
"""

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
